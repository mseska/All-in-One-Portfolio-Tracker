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
    userAssetIds = my_custom_sql("SELECT distinct(asset_information.name), asset_information.current_value FROM comp491.user_asset_ownership,comp491.asset_information WHERE user_asset_ownership.asset_id = asset_information.asset_id and asset_information.asset_id>0 and user_id = {};".format(id),connection)
    return(userAssetIds)

def get_asset_value_with_asset_id(asset_id):
    assetName = my_custom_sql("SELECT current_value FROM comp491.asset_information WHERE asset_information.asset_id ={};".format(asset_id),connection)
    return(assetName[0][0])

def get_portfolio_id_with_portfolio_name_and_user_id(portfolio_name,user_id):
    print(portfolio_name,user_id,"portfo denemeeeeeee hop alo şşşşş")
    portfolio_id = my_custom_sql("SELECT distinct(portfolio_id) FROM comp491.portfolio,comp491.user_asset_ownership where user_asset_ownership.portfolio_id = portfolio.id and portfolio.name = '{}' and user_asset_ownership.user_id = {};".format(portfolio_name,user_id),connection)
    print(portfolio_id,"portfo hataaaa")
    return(portfolio_id[0][0])

def get_daily_change(asset_name,current_value):
    current_value = float(current_value)

    r=random.uniform(0,2)
    #last_value = current_value/r  #Fuat aga sadece bunun değişmesi lazım, gerçek dünkü kapanış lazım bize


    query = "SELECT value FROM `comp491`.`asset_history` WHERE asset_name=%s AND DATE(date) = DATE(DATE_SUB(NOW(), INTERVAL %s DAY))  "
    query = "SELECT value FROM `comp491`.`asset_history` WHERE asset_name = %s AND DATE(date) < DATE(NOW()) ORDER BY DATE(date) DESC LIMIT 1;  "

    result = my_custom_news_sql(query, (asset_name))
    if len(result) == 0:
        last_value=current_value
    else:
        last_value = result[0][0]


    # print("last value:", last_value)
    # print("currrent: ", current_value)
    change = 100*((current_value/last_value)-1)
    # print("------------------------------", change)
    change = round(change,2)
    #print(current_value,last_value,change,"change",r,"r")
    # print("------------------------------", change)
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
    print(asset_id,"asset_id fonskiyonu")
    asset_id_value = asset_id[0][0]
    return(asset_id_value)

def get_user_asset_id():
    user_asset_id = my_custom_sql("SELECT max(user_asset_id) FROM comp491.user_asset_ownership;",connection)
    user_asset_id_value = user_asset_id[0][0]
    user_asset_id_value += 1
    return(user_asset_id_value)

def symbols_in_portfolio(token, portfolio_id):
    symbols = my_custom_sql("SELECT DISTINCT comp491.asset_information.name FROM comp491.asset_information INNER JOIN comp491.user_asset_ownership ON asset_information.asset_id = user_asset_ownership.asset_id WHERE user_asset_ownership.portfolio_id = {};".format(portfolio_id),connection)
    symbols = [row[0] for row in symbols]
    return(symbols)

def add_asset(token, portfolio_id, symbol, amount, current_date):
    #find asset_id of the given symbol:
    print("this is the symbol to be added", symbol)
    asset_id = get_asset_id(symbol)

    #find user_id corresponds to the given token:
    user_id = get_id_with_token(token)

    print(user_id, "----------------here is the user id")

    user_asset_id = get_user_asset_id()

    print("AMOUNT: ", amount)
    print("this is the value", user_asset_id)
    result = my_custom_sql("INSERT INTO comp491.user_asset_ownership (user_asset_id, user_id, asset_id, purchase_date, amount, portfolio_id) VALUES ({}, {}, {},'{}',{}, {});".format(user_asset_id, user_id, asset_id, current_date, amount, portfolio_id),connection)

