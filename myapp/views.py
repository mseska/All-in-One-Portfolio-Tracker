import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import   Stock2
from django.db import connection
from .dbFunctions import * 
import json
import random

from django.http import JsonResponse

from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

from rest_framework.decorators import api_view
from rest_framework.response import Response


import yfinance as yf
import json
import schedule
import time
import threading
import requests
import json
import feedparser

from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

#from django.http import JsonResponse


class ReactView(APIView):
    def get(self,request):
        output = [{'employee':output.employee,'department':output.department} for output in React.objects.all()]
        return Response(output)

    def post(self,request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# Create your views here.
def index(request):
    print("deneöe")
    #return HttpResponse('<h1>Hey, Welcome</h1>')
    name = 'Mert'
    #feature1 = Feature()
    #feature1.id = 0
    #feature1.name = 'Fast'
    #feature1.description = 'Our service is fast'
    news_update_thread = threading.Thread(target=update_news_periodically)
    news_update_thread.start()

    prices_update_thread = threading.Thread(target=update_prices_periodically)
    prices_update_thread.start()
    return render(request,'a.html',{'name':name})

def input(request):
    print("deneöe")

    return render(request,'input.html')

def inputCheck(request):
    with open('output.json') as json_file:
        data = json.load(json_file)

        # Print the type of data variable
        #print("Type:", type(data))

        # Print the data of dictionary
        #print("\nPeople1:", data['people1'])
        #print("\nPeople2:", data['people2'])

    inputGet = request.POST['inputText']
    currency = data["chart"]["result"][0]["meta"]["currency"]
    symbol = data["chart"]["result"][0]["meta"]["symbol"]
    #timestamp = data["chart"]["result"][0]["timestamp"]
    #high = data["chart"]["result"][0]["timestamp"]["indicators"]["quote"][0]["high"]
    #low = data["chart"]["result"][0]["timestamp"]["indicators"]["quote"][0]["low"]
    #open = data["chart"]["result"][0]["timestamp"]["indicators"]["quote"][0]["open"]
    #close = data["chart"]["result"][0]["timestamp"]["indicators"]["quote"][0]["close"]
    #volume = data["chart"]["result"][0]["timestamp"]["indicators"]["quote"][0]["volume"]

    #my_custom_sql("INSERT INTO `comp491`.`asset_history` (`keysforassets`, `currency`, `asset_name`) VALUES ('"+inputGet+"', '"+currency+"', '"+symbol+"')",connection)
    output = my_custom_sql("SELECT * FROM `comp491`.`asset_history`",connection)
    print(output)
    return render(request,'inputCheck.html',{'inputText':inputGet,'wordCount':output})

def static(request):
    return render(request,'static.html')

def my_custom_sql(query,connection):
    with connection.cursor() as cursor:
        cursor.execute(query)
        #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])

        row = cursor.fetchall()

    return row


def my_custom_news_sql(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result

def list(request):
    list = my_custom_sql("SELECT * FROM `comp491`.`asset_history`",connection)
    returnList = []
    #print(list)

    for asset in list:
        #print(type(asset))
        newAsset = Assets()
        newAsset.AssetName = asset[2]
        newAsset.value = asset[3]
        returnList.append(newAsset)

    from django.contrib.auth.tokens import default_token_generator


    return render(request,'list.html',{'list':returnList})

@api_view(['POST'])
#@api_view(['GET'])
def add_item(request):
    print("POST METHOD WORKS")
    print(request.data.get('name'))
    
    # print("GET METHOD WORKS")
    # print(request.GET.get('name'))
    
    #serializer = ItemSerializer(data=request.data)
    #if serializer.is_valid():
    #    serializer.save()
    #    print(serializer.data)
    #
    #print(request)
    # print(request.method)

    # # Print the request path
    # print(request.path)

    # # Print the request headers
    # print(request.headers)

    # # Print the request body
    # print(request.body)    
    #return Response(request.GET.get('name'), status=201)
    return Response(request.data.get('name'), status=201) #POST İÇİN

@api_view(['GET'])
def get_myasset_list(request):
    # print("GET METHOD WORKS")
    # print(request.GET)
    token = request.META.get('HTTP_AUTHORIZATION')
    print(token,"hop alo token")
    id = get_id_with_token(token)
    print(id,"hop alo id")
    
    Assets = get_assets_with_user_id(id)   
    print(Assets)
    
    # #TODO delete after development phase of news data retrieval
    # update_news_data()
    # update_prices()

    # news_update_thread = threading.Thread(target=update_news_periodically)
    # news_update_thread.start()
    # prices_update_thread = threading.Thread(target=update_prices_periodically)
    # prices_update_thread.start()

    list = my_custom_sql("SELECT * FROM `comp491`.`asset_history`",connection)
    returnList = []
    # print(list,"databaseden gelen veri")
    
    #Bunu uncomment etmeden önce databasein düzenlenmesi lazım. 
    # 1-auth_user artık user information tutucu ona göre foreign keyler tutulmalı
    # 2-user information, asset information ve asset_user_ownership birbiriyle uyumlu veri içermeli
    for stock in Assets:
    #for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        if stock[0] != 'database':
            newAsset.symbol = stock[0]
            newAsset.price = stock[1]
            newAsset.change = get_daily_change(newAsset.symbol, newAsset.price)
        #print(stock[1])
        #print(stock[2])
        #print(stock[3])
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.change,"newAsset.change")
        # print(newAsset,"newAsset")
            returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    print(serialized_objects, "serialized")
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)
    

