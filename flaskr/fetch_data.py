import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import math
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import csv

def get_stock(ticker_name, days_number):
    tick = yf.Ticker(ticker_name)
    df = tick.history(period=str(days_number) + "d")
    return df


def regression(df, name, date):
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    # Attribute Reduction
    df["HL_PCT"] = (df["High"] - df["Low"]) / df["Close"] * 100.0
    df["PCT_change"] = (df["Close"] - df["Open"]) / df["Open"] * 100.0
    # New and more statistically important attributes
    df = df[["Close", "HL_PCT", "PCT_change", "Volume"]]

    forecast_col = "Close"
    # which column to forecast

    df.fillna(value=-99999, inplace=True)
    forecast_out = int(math.ceil(0.1 * len(df)))
    # what percent of days from total number of days to forecast
    df["label"] = df[forecast_col].shift(-forecast_out)

    # preprocessing and subsetting data for training
    X = np.array(df.drop(["label"], 1))
    X = preprocessing.scale(X)
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]

    df.dropna(inplace=True)
    y = np.array(df["label"])

    # splitting data for test and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # calling Linear Regression funtion
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)

    # Model Trained now printing accuracy
    print("Confidence - ", confidence)

    forecast_set = clf.predict(X_lately)
    df["Forecast"] = np.nan

    last_date = df.iloc[-1].name
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day

    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += 86400
        df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

    optimistic = df["Forecast"] * 1.05
    pessimistic = df["Forecast"] * 0.95
    indexvalues = df.index
    covidflag = -1
    s = "22/02/2020"
    covidtime = datetime.datetime.strptime(s, "%d/%m/%Y")
    for i in range(len(indexvalues)):
        if indexvalues[i] >= covidtime:
            covidflag = i
            break

    for i in range(len(df)):
        if not np.isnan(optimistic[i]):
            df["Close"][i] = df["Forecast"][i]
            optimistic[i] = df["Forecast"][i]
            pessimistic[i] = df["Forecast"][i]
            break
    # plotting data with the original and the predicted
    plt.style.use("dark_background")
    plt.figure(figsize=(8, 4))
    if covidflag == -1:
        plt.plot(df["Close"], color="lime", label="Actual")
    else:
        plt.plot(df["Close"][:covidflag], color="lime", label="Before Covid")
        if covidflag == 0:
            plt.plot(df["Close"][covidflag:], color="yellow", label="After Covid")
        else:
            plt.plot(df["Close"][covidflag - 1 :], color="yellow", label="After Covid")
    plt.fill_between(
        optimistic.index,
        optimistic,
        pessimistic,
        color="lightgrey",
        label="95% confidence interval",
    )
    plt.plot(df["Forecast"], color="red", label="Forecast")
    plt.legend(loc=0)
    plt.xlabel("Date")
    plt.ylabel("Price")
    # plt.show()
    plt.savefig(fname="flaskr/static/" + name + "-" + date + ".png", format="png")


def Sort(arr): 
    return(sorted(arr, key = lambda x: x[2], reverse=True))

#Calculate slopes 
def generateGrowthRates():
    rowList = []
    with open('flaskr/static/stocks.csv') as f:
    #with open('stocks.csv') as f:
        reader = csv.reader(f)
        i = 100
        for row in reader:
            if row not in ['DLPH', 'ASFI', 'CETV', 'BREW', 'INWK', 'MNTA', 'AMTD']:
                error = 0
                try:
                    df = get_stock(row[0], 30)
                except Exception as e:
                    print(e)
                    error = 1

                #Calculate slope and append to the top ten list
                if error == 0:
                    rowList.append([
                        row[0],
                        row[1],
                        (df['Close'][len(df['Close'])-1] - df['Close'][0])/df['Close'][0]
                    ])
            i -= 1
    sortedList = Sort(rowList)
    #sortedList.insert(0, ["Ticker", "Name", "Slope"])
    with open('GrowthRates.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sortedList)