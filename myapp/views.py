from django.shortcuts import render
from django.http import HttpResponse
from .models import Assets, Product, Stock2
from django.db import connection
import json
from . serializer import ItemSerializer
from django.http import JsonResponse

from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

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
def get_stock_list(request):
    print("GET METHOD WORKS")
    print(request.GET)

    list = my_custom_sql("SELECT * FROM `comp491`.`asset_history`",connection)
    returnList = []
    # print(list,"databaseden gelen veri")
    
    for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[2]
        newAsset.price = stock[3]
        newAsset.currency = stock[1]
        # print(stock[1])
        # print(stock[2])
        # print(stock[3])
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.currency,"newAsset.currency")
        # print(newAsset,"newAsset")
        returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    # serializer = StockSerializer(data=returnList)
    # if serializer.is_valid():
    #     serializer.save()
    #     print(serializer.data)
    #returnListDict = {returnList}
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)
    

@api_view(['GET'])
def get_crypto_list(request):
    print("GET METHOD WORKS")
    print(request.GET)

    list = my_custom_sql("SELECT * FROM `comp491`.`asset_history`",connection) #table will be changed
  
    returnList = []
    # print(list,"databaseden gelen veri")
    
    for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[2]
        newAsset.price = stock[3]
        newAsset.currency = stock[1]
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.currency,"newAsset.currency")
        # print(newAsset,"newAsset")
        returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    # serializer = StockSerializer(data=returnList)
    # if serializer.is_valid():
    #     serializer.save()
    #     print(serializer.data)
    #returnListDict = {returnList}
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)
    

@api_view(['GET'])
def get_currency_list(request):
    print("GET METHOD WORKS")
    print(request.GET)

    list = my_custom_sql("SELECT * FROM `comp491`.`asset_history`",connection)
  
    returnList = []
    # print(list,"databaseden gelen veri")
    
    for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[2]
        newAsset.price = stock[3]
        newAsset.currency = stock[1]
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.currency,"newAsset.currency")
        # print(newAsset,"newAsset")
        returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    # serializer = StockSerializer(data=returnList)
    # if serializer.is_valid():
    #     serializer.save()
    #     print(serializer.data)
    #returnListDict = {returnList}
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)

@api_view(['GET'])
def get_commodity_list(request):
    print("GET METHOD WORKS")
    print(request.GET)

    list = my_custom_sql("SELECT * FROM `comp491`.`asset_history`",connection) 
  
    returnList = []
    # print(list,"databaseden gelen veri")
    
    for stock in list:
        #print(type(asset))
        newAsset = Stock2()
        # print(newAsset,"newAsset daha oluştu")
        newAsset.symbol = stock[2]
        newAsset.price = stock[3]
        newAsset.currency = stock[1]
        # print(newAsset.symbol,"newAsset.symbol")
        # print(newAsset.price,"newAsset.price")
        # print(newAsset.currency,"newAsset.currency")
        print(newAsset,"newAsset")
        returnList.append(newAsset)
    #print(returnList,"liste databaseden alındı")
    # serializer = StockSerializer(data=returnList)
    # if serializer.is_valid():
    #     serializer.save()
    #     print(serializer.data)
    #returnListDict = {returnList}
    serialized_objects = [obj.to_dict() for obj in returnList]  # Convert each object to a dictionary using a method 'to_dict'
    return JsonResponse(serialized_objects, safe=False)
    #return JsonResponse(json.dumps(returnListDict), safe=False)
    

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
        return JsonResponse({'token': token.key}, status = 200)
    else:
        print("user does not exist:(")
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

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
        return JsonResponse({'error': 'User with this email already exists'})

    #create a user:
    user = User.objects.create_user(username=email, password=password)
    user.save()

    #to check whether the user is empty or not:
    print(user.email)
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
        return JsonResponse({'token': token.key}, status=201)
    else:
        print("user is not created sorry")
        return JsonResponse({'error': 'Invalid credentials'}, status = 401)
