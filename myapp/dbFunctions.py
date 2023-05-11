from django.db import connection
import random

def my_custom_sql(query,connection):
    with connection.cursor() as cursor:
        cursor.execute(query)
        
        row = cursor.fetchall()

    return row

def my_custom_news_sql(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result

def get_id_with_token(token):
    id =  my_custom_sql("SELECT user_id FROM comp491.authtoken_token WHERE authtoken_token.key ='{}';".format(token),connection)
    return(id[0][0])

def get_user_asset_ids_with_user_id(id):
    userAssetIds = my_custom_sql("SELECT asset_id FROM comp491.user_asset_ownership WHERE user_asset_ownership.user_id ={};".format(id),connection)
    userAssetIds = [row[0] for row in userAssetIds]
    return(userAssetIds)

def get_asset_information_with_ids(user_asset_ids):
    Assets = my_custom_sql("SELECT * FROM comp491.asset_information WHERE asset_information.asset_id IN (" + ",".join(str(id) for id in user_asset_ids) + ")",connection)
    return(Assets)

def get_asset_name_with_asset_id(asset_id):
    assetName = my_custom_sql("SELECT name FROM comp491.asset_information WHERE asset_information.asset_id ={};".format(asset_id),connection)
    return(assetName[0][0])

def get_assets_with_user_id(id):
    userAssetIds = my_custom_sql("SELECT distinct(asset_information.name), asset_information.current_value FROM comp491.user_asset_ownership,comp491.asset_information WHERE user_asset_ownership.asset_id = asset_information.asset_id and user_id = {};".format(id),connection)
    return(userAssetIds)

def get_asset_value_with_asset_id(asset_id):
    assetName = my_custom_sql("SELECT current_value FROM comp491.asset_information WHERE asset_information.asset_id ={};".format(asset_id),connection)
    return(assetName[0][0])


def get_daily_change(asset_name,current_value):
    current_value = float(current_value)
    r=random.uniform(0,2)
    last_value = current_value/r  #Fuat aga sadece bunun değişmesi lazım, gerçek dünkü kapanış lazım bize 
    change = 100*(current_value/last_value -1)
    change = round(change,2)
    #print(current_value,last_value,change,"change",r,"r")
    return(change)

def get_portfolio_ids_with_user_id(id):
    portfolioIds = my_custom_sql("SELECT distinct(portfolio_id) FROM comp491.user_asset_ownership where user_id = {};".format(id),connection)
    portfolioIds = [row[0] for row in portfolioIds]
    return(portfolioIds)

def get_portfolio_name_with_portfolio_id(portfolio_id):
    portfolio_name = my_custom_sql("SELECT name FROM comp491.portfolio where id={};".format(portfolio_id),connection)
    return(portfolio_name[0][0])

def get_asset_ids_with_portfolio_id(portfolio_id):
    assetIds = my_custom_sql("SELECT distinct(asset_id) FROM comp491.user_asset_ownership where portfolio_id = {};".format(portfolio_id),connection)
    assetIds = [row[0] for row in assetIds]
    if 0 in assetIds:
        assetIds.remove(0)
    return(assetIds)

def get_total_amount_of_an_asset(asset_id,portfolio_id):
    totalAmount = my_custom_sql("SELECT sum(amount) FROM comp491.user_asset_ownership where asset_id={} and portfolio_id = {};".format(asset_id,portfolio_id),connection)
    return(totalAmount[0][0])

def create_port(portfolio_name,token):
    id = get_id_with_token(token)
    portfolio_id = my_custom_sql("SELECT max(id) FROM comp491.portfolio;",connection)
    portfolio_id = portfolio_id[0][0]
    portfolio_id = portfolio_id + 1
    my_custom_sql("INSERT INTO `comp491`.`portfolio` (`id`,`name`) VALUES ({},'{}');".format(portfolio_id,portfolio_name),connection)
    
    my_custom_sql("INSERT INTO `comp491`.`user_asset_ownership` (`user_asset_id`, `user_id`, `asset_id`, `purchase_date`, `amount`, `portfolio_id`) VALUES ('', '{}', '0', '2005-05-20 20:00:00', '0', '{}');".format(id,portfolio_id),connection)

def allSymbols():
    symbols = my_custom_sql("SELECT name FROM comp491.asset_information where asset_id>0;",connection)
    symbols = [row[0] for row in symbols]
    return(symbols)

def get_asset_id(symbol):
    asset_id = my_custom_sql("SELECT asset_id FROM comp491.asset_information WHERE comp491.asset_information.name='{}';".format(symbol),connection)
    asset_id_value = asset_id[0][0]
    return(asset_id_value)

def symbols_in_portfolio(token, portfolio_id):
    symbols = my_custom_sql("SELECT DISTINCT comp491.asset_information.name FROM comp491.asset_information INNER JOIN comp491.user_asset_ownership ON asset_information.asset_id = user_asset_ownership.asset_id WHERE user_asset_ownership.portfolio_id = {};".format(portfolio_id),connection)
    symbols = [row[0] for row in symbols]
    return(symbols)

def add_asset(token, portfolio_id, symbol, amount):
    #find asset_id of the given symbol:
    print("this is the symbol to be added", symbol)
    asset_id = get_asset_id(symbol)
    # my_custom_sql("SELECT asset_id FROM comp491.asset_information WHERE comp491.asset_information.name='{}';".format(symbol),connection)
    print(asset_id)
    #asset_id_value = asset_id[0][0]
    #print("--------------->this is the asset_id: ", asset_id_value)

    #find user_id corresponds to the given token:
    user_id = get_id_with_token(token)

    # user_id_value = user_id[0][0]
    print(user_id, "----------------here is the user id")

    user_asset_id = my_custom_sql("SELECT max(user_asset_id) FROM comp491.user_asset_ownership;",connection)
    print(user_asset_id) #((29,),)
    user_asset_id_value = user_asset_id[0][0]
    user_asset_id_value += 1

    print("AMOUNT: ", amount)
    print("this is the value", user_asset_id_value)
    result = my_custom_sql("INSERT INTO comp491.user_asset_ownership (user_asset_id, user_id, asset_id, purchase_date, amount, portfolio_id) VALUES ({}, {}, {},'2003-05-20 23:00:00',{}, {});".format(user_asset_id_value,user_id_value, asset_id_value, amount, portfolio_id),connection)
    

def increase_amount(token, portfolio_id, amount, symbol):
    #symbol='TSLA'
    asset_id= get_asset_id(symbol)
    #my_custom_sql("SELECT asset_id FROM comp491.asset_information WHERE comp491.asset_information.name='{}';".format(symbol),connection)
    print("------------------------------>here is thr asset_id: ",asset_id)
    # asset_id_value = asset_id[0][0]
    # print("asset id value inside dbFunctions: ", asset_id_value)
    user_id = get_id_with_token(token)

    #take current amount:
    # current_amount = my_custom_sql("SELECT amount FROM comp491.user_asset_ownership WHERE asset_id = {} AND user_id = {};".format(asset_id, user_id),connection)
    # current_amount_value = current_amount[0][0]

    update = my_custom_sql("UPDATE comp491.user_asset_ownership SET amount = {} WHERE user_id = {} AND asset_id={};".format(amount, user_id, asset_id),connection)

def decrease_amount(token, portfolio_id, amount, symbol):
    #symbol='TSLA'
    asset_id= get_asset_id(symbol)
    #my_custom_sql("SELECT asset_id FROM comp491.asset_information WHERE comp491.asset_information.name='{}';".format(symbol),connection)
    print("------------------------------>here is thr asset_id: ",asset_id)
    # asset_id_value = asset_id[0][0]
    # print("asset id value inside dbFunctions: ", asset_id_value)
    user_id = get_id_with_token(token)

    update = my_custom_sql("UPDATE comp491.user_asset_ownership SET amount = {} WHERE user_id = {} AND asset_id={};".format(amount, user_id, asset_id),connection)