@api_view(['GET'])
def get_crypto_list(request):
    # print("GET METHOD WORKS")
    # print(request.GET)

    list = my_custom_sql("SELECT * FROM comp491.asset_information WHERE asset_information.description = 'CRYPTOCURRENCY';",connection) #table will be changed
  
    returnList = []
    # print(list,"databaseden gelen veri")
    
    for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[1]
        newAsset.price = stock[2]
        newAsset.change = get_daily_change(newAsset.symbol, newAsset.price)
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.change,"newAsset.change")
        # print(newAsset,"newAsset")
        returnList.append(newAsset)
    # print(returnList,liste databaseden alındı")
    
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)
    

@api_view(['GET'])
def get_stock_list(request):
    # print("GET METHOD WORKS")
    # print(request.GET)

    list = my_custom_sql("SELECT * FROM comp491.asset_information WHERE asset_information.description = 'EQUITY';",connection) #table will be changed
  
    returnList = []
    # print(list,"databaseden gelen veri")
    
    for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[1]
        newAsset.price = stock[2]
        newAsset.change = get_daily_change(newAsset.symbol, newAsset.price)
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.change,"newAsset.change")
        # print(newAsset,"newAsset")
        returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)




@api_view(['GET'])
def get_commodity_list(request):
    # print("GET METHOD WORKS")
    # print(request.GET)

    #TODO delete after development phase of news data retrieval
    tickersList = ["TSLA", "GLD", "ASELS.IS", "ETH-USD","BTC-USD"]
    update_news_data_general()
    #update_prices()
    #fill_db_for_long_term(30)



    news_update_thread = threading.Thread(target=update_news_periodically)
    news_update_thread.start()
    prices_update_thread = threading.Thread(target=update_prices_periodically)
    prices_update_thread.start()
    list = my_custom_sql("SELECT * FROM comp491.asset_information WHERE asset_information.description = 'ETF';",connection) #table will be changed
    
    returnList = []
    # print(list,"databaseden gelen veri")
    
    for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[1]
        newAsset.price = stock[2]
        newAsset.change = get_daily_change(newAsset.symbol, newAsset.price)
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.change,"newAsset.change")
        # print(newAsset,"newAsset")
        returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)

def update_news_data_general():
    print("json is being updated\n\n\n\n")
    # Define the list of stock tickers to retrieve news for
    tickers = ["general"]

    news_dict = {}
    news_dict["news"] = []
    # Loop through the tickers and retrieve news data from Yahoo Finance API
    for ticker in tickers:
        # Retrieve the news data for the current ticker
        stock = yf.Ticker(ticker)
        news = stock.news

        news_list = []
        for article in news:
            news_dict2 = {"title": "", "publisher": "", "link": "", "thumbnail": ""}
            if "title" in article:
                news_dict2["title"] = article["title"]
            if "publisher" in article:
                news_dict2["publisher"] = article["publisher"]
            if "link" in article:
                news_dict2["link"] = article["link"]
            if "thumbnail" in article:
                if "resolutions" in article["thumbnail"] and article["thumbnail"]["resolutions"]:
                    news_dict2["thumbnail"] = article["thumbnail"]["resolutions"][0]["url"]
            else:
                news_dict2[
                    "thumbnail"] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSriG88tNG1fjZY9tjMkWpziGZDukdu_2i2Cg&usqp=CAU"

            news_list.append(news_dict2)

        # Add the news data to the dictionary
        news_dict["news"].extend(news_list)
    random.shuffle(news_dict["news"])

    with open("news_data_general.json", "w") as f:
        json.dump(news_dict, f)
    print("jsonupdated\n\n\n\n")

    print("dbupdating\n\n\n\n")
    delete_query = "DELETE FROM `comp491`.`news_general` WHERE TIMESTAMPDIFF(DAY, addDate, NOW()) > 7"
    my_custom_news_sql(delete_query)

    with open('news_data.json') as f2:
        news_data = json.load(f2)

    # Loop through the news items and insert them into the MySQL database if they don't already exist
    for ticker, news_items in news_data.items():

        for news_item in news_items:
            title = news_item['title']
            publisher = news_item['publisher']
            link = news_item['link']
            thumbnail = news_item['thumbnail']
            asset = ticker

            # Check if the news already exists in the database
            query = "SELECT * FROM `comp491`.`news_general` WHERE title=%s AND publisher=%s AND link=%s"
            result = my_custom_news_sql(query, (title, publisher, link))

            if len(result) > 0:
                # The news already exists in the database, so skip inserting it
                print(f"News '{title}' already exists in the database")
            else:
                # Insert the news into the database
                query = "INSERT INTO `comp491`.`news_general` (title, publisher, link, thumbnail, asset, addDate) VALUES (%s, %s, %s, %s, %s, NOW())"
                my_custom_news_sql(query, (title, publisher, link, thumbnail, asset))
                print(f"Inserted gemmneral news '{title}' into the database")

    print("dbupdated\n\n\n\n")


