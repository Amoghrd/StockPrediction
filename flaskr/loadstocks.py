import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="sefall2021.cosnmrdyk6wi.us-east-2.rds.amazonaws.com",
    database='StockPrediction',
    user="root",
    password="SEFall2021"
)

def main():
    loadStockDataFromCSV()

def loadStockDataFromCSV():
    StockData = pd.read_csv("stocks.csv")
    StockData.columns = ['stock_id','stock_name']
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS stock;')
        cursor.execute('CREATE TABLE stock(stock_id nvarchar(50), stock_name nvarchar(50))')
        for row in StockData.index:
            sql = "INSERT INTO stock(stock_id,stock_name)VALUES(%s,%s);"
            cursor.execute(sql,(str(StockData.loc[row, 'stock_id']),str(StockData.loc[row, 'stock_name'])))
        connection.commit()

if __name__=="__main__": 
    main() 
