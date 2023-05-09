import datetime

from django.shortcuts import render
from django.http import HttpResponse
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
    user_asset_ids =  get_user_asset_ids_with_user_id(id)
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
    #print(returnList,"liste databaseden alındı")
    
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
    update_news_data(tickersList)
    update_prices()

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
def update_prices():
    #tickers = ["TSLA", "GLD", "ASELS.IS", "ETH-USD", "CEEK-USD"]
    tickers =  [

  "GARAN.IS", "AKBNK.IS", "KCHOL.IS", "SISE.IS", "ULKER.IS",
  "ISCTR.IS", "TCELL.IS", "BIMAS.IS", "YKBNK.IS", "VAKBN.IS",


  "AAPL", "MSFT", "AMZN", "GOOGL", "FB",
  "BRK-B", "V", "JNJ", "WMT", "NVDA",


  "GLD", "SLV", "USO", "UNG", "DBC",
  "DBA", "DBB", "DBE", "DBP", "DBS",


  "BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "XRP-USD",
  "SOL1-USD", "DOT1-USD", "DOGE-USD", "LUNA1-USD", "AVAX-USD",


  "KO", "PEP", "MCD", "INTC", "DIS",
  "ENJSA.IS", "VESTL.IS", "ARCLK.IS", "CRFSA.IS", "TUPRS.IS"
]


    start_date = "2022-04-02"
    end_date = "2022-04-04"

    url = f"https://query1.finance.yahoo.com/v7/finance/chart/{{}}?range=1d&interval=1d&indicators=quote&includeTimestamps=true"

    data_dict = {}

    # Loop through the tickers and retrieve data from Yahoo Finance API
    for ticker in tickers:
        current_url = url.format(ticker)

        response = requests.get(current_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})

        data = response.json()

        # Extract the data for the specified date range
        timestamps = data["chart"]["result"][0]["timestamp"]
        prices = data["chart"]["result"][0]["indicators"]["quote"][0]
        data_dict[ticker] = {"Timestamp": timestamps, "Open": prices["open"], "High": prices["high"],
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
        asset = ticker

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

    print("dbupdated\n\n\n\n")

    pass



def update_news_periodically():
    while True:
        now = datetime.datetime.now()
        if now.second == 0 and now.minute== 0:  # Run update_news_data() once per hour at the start of the hour
            tickersList = ["TSLA", "GLD", "ASELS.IS", "ETH-USD","BTC-USD"]
            update_news_data(tickersList)
        time.sleep(1)



def update_prices_periodically():
    while True:
        now = datetime.datetime.now()
        if now.second == 0 and now.minute == 0:  # Run update_news_data() once per hour at the start of the hour
            update_prices()
        time.sleep(1)


@api_view(['GET'])
def news_api(request):
    with open('news_data.json') as f:
        data = json.load(f)
    #print(data)
    return JsonResponse(data, safe=False)


@api_view(['POST'])           
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
    #User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        print("email confirmed!")
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('http://localhost:3000') #TODO
        #return JsonResponse({'token': token.key}, status=201)
    else:
        print("sorry could not confirmed the email")
        messages.error(request, 'Activation link is invalid!')


def send_verification_email(request, user, name):
    print("activating the email confirmation...") 

    mail_subject = 'Activate Your Account'
    print(user.username, "this is the username to be printed to the email")
    message = render_to_string('template_activate_account.html', {
        'user': name, 
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
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
    user.first_name = name
    user.last_name = surname
    user.save()

    #to check whether the user is empty or not:
    print(user.email, "hello")
    print(user.password)

    user = authenticate(request, username=email, password=password)

    print(user, "after authenticate")

    # print(user.email, "After authenticate()")
    # print(user.password)
   
    if user is not None:
        print("user created")
        #login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        #activate(request, uidb64, token)
        # verification_mail = send_verification_email(request, user, name)
        # if verification_mail.send():
            # messages.success(request, f'Dear <b>{name}</b>, please go to you email <b>{email}</b> inbox and click on \
            # received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
        print("email sent değil!!!!!!!")
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
    get_portfolios = get_portfolios_with_user_id(id)
    print(get_portfolios)
    returnList = []
    # print(list,"databaseden gelen veri")
    
    #Bunu uncomment etmeden önce databasein düzenlenmesi lazım. 
    # 1-auth_user artık user information tutucu ona göre foreign keyler tutulmalı
    # 2-user information, asset information ve asset_user_ownership birbiriyle uyumlu veri içermeli
    for stock in get_portfolios:
    #for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[0]
        newAsset.price = stock[1]*stock[4]
        newAsset.change = "deneme"
        print(stock[1])
        print(stock[2])
        print(stock[3])
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.change,"newAsset.change")
        # print(newAsset,"newAsset")
        returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    print(serialized_objects, "serialized")
    return JsonResponse(serialized_objects, safe=False)