def update_news_data(tickersList):
    print("json is being updated\n\n\n\n")
    # Define the list of stock tickers to retrieve news for
    tickers = tickersList
    
    news_dict = {}
    news_dict["news"] = []
    # Loop through the tickers and retrieve news data from Yahoo Finance API
    for ticker in tickers:
        # Retrieve the news data for the current ticker
        stock = yf.Ticker(ticker)
        news = stock.news

        news_list = []
        for article in news:
            news_dict2 = {"title": "", "publisher": "", "link": "", "thumbnail": ""}
            if "title" in article:
                news_dict2["title"] = article["title"]
            if "publisher" in article:
                news_dict2["publisher"] = article["publisher"]
            if "link" in article:
                news_dict2["link"] = article["link"]
            if "thumbnail" in article:
                if "resolutions" in article["thumbnail"] and article["thumbnail"]["resolutions"]:
                    news_dict2["thumbnail"] = article["thumbnail"]["resolutions"][0]["url"]
            else:
                    news_dict2["thumbnail"] ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSriG88tNG1fjZY9tjMkWpziGZDukdu_2i2Cg&usqp=CAU"
            
            news_list.append(news_dict2)

        # Add the news data to the dictionary
        news_dict["news"].extend(news_list)
    random.shuffle(news_dict["news"])

    with open("news_data.json", "w") as f:
        json.dump(news_dict, f)
    print("jsonupdated\n\n\n\n")

    print("dbupdating\n\n\n\n")
    delete_query = "DELETE FROM `comp491`.`news` WHERE TIMESTAMPDIFF(DAY, addDate, NOW()) > 7"
    my_custom_news_sql(delete_query)

    with open('news_data.json') as f2:
        news_data = json.load(f2)


    # Loop through the news items and insert them into the MySQL database if they don't already exist
    for ticker, news_items in news_data.items():



        for news_item in news_items:
            title = news_item['title']
            publisher = news_item['publisher']
            link = news_item['link']
            thumbnail = news_item['thumbnail']
            asset = ticker

            # Check if the news already exists in the database
            query = "SELECT * FROM `comp491`.`news` WHERE title=%s AND publisher=%s AND link=%s"
            result = my_custom_news_sql(query, (title, publisher, link))

            if len(result) > 0:
                # The news already exists in the database, so skip inserting it
                print(f"News '{title}' already exists in the database")
            else:
                # Insert the news into the database
                query = "INSERT INTO `comp491`.`news` (title, publisher, link, thumbnail, asset, addDate) VALUES (%s, %s, %s, %s, %s, NOW())"
                my_custom_news_sql(query, (title, publisher, link, thumbnail, asset))
                print(f"Inserted news '{title}' into the database")







    print("dbupdated\n\n\n\n")

    pass

