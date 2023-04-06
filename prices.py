import requests
import json

tickers = ["TSLA","GLD","ASELS.IS"]

start_date = "2022-04-02"
end_date = "2022-04-04"

url = f"https://query1.finance.yahoo.com/v7/finance/chart/{{}}?range=2d&interval=1d&indicators=quote&includeTimestamps=true"


data_dict = {}

# Loop through the tickers and retrieve data from Yahoo Finance API
for ticker in tickers:

    current_url = url.format(ticker)

    response = requests.get(current_url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})

    data = response.json()



    # Extract the data for the specified date range
    timestamps = data["chart"]["result"][0]["timestamp"]
    prices = data["chart"]["result"][0]["indicators"]["quote"][0]
    data_dict[ticker]= {"Timestamp": timestamps, "Open": prices["open"], "High": prices["high"], "Low": prices["low"],
                 "Close": prices["close"], "Volume": prices["volume"]}



with open("price_data.json", "w") as f:
    json.dump(data_dict, f)