def modify_amount(token, portfolio_id, amount, symbol, operation, current_date):
    asset_id= get_asset_id(symbol)
    user_id = get_id_with_token(token)
    user_asset_id = get_user_asset_id() 

    if operation == 'decrease':
        updated_amount = amount * -1
    else: 
        updated_amount = amount

    print("helloooo this amount should be negative", updated_amount)

    result = my_custom_sql("INSERT INTO comp491.user_asset_ownership (user_asset_id, user_id, asset_id, purchase_date, amount, portfolio_id) VALUES ({}, {}, {},'{}',{}, {});".format(user_asset_id,user_id, asset_id, current_date, updated_amount, portfolio_id),connection)

from datetime import datetime, timedelta,date
from dateutil.relativedelta import relativedelta

def get_asset_values_week_in_portfolio(portfolio_id, time_interval):
    dict = {}
    asset_list = get_asset_ids_with_portfolio_id(portfolio_id)

    end_time = date.today()
    if time_interval == 'week':
        start_time = end_time - timedelta(days=6)
        print("----------------------weekly timeline-------------------------")
    elif time_interval == 'month':
        start_time = end_time - timedelta(days=30)
        print("----------------------monthly timeline------------------------")
    else: 
        start_time = end_time - relativedelta(months=12)
        print(start_time)
        print("----------------------yearly timeline-------------------------")

    #print(start_time,end_time,asset_list, "fonksiyon içi argümanlar")
    for asset_id in asset_list:
        valueList = []
        asset_values = get_asset_values_week(start_time,end_time,asset_id)
        #print(asset_values, "fonksiyon içi asset_values")
        asset_amounts = get_asset_amounts_week(start_time,end_time,asset_id,portfolio_id, time_interval)
        # print(asset_amounts, "fonksiyon içi asset_amounts")
        #print(asset_values,asset_amounts,asset_id, "fonksiyon iç içi  değerler")
        # print("--------------------------------->", len(asset_amounts))
        # for i in range(len(asset_amounts)):
        #     valueList.append((asset_amounts[i][0].strftime('%a'),asset_values[i]*asset_amounts[i][1]))
        count=0
        months=[]
        # print("***************************************************************")
        for i in range(len(asset_amounts)):
            try:
                # print("-------------------------------------------->>>>>>>>>>",asset_amounts[i][0])
                if time_interval == 'week':
                    valueList.append((asset_amounts[i][0].strftime('%a'), asset_values[i] * asset_amounts[i][1]))
                elif time_interval == 'month':
                    #TODO:burda ayın gününe çeviriyor May 21 22 ... falan diye
                    valueList.append((asset_amounts[i][0].strftime('%d'), asset_values[i] * asset_amounts[i][1]))
                else:
                    #TODO: burda da month year string halinde yazıyor
                    count+=1
                    current_month = asset_amounts[i][0].strftime('%B')
                    if current_month in months:
                        print("this month exists in the list")
                    else: 
                        months.append(current_month)
                        # print("ilk harfi\t\t\t: ", current_month[0])
                        valueList.append((current_month[0], asset_values[i] * asset_amounts[i][1]))
            
            except IndexError:
                break
        # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", count)
        # print("\n\nHellooooooooooooo:\n", months)
        # print("***************************************************************")
        dict[asset_id] = valueList
        #print(dict, "fonksiyon içi dict")
    return dict

def get_total_value_week_in_portfolio(portfolio_id, time_interval):
    dict = get_asset_values_week_in_portfolio(portfolio_id, time_interval)
    keys = list(dict.keys())
    # print("keys-----------------------------------------------------------")
    # print(keys)
    # print("---------------------------------------------------------------")
    total_value_list = []
    if len(keys) != 0:
        print("this is the lenght of the for loop: ", len(dict[keys[0]]))
        
        for i in range(len(dict[keys[0]])):
            total_value = 0
            for key in keys:
                total_value += dict[key][i][1]
                # print("------------------------------>", dict[key][i][0])
            total_value_list.append({"name":dict[key][i][0],"value":total_value})
    else:
        if time_interval == 'week':
            total_value_list.append({"name":date.today().strftime('%a'),"value":0})
        elif time_interval == 'month':
            total_value_list.append({"name": date.today().strftime('%d'), "value": 0})
        else: 
            total_value_list.append({"name": date.today().strftime('%B'), "value": 0})

    # print("/////////////////////////////////////////////////////////////")
    # print(total_value_list)
    # print("/////////////////////////////////////////////////////////////")
    return total_value_list


