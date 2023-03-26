from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
from django.db import connection
import json
 


# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hey, Welcome</h1>')
    name = 'Mert'
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.description = 'Our service is fast'
    return render(request,'a.html',{'feature':feature1,'name':name})

def input(request):
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

    my_custom_sql("INSERT INTO `comp491`.`asset_history` (`keysforassets`, `currency`, `asset_name`) VALUES ('"+inputGet+"', '"+currency+"', '"+symbol+"')",connection)
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