def fill_db_for_long_term(howmanydays):
    tickers = ["UNG"]

    tickers = [
        "ASELS.IS", "CEEK-USD", "TSLA",

        "GARAN.IS", "AKBNK.IS", "KCHOL.IS", "SISE.IS", "ULKER.IS",
        "ISCTR.IS", "TCELL.IS", "BIMAS.IS", "YKBNK.IS", "VAKBN.IS",

        "AAPL", "MSFT", "AMZN", "GOOGL",
        "BRK-B", "V", "JNJ", "WMT", "NVDA",

        "GLD", "SLV", "USO", "UNG", "DBC",
        "DBA", "DBB", "DBE",

        "BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "XRP-USD",
        "DOGE-USD", "AVAX-USD",

        "KO", "PEP", "MCD", "INTC", "DIS",
        "ENJSA.IS", "VESTL.IS", "ARCLK.IS", "CRFSA.IS", "TUPRS.IS"
    ]
    tickers = ["UNG"]


    start_date = "2022-04-02"
    end_date = "2022-04-04"

    url = f"https://query1.finance.yahoo.com/v7/finance/chart/{{}}?range="+str(howmanydays)+"d&interval=1d&indicators=quote&includeTimestamps=true"

    data_dict = {}
    index = 0

    # Loop through the tickers and retrieve data from Yahoo Finance API
    for ticker in tickers:
        current_url = url.format(ticker)

        index += 1

        response = requests.get(current_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})

        data = response.json()

        # Extract the data for the specified date range
        typeOfasset = data["chart"]["result"][0]["meta"]["instrumentType"]
        timestamps = data["chart"]["result"][0]["timestamp"]
        prices = data["chart"]["result"][0]["indicators"]["quote"][0]
        data_dict[ticker] = {"Timestamp": timestamps, "Type": typeOfasset, "Open": prices["open"],
                             "High": prices["high"],
                             "Low": prices["low"],
                             "Close": prices["close"], "Volume": prices["volume"]}

    with open("price_data.json", "w") as f:
        json.dump(data_dict, f)

    print("dbupdating\n\n\n\n")
    # delete_query = "DELETE FROM `comp491`.`prices` WHERE TIMESTAMPDIFF(DAY, addDate, NOW()) > 7"
    # my_custom_news_sql(delete_query)

    with open('price_data.json') as f2:
        price_data = json.load(f2)

    # Loop through the news items and insert them into the MySQL database if they don't already exist
    for ticker, price_item in price_data.items():

        for i in range(len(price_item['Close'])):

            timestamp = price_item['Timestamp'][i]
            openn = price_item['Open'][i]
            high = price_item['High'][i]
            low = price_item['Low'][i]
            close = price_item['Close'][i]
            volume = price_item['Volume'][i]
            description = price_item['Type']
            asset = ticker

            name = asset
            current_value = close
            date=datetime.fromtimestamp(timestamp)
            check_query = "SELECT asset_id FROM `comp491`.asset_information WHERE name = %s"
            insert_query = "INSERT INTO `comp491`.asset_information (name, current_value, description) VALUES (%s, %s, %s)"
            find_max_query = "SELECT MAX(keysforassets) FROM `comp491`.asset_history"
            insert_query_for_historical = "INSERT INTO `comp491`.asset_history (keysforassets,currency, asset_name, value,date) VALUES (%s, %s,%s, %s,%s)"


            # query = "SELECT * FROM `comp491`.`asset_information` WHERE name=%s AND DATE(addDate) = DATE(NOW()) "
            #result = my_custom_news_sql(check_query, (asset))
            maxInd = my_custom_news_sql(find_max_query, params=None)


                # Item does not exist, so insert a new row
                #my_custom_news_sql(insert_query, (name, current_value, description))

                # Item already exists, so update its current value


            newind = maxInd[0][0] + 1

            my_custom_news_sql(insert_query_for_historical,(newind, 'USD', name, current_value, date))
            print("Inserted "+str(name)+" -> "+str(date))


        # print(f"Inserted prices  into the database")

    '''

        # Check if the news already exists in the database
        # query = "SELECT * FROM `comp491`.`prices` WHERE asset=%s AND DATE(addDate) = DATE(NOW()) "
        # result = my_custom_news_sql(query, (asset))

        # if len(result) > 0:
        # The news already exists in the database, so skip inserting it
        #   print(f"already exists in the database")
        #:else:
        # Insert the news into the database
        # query = "INSERT INTO `comp491`.`prices` (timestamp, open, high, low, close,volume, asset, addDate) VALUES (%s,%s,%s, %s, %s, %s, %s, NOW())"
        # my_custom_news_sql(query, (timestamp, openn, high, low, close, volume, asset))
        # print(f"Inserted prices  into the database")


    ''''''  THE CODE BELOW CAN BE USED TO POPULATE SO WE MAY CONSIDER NOT DELETING
            for i in range(len(price_item['Close'])):


                timestamp = price_item['Timestamp'][i]
                openn = price_item['Open'][i]
                high = price_item['High'][i]
                low = price_item['Low'][i]
                close = price_item['Close'][i]
                volume = price_item['Volume'][i]
                description = price_item['Type']
                asset = ticker

                name = asset
                current_value = close
                check_query = "SELECT asset_id FROM `comp491`.asset_information WHERE name = %s"
                insert_query = "INSERT INTO `comp491`.asset_information (name, current_value, description) VALUES (%s, %s, %s)"
                find_max_query ="SELECT MAX(keysforassets) FROM `comp491`.asset_history"
                insert_query_for_historical="INSERT INTO `comp491`.asset_history (keysforassets,currency, asset_name, value,date) VALUES (%s, %s,%s, %s,DATE_SUB(NOW(), INTERVAL %s DAY))"
                update_query = "UPDATE `comp491`.asset_information SET current_value = %s WHERE name = %s"

                # query = "SELECT * FROM `comp491`.`asset_information` WHERE name=%s AND DATE(addDate) = DATE(NOW()) "
                result = my_custom_news_sql(check_query, (asset))
                maxInd=my_custom_news_sql(find_max_query,params=None)





                if result == 0:
                    # Item does not exist, so insert a new row
                    my_custom_news_sql(insert_query, (name, current_value, description))
                else:
                    # Item already exists, so update its current value
                    newind=maxInd[0][0]+1
                    my_custom_news_sql(insert_query_for_historical, (newind,'USD', name, current_value,(29-i)))
                    my_custom_news_sql(update_query, (current_value, name))

                # print(f"Inserted prices  into the database")

                # Check if the news already exists in the database
                #query = "SELECT * FROM `comp491`.`prices` WHERE asset=%s AND DATE(addDate) = DATE(NOW()) "
                #result = my_custom_news_sql(query, (asset))

                #if len(result) > 0:
                    # The news already exists in the database, so skip inserting it
                 #   print(f"already exists in the database")
                #:else:
                    # Insert the news into the database
                    #query = "INSERT INTO `comp491`.`prices` (timestamp, open, high, low, close,volume, asset, addDate) VALUES (%s,%s,%s, %s, %s, %s, %s, NOW())"
                    #my_custom_news_sql(query, (timestamp, openn, high, low, close, volume, asset))
                    #print(f"Inserted prices  into the database")


        '''
    print("dbupdated\n\n\n\n")

    pass

