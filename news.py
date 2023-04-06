import yfinance as yf
import json

# Define the list of stock tickers to retrieve news for
tickers = [ "TSLA","GLD","ASELS.IS"]

news_dict = {}

# Loop through the tickers and retrieve news data from Yahoo Finance API
for ticker in tickers:
    # Retrieve the news data for the current ticker
    stock = yf.Ticker(ticker)
    news = stock.news


    news_list = []
    for article in news:



        news_dict2 =  news_dict2 = {"title": "", "publisher": "", "link": "", "thumbnail": ""}
        if "title" in article:
            news_dict2["title"] = article["title"]
        if "publisher" in article:
            news_dict2["publisher"] = article["publisher"]
        if "link" in article:
            news_dict2["link"] = article["link"]
        if "thumbnail" in article:
            if "resolutions" in article["thumbnail"] and article["thumbnail"]["resolutions"]:
                news_dict2["thumbnail"] = article["thumbnail"]["resolutions"][0]["url"]
        news_list.append(news_dict2)

    # Add the news data to the dictionary
    news_dict[ticker] = news_list



with open("news_data.json", "w") as f:
    json.dump(news_dict, f)
