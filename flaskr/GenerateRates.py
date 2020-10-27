import yfinance as yf
import csv


def get_stock(ticker_name, days_number):
    tick = yf.Ticker(ticker_name)
    df = tick.history(period=str(days_number) + "d")
    return df


def Sort(arr):
    return sorted(arr, key=lambda x: x[2], reverse=True)


# Calculate slopes
def generateGrowthRates():
    rowList = []
    with open("stocks.csv") as f:
        # with open('stocks.csv') as f:
        reader = csv.reader(f)
        i = 100
        for row in reader:
            if row not in ["DLPH", "ASFI", "CETV", "BREW", "INWK", "MNTA", "AMTD"]:
                error = 0
                try:
                    df = get_stock(row[0], 30)
                except Exception as e:
                    print(e)
                    error = 1

                # Calculate slope and append to the top ten list
                if error == 0:
                    rowList.append(
                        [
                            row[0],
                            row[1],
                            (df["Close"][len(df["Close"]) - 1] - df["Close"][0])
                            / df["Close"][0],
                        ]
                    )
            i -= 1
    sortedList = Sort(rowList)
    # sortedList.insert(0, ["Ticker", "Name", "Slope"])
    with open("GrowthRates.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sortedList)


generateGrowthRates()