def update_prices():
    #tickers = ["TSLA"]

    tickers =  [
    "ASELS.IS", "CEEK-USD","TSLA",

  "GARAN.IS", "AKBNK.IS", "KCHOL.IS", "SISE.IS", "ULKER.IS",
  "ISCTR.IS", "TCELL.IS", "BIMAS.IS", "YKBNK.IS", "VAKBN.IS",


  "AAPL", "MSFT", "AMZN", "GOOGL",
  "BRK-B", "V", "JNJ", "WMT", "NVDA",


  "GLD", "SLV", "USO", "UNG", "DBC",
  "DBA", "DBB", "DBE",


  "BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "XRP-USD",
   "DOGE-USD", "AVAX-USD",


  "KO", "PEP", "MCD", "INTC", "DIS",
  "ENJSA.IS", "VESTL.IS", "ARCLK.IS", "CRFSA.IS", "TUPRS.IS"
]


    start_date = "2022-04-02"
    end_date = "2022-04-04"

    url = f"https://query1.finance.yahoo.com/v7/finance/chart/{{}}?range=0d&interval=1d&indicators=quote&includeTimestamps=true"

    data_dict = {}
    index =0

    # Loop through the tickers and retrieve data from Yahoo Finance API
    for ticker in tickers:
        current_url = url.format(ticker)
        #example url provided by api
        #https://query1.finance.yahoo.com/v7/finance/chart/AVAX-USD?range=0d&interval=1d&indicators=quote&includeTimestamps=true


        index+=1

        response = requests.get(current_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})

        data = response.json()

        # Extract the data for the specified date range
        typeOfasset = data["chart"]["result"][0]["meta"]["instrumentType"]
        timestamps = data["chart"]["result"][0]["timestamp"]
        prices = data["chart"]["result"][0]["indicators"]["quote"][0]
        data_dict[ticker] = {"Timestamp": timestamps, "Type": typeOfasset, "Open": prices["open"],
                             "High": prices["high"],
                             "Low": prices["low"],
                             "Close": prices["close"], "Volume": prices["volume"]}


    with open("price_data.json", "w") as f:
        json.dump(data_dict, f)

    print("dbupdating\n\n\n\n")
    #delete_query = "DELETE FROM `comp491`.`prices` WHERE TIMESTAMPDIFF(DAY, addDate, NOW()) > 7"
    #my_custom_news_sql(delete_query)

    with open('price_data.json') as f2:
        price_data = json.load(f2)

    # Loop through the news items and insert them into the MySQL database if they don't already exist
    for ticker, price_item in price_data.items():



        timestamp = price_item['Timestamp'][0]
        openn = price_item['Open'][0]
        high = price_item['High'][0]
        low = price_item['Low'][0]
        close = price_item['Close'][0]
        volume = price_item['Volume'][0]
        description = price_item['Type']
        asset = ticker

        name = asset
        current_value = close
        check_query = "SELECT asset_id FROM `comp491`.asset_information WHERE name = %s"
        insert_query = "INSERT INTO `comp491`.asset_information (name, current_value, description) VALUES (%s, %s, %s)"
        find_max_query = "SELECT MAX(keysforassets) FROM `comp491`.asset_history"
        insert_query_for_historical = "INSERT INTO `comp491`.asset_history (keysforassets,currency, asset_name, value,date) VALUES (%s, %s,%s, %s,%s)"
        update_query = "UPDATE `comp491`.asset_information SET current_value = %s WHERE name = %s"

        # query = "SELECT * FROM `comp491`.`asset_information` WHERE name=%s AND DATE(addDate) = DATE(NOW()) "
        result = my_custom_news_sql(check_query, (asset))
        maxInd = my_custom_news_sql(find_max_query, params=None)

        if result == 0:
            # Item does not exist, so insert a new row
            my_custom_news_sql(insert_query, (name, current_value, description))
        else:
            # Item already exists, so update its current value
            newind = maxInd[0][0] + 1
            my_custom_news_sql(insert_query_for_historical, (newind, 'USD', name, current_value,datetime.fromtimestamp(timestamp)))
            my_custom_news_sql(update_query, (current_value, name))

        # print(f"Inserted prices  into the database")

    '''

        # Check if the news already exists in the database
        # query = "SELECT * FROM `comp491`.`prices` WHERE asset=%s AND DATE(addDate) = DATE(NOW()) "
        # result = my_custom_news_sql(query, (asset))

        # if len(result) > 0:
        # The news already exists in the database, so skip inserting it
        #   print(f"already exists in the database")
        #:else:
        # Insert the news into the database
        # query = "INSERT INTO `comp491`.`prices` (timestamp, open, high, low, close,volume, asset, addDate) VALUES (%s,%s,%s, %s, %s, %s, %s, NOW())"
        # my_custom_news_sql(query, (timestamp, openn, high, low, close, volume, asset))
        # print(f"Inserted prices  into the database")


    ''''''  THE CODE BELOW CAN BE USED TO POPULATE SO WE MAY CONSIDER NOT DELETING
        for i in range(len(price_item['Close'])):


            timestamp = price_item['Timestamp'][i]
            openn = price_item['Open'][i]
            high = price_item['High'][i]
            low = price_item['Low'][i]
            close = price_item['Close'][i]
            volume = price_item['Volume'][i]
            description = price_item['Type']
            asset = ticker

            name = asset
            current_value = close
            check_query = "SELECT asset_id FROM `comp491`.asset_information WHERE name = %s"
            insert_query = "INSERT INTO `comp491`.asset_information (name, current_value, description) VALUES (%s, %s, %s)"
            find_max_query ="SELECT MAX(keysforassets) FROM `comp491`.asset_history"
            insert_query_for_historical="INSERT INTO `comp491`.asset_history (keysforassets,currency, asset_name, value,date) VALUES (%s, %s,%s, %s,DATE_SUB(NOW(), INTERVAL %s DAY))"
            update_query = "UPDATE `comp491`.asset_information SET current_value = %s WHERE name = %s"

            # query = "SELECT * FROM `comp491`.`asset_information` WHERE name=%s AND DATE(addDate) = DATE(NOW()) "
            result = my_custom_news_sql(check_query, (asset))
            maxInd=my_custom_news_sql(find_max_query,params=None)





            if result == 0:
                # Item does not exist, so insert a new row
                my_custom_news_sql(insert_query, (name, current_value, description))
            else:
                # Item already exists, so update its current value
                newind=maxInd[0][0]+1
                my_custom_news_sql(insert_query_for_historical, (newind,'USD', name, current_value,(29-i)))
                my_custom_news_sql(update_query, (current_value, name))

            # print(f"Inserted prices  into the database")

            # Check if the news already exists in the database
            #query = "SELECT * FROM `comp491`.`prices` WHERE asset=%s AND DATE(addDate) = DATE(NOW()) "
            #result = my_custom_news_sql(query, (asset))

            #if len(result) > 0:
                # The news already exists in the database, so skip inserting it
             #   print(f"already exists in the database")
            #:else:
                # Insert the news into the database
                #query = "INSERT INTO `comp491`.`prices` (timestamp, open, high, low, close,volume, asset, addDate) VALUES (%s,%s,%s, %s, %s, %s, %s, NOW())"
                #my_custom_news_sql(query, (timestamp, openn, high, low, close, volume, asset))
                #print(f"Inserted prices  into the database")


    '''
    print("dbupdated\n\n\n\n")

    pass