def get_asset_values_week(start_date,end_date,asset_id):
    #get the name of the asset:
    asset_name =  my_custom_sql("SELECT name FROM comp491.asset_information WHERE asset_id = {};".format(asset_id),connection)
    name = asset_name[0][0]
    
    asset_values =  my_custom_sql("SELECT value FROM comp491.asset_history WHERE asset_name='{}' AND STR_TO_DATE(date, '%Y-%m-%d') >= STR_TO_DATE('{}', '%Y-%m-%d') AND STR_TO_DATE(date, '%Y-%m-%d %H:%i:%s') <= STR_TO_DATE('{}', '%Y-%m-%d %H:%i:%s');".format(name, start_date, end_date),connection)
    asset_values = [row[0] for row in asset_values]
    return(asset_values)

def get_asset_amounts_week(start_date,end_date,asset_id,portfolio_id, time_interval):
    time_difference = end_date - start_date
    difference_in_days = time_difference.days
    result2 = []
    if time_interval == 'year':
        difference_in_days = 11
    for i in range(difference_in_days+1):
        if time_interval == 'year':
            date = start_date + relativedelta(months=i)
            # print("---------------------------------------------------------->", date)
        else:
            date = start_date + timedelta(days=i)
        result2.append((date,0))
    
    initial_query = """SELECT
        DATE(ua.purchase_date) AS date,
        (
            SELECT SUM(ua2.amount)
            FROM user_asset_ownership AS ua2
            WHERE ua2.asset_id = a.asset_id
            AND ua2.portfolio_id = ua.portfolio_id
            AND DATE(ua2.purchase_date) <= DATE(ua.purchase_date)
        ) AS total_balance
    FROM
        user_asset_ownership AS ua
        JOIN asset_information AS a ON ua.asset_id = a.asset_id
    WHERE
        DATE(ua.purchase_date) <= %s
        AND a.asset_id = %s
        AND ua.portfolio_id = %s
        
    GROUP BY
        a.name,
        DATE(ua.purchase_date),
        ua.portfolio_id
    ORDER BY
        a.name,
        DATE(ua.purchase_date) DESC;
    """

    inital_value = my_custom_news_sql(initial_query,(start_date,asset_id,portfolio_id))
    print(asset_id)
    print(portfolio_id)
    print(inital_value, "inital_value")
    for i in range(difference_in_days+1):
        if inital_value !=():
            result2[i] = (result2[i][0],inital_value[0][1])
    query = """SELECT
        DATE(ua.purchase_date) AS date,
        (
            SELECT SUM(ua2.amount)
            FROM user_asset_ownership AS ua2
            WHERE ua2.asset_id = a.asset_id
            AND ua2.portfolio_id = ua.portfolio_id
            AND DATE(ua2.purchase_date) <= DATE(ua.purchase_date)
        ) AS total_balance
    FROM
        user_asset_ownership AS ua
        JOIN asset_information AS a ON ua.asset_id = a.asset_id
    WHERE

        DATE(ua.purchase_date) >= %s
        AND DATE(ua.purchase_date) <= %s
        AND a.asset_id = %s
        AND ua.portfolio_id = %s
    GROUP BY
        a.name,
        DATE(ua.purchase_date),
        ua.portfolio_id
    ORDER BY
        a.name,
        DATE(ua.purchase_date) ASC;
    """
    result = my_custom_news_sql(query, (start_date, end_date, asset_id, portfolio_id))
    for new_item in result:
        for initial in range(len(result2)):
            if new_item[0] <= result2[initial][0]:
                result2[initial] = (result2[initial][0],new_item[1])
    # ((datetime.date(2023, 5, 12), 1.0), (datetime.date(2023, 5, 20), 10.0))
    # şeşka aga sonuç böyle dönüyo,tarihten de bakabilirsin yok dersen kırp kullan böyle kolaylaştırabilir diye düşündüm ya da 1 0 0 0 0 0 0 10 gibi bi array istersen time a göre iterate edebiliriz

    return result2