def update_news_periodically():
    while True:
        now = datetime.now()
        if now.second == 0 and now.minute== 0:  # Run update_news_data() once per hour at the start of the hour
            tickersList = ["TSLA", "GLD", "ASELS.IS", "ETH-USD","BTC-USD"]
            update_news_data(tickersList)
            update_news_data_general()
        time.sleep(1)



def update_prices_periodically():
    while True:
        now = datetime.now()
        if now.second == 0 and now.minute == 0:  # Run update_news_data() once per hour at the start of the hour
            update_prices()
        time.sleep(1)


@api_view(['GET'])
def news_api(request):
    with open('news_data.json') as f:
        data = json.load(f)
    #print(data)
    return JsonResponse(data, safe=False)


@api_view(['POST','OPTIONS'])           
def login_generate_token(request):
    print("POST METHOD WORKS - in login generate token")
    email = request.data.get('eMail') 
    password = request.data.get('PassWord')

    print(email, "- email")
    print(password, "- password")
    
    user = authenticate(request, username=email, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        print("this user exist, return the token")
        print(user.id, "this si the user id")
        return JsonResponse({'token': token.key,  'id' : user.id}, status = 200)
    else:
        print("user does not exist:(")
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

def activate(request, uidb64, token):
    print("entered activate(), confirming the email...")
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(user.email, "------------------------------- of")
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None:
    #and account_activation_token.check_token(user, token):
        user.is_active = 1
        user.save()
        print("before the mail is sent: ", user.is_active)
        print("email confirmed!")
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return HttpResponseRedirect('http://localhost:3000')
        # return redirect('http://localhost:3000') #TODO
        #return JsonResponse({'token': token.key}, status=201)
    else:
        print("sorry could not confirmed the email")
        messages.error(request, 'Activation link is invalid!')

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from .tokens import account_activation_token
from django.contrib import messages


def send_verification_email(request, user, name, token):
    print("activating the email confirmation...") 

    mail_subject = 'Activate Your Account'
    print(user.username, "this is the username to be printed to the email")
    message = render_to_string('template_activate_account.html', {
        'user': name, 
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token,
        #account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    print(user.is_active, "inside send-verification--------------------")
    return EmailMessage(mail_subject, message, to=[user.username])

@api_view(['POST'])           
def signup_generate_token(request):
    print("POST METHOD WORKS - in signup generate token")
    name = request.data.get('name')
    surname = request.data.get('surname')
    email = request.data.get('email') #uppercase falan degisebilir
    password = request.data.get('password')

    print(name, "- name")
    print(surname, "- surname")
    print(email, "- email")
    print(password, "- password")

    #email must be unique, check the emails:
    if User.objects.filter(email=email).exists():
        print("invalid email address:(((")
        return JsonResponse({'error': 'User with this email already exists'}, status=409)

    #create a user:
    user = User.objects.create_user(username=email, email=email, password=password)
    # user.is_active = False

    #to check whether the user is empty or not:
    print(user.email, "hello")
    print(user.password)

    user = authenticate(request, username=email, password=password)
    user.first_name = name
    user.last_name = surname
    user.is_active = 0
    user.save()
    print(user, "after authenticate")

    # print(user.password)
   
    if user is not None:
        print("user created")
        #login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        # uidb64 = urlsafe_base64_encode(force_bytes(user.id))
        #activate(request, uidb64, token)
        verification_mail = send_verification_email(request, user, name, token)
        if verification_mail.send():
            print(user.is_active, "------------------ sent the email")
            messages.success(request, f'Dear <b>{name}</b>, please go to you email <b>{email}</b> inbox and click on \
            # received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
            print("email sent !!!!!!!")
        return JsonResponse({'token': token.key, 'id' : user.id}, status=201)
    else:
        print("user is not created sorry")
        return JsonResponse({'error': 'Invalid credentials'}, status = 401)


@api_view(['GET'])
def get_user_info(request):
    #user = User.objects.get(username='ysm1')
    data = request.GET
    #print("thsi is the data", data)
    id = request.GET.get("id")
    print( "this is the id: ", id)
    if id is not None:
        user = User.objects.get(id=id)
        if user is not None and user.is_active: #if request.user.is_authenticated:
            print("user exists!")
            #print(user.username)
            #print(user.first_name, "- here is the first name")

            #user = authenticate(request, username=user.username, password=user.password) -> returns None??????

            login(request, user)
            #print(user, "after login")

            serializer = UserSerializer(user)
            #print(serializer.data, "- serializer data")
            print("found the user, sending the name field...")

            return JsonResponse(serializer.data)
        else:
            print("sorry could not find the user")
            #return JsonResponse({'error': 'Invalid'}, status = 401) #bu dogru mu burda
    else:
        print("id returns none")
        #return JsonResponse({'error': 'Invalid'}, status = 401) #bu dogru mu burda

@api_view(['GET'])
def get_portfolios(request):
    
    
    print("GET METHOD WORKS - in get portfolios")
    
    token  = request.GET.get("token")
    id = get_id_with_token(token)
    get_portfolios = get_portfolio_ids_with_user_id(id)
    returnDict = {}
    returnDict["length"] = len(get_portfolios)
    for index in range(len(get_portfolios)):
        asset_ids = get_asset_ids_with_portfolio_id(get_portfolios[index])
        returnDict[index] = {}
        
        name = get_portfolio_name_with_portfolio_id(get_portfolios[index])
        
        data = []
        #print(asset_ids)
        for asset_id in asset_ids:
            amount = get_total_amount_of_an_asset(asset_id,get_portfolios[index])
            asset_name = get_asset_name_with_asset_id(asset_id)
            current_value = get_asset_value_with_asset_id(asset_id)
            #print(name,amount,get_portfolios[index])
            currentAsset = {}
            currentAsset["name"] = asset_name
            currentAsset ["value"] = round(amount*float(current_value),2)
            data.append(currentAsset)

        returnDict[index]["name"] = name
        returnDict[index]["id"] = get_portfolios[index]
        returnDict[index]["data"] = data    
    
    #print(returnDict)
        
    #serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    #print(serialized_objects, "serialized")
    return JsonResponse(returnDict, safe=False)

@api_view(['GET'])
def get_portfolio_data(request):
    print("GET METHOD WORKS - in get portfolio data")
    token = request.headers.get('Authorization')
    selected_portfolio = request.headers.get('portfolio')

    asset_ids = get_asset_ids_with_portfolio_id(selected_portfolio)
    data = []
    for asset_id in asset_ids:
        amount = get_total_amount_of_an_asset(asset_id,selected_portfolio)
        asset_name = get_asset_name_with_asset_id(asset_id)
        current_value = get_asset_value_with_asset_id(asset_id)
        currentAsset = {}
        currentAsset["name"] = asset_name
        currentAsset ["value"] = round(amount*float(current_value),2)
        data.append(currentAsset)
    
    print(data, "DAAAATAAAAA")
    returnDict = {}
    returnDict["data"] = data
    return JsonResponse(returnDict, safe=False)


@api_view(['POST'])           
def create_portfolio(request):
    print("POST METHOD WORKS - create token")
    name = request.data.get('name') 
    usertoken = request.data.get('token')
    create_port(name,usertoken)
    return JsonResponse({}, status=201)


@api_view(['GET'])
def all_symbols(request):
    print("GET METHOD WORKS - in all symbols")
    symbols = allSymbols()
    print(symbols)
    ret = {}
    ret['data'] = symbols
    print("insdie all symbols:\n",ret)
    return JsonResponse(ret, status=201)


@api_view(['GET'])
def get_symbols_of_portfolio(request):
    print("inside get_symbols_of_portfolio")
    token = request.data.get('Authorization') 
    portfolio_id = request.headers.get('Portfolio')

    symbols = symbols_in_portfolio(token, portfolio_id)

    ret = {}
    print(symbols[0], "this is the first")
    if symbols[0] == 'database':
        ret['name'] = symbols[1:]   
    else:
        ret['name'] = symbols 

    print("here is all the symbols in the selected portfolio: ", ret)
    return JsonResponse(ret, status=201)

@api_view(['POST'])   
def add_to_portfolio(request):
    token = request.data.get('Token') 
    portfolio_id = request.data.get('PortfolioId')
    symbol = request.data.get('symbol')
    amount = request.data.get('amount')

    amount_float = float(amount)
    print("-------------------------------------")
    print(amount_float)

    # print("----------------inside add_to_portfolio-------------------")
    # print("token: "+ token+ "\nportfolio_id"+ portfolio_id)
    # print("symbol: "+ symbol+ "\namount: "+ amount)
    # print("----------------inside add_to_portfolio-------------------")

    current_datetime = datetime.now()
    current_datetime_formatted = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(current_datetime_formatted)

    result = add_asset(token, portfolio_id, symbol, amount_float, current_datetime_formatted)

    return JsonResponse({}, status=201) 

@api_view(['POST'])  
def increase_in_portfolio(request):
    token = request.data.get('Token') 
    portfolio_id = request.data.get('PortfolioId')
    symbol = request.data.get('Symbol')
    amount = request.data.get('amount')

    amount_float = float(amount)
    print("-------------------------------------")
    print(amount_float)

    # print("----------------increase_in_portfolio-------------------")
    # print("token: ", token)
    # print("portfolio_id: ", portfolio_id)
    # print("amount: ", amount)
    # print("symbol: ", symbol)
    # print("----------------increase_in_portfolio-------------------")
    
    current_datetime = datetime.now()
    current_datetime_formatted = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(current_datetime_formatted)

    operation = 'increase'
    result = modify_amount(token, portfolio_id, amount_float, symbol, operation, current_datetime_formatted)

    return JsonResponse({}, status=201) 

@api_view(['POST'])  
def decrease_in_portfolio(request):
    token = request.data.get('Token') 
    portfolio_id = request.data.get('PortfolioId')
    symbol = request.data.get('Symbol')
    amount = request.data.get('amount')

    amount_float = float(amount)
    print("-------------------------------------")
    print(amount_float)

    # print("----------------decrease-in-portfolio-------------------")
    # print("token: ", token)
    # print("portfolio_id: ", portfolio_id)
    # print("amount: ", amount)
    # print("symbol: ", symbol)
    # print("----------------decrease-in-portfolio-------------------")

    current_datetime = datetime.now()
    current_datetime_formatted = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(current_datetime_formatted)

    operation = 'decrease'
    result = modify_amount(token, portfolio_id, amount_float, symbol, operation, current_datetime_formatted)

    return JsonResponse({}, status=201) 

@api_view(['GET','OPTIONS'])
def get_portfolio_names(request):
    print("inside get_portfolio_names")
    token = request.headers.get('Authorization') 
    id = get_id_with_token(token)
    get_portfolios = get_portfolio_ids_with_user_id(id)
    portfolio_names =[]
    for id in get_portfolios:
        portfolio_names.append(get_portfolio_name_with_portfolio_id(id))
    dict = {}
    dict['names'] = portfolio_names
    
    #ret['data'] = portfolio_names
    #print("insdie get_portfolio_names:\n",ret)
    
    return JsonResponse(dict, status=201)

@api_view(['GET','OPTIONS'])
def get_asset_names(request):
    print("inside get_asset_names")
    token = request.headers.get('Authorization')
    user_id = get_id_with_token(token)
    asset_ids = get_assets_with_user_id(user_id)
    asset_names = []
    for (name,value) in asset_ids:
        asset_names.append(name)
    dict = {}
    dict['names'] = asset_names


    return JsonResponse(dict, status=201)

@api_view(['GET','OPTIONS'])
def get_weekly_data_portfolio(request):
    print("--------------------------------------------------------")
    token = request.headers.get('Authorization')
    portfolio_name = request.headers.get('Portfolio')
    print("portfolio_name: ", portfolio_name)
    #portfolio_name = "agaOlArtıkBe"
    user_id = get_id_with_token(token)
    portfolio_id = get_portfolio_id_with_portfolio_name_and_user_id(portfolio_name, user_id)
    asset_values = get_total_value_week_in_portfolio(portfolio_id, 'week')
    print(asset_values)
    print("--------------------------------------------------------")
    retDict={}
    retDict['data'] = asset_values
    return JsonResponse(retDict, status=201)

@api_view(['GET','OPTIONS'])
def get_monthly_data_portfolio(request):
    print("--------------------------------------------------------")
    token = request.headers.get('Authorization')
    portfolio_name = request.headers.get('Portfolio')
    print("portfolio_name: ", portfolio_name)
    #portfolio_name = "agaOlArtıkBe"
    user_id = get_id_with_token(token)
    portfolio_id = get_portfolio_id_with_portfolio_name_and_user_id(portfolio_name, user_id)
    asset_values = get_total_value_week_in_portfolio(portfolio_id, 'month')
    print(asset_values)
    print("--------------------------------------------------------")
    retDict={}
    retDict['data'] = asset_values
    return JsonResponse(retDict, status=201)

@api_view(['GET','OPTIONS'])
def get_yearly_data_portfolio(request):
    print("--------------------------------------------------------")
    token = request.headers.get('Authorization')
    portfolio_name = request.headers.get('Portfolio')
    print("portfolio_name: ", portfolio_name)
    #portfolio_name = "agaOlArtıkBe"
    user_id = get_id_with_token(token)
    portfolio_id = get_portfolio_id_with_portfolio_name_and_user_id(portfolio_name, user_id)
    asset_values = get_total_value_week_in_portfolio(portfolio_id, 'year')
    print(asset_values)
    print("--------------------------------------------------------")
    retDict={}
    retDict['data'] = asset_values
    return JsonResponse(retDict, status=201)


from datetime import datetime, timedelta,date
# from dateutil.relativedelta import relativedelta

@api_view(['GET','OPTIONS'])
def get_weekly_data_asset(request):
    #print(request.headers)

    asset_name = request.headers.get('AssetName')
    # asset_name = "TSLA"
    asset_id = get_asset_id(asset_name)
    

    end_time = date.today()
    start_time = end_time - timedelta(days=6)

    asset_values = get_asset_values_week(start_time, end_time, asset_id)
    #print(asset_values,"YENİ HOP ALO ŞŞŞŞ")
    difference_in_days = 6
    result2 = []
    for i in range(difference_in_days+1):
        dateq = start_time + timedelta(days=i)
        result2.append({"name":dateq.strftime('%a'),"value":asset_values[i]})

    retDict = {}
    retDict["data"] = result2

    print(retDict)

    return JsonResponse(retDict, status=201)

@api_view(['GET','OPTIONS'])
def get_monthly_data_asset(request):
    #print(request.headers)

    asset_name = request.headers.get('AssetName')
    # asset_name = "TSLA"
    asset_id = get_asset_id(asset_name)
    

    end_time = date.today()
    start_time = end_time - timedelta(days=30)

    asset_values = get_asset_values_week(start_time, end_time, asset_id)
    #print(asset_values,"YENİ HOP ALO ŞŞŞŞ")
    difference_in_days = 30
    result2 = []
    for i in range(difference_in_days+1):
        dateq = start_time + timedelta(days=i)
        result2.append({"name":dateq.strftime('%d'),"value":asset_values[i]})

    retDict = {}
    retDict["data"] = result2

    print(retDict)

    return JsonResponse(retDict, status=201)

from dateutil.relativedelta import relativedelta

@api_view(['GET','OPTIONS'])
def get_yearly_data_asset(request):
    #print(request.headers)

    asset_name = request.headers.get('AssetName')
    # asset_name = "TSLA"
    asset_id = get_asset_id(asset_name)
    

    end_time = date.today()
    #start_time = end_time - timedelta(days=365)
    start_time = end_time - relativedelta(months=12)

    asset_values = get_asset_values_week(start_time, end_time, asset_id)
    #print(asset_values,"YENİ HOP ALO ŞŞŞŞ")
    difference_in_days = 11
    result2 = []
    for i in range(difference_in_days+1):
        dateq = start_time + relativedelta(months=i)
        current_date = dateq.strftime('%B')
        # print("--------------------------------->current_date: ", current_date)
        current_month = current_date[0]
        result2.append({"name":current_month,"value":asset_values[i]})

    retDict = {}
    retDict["data"] = result2

    print(retDict)

    return JsonResponse(retDict, status=201)






