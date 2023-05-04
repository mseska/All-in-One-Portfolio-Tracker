from django.db import connection

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

def get_portfolios_with_user_id(id):
    # portfolios = my_custom_sql("SELECT asset_information.name,asset_information.current_value,user_asset_ownership.portfolio_id,user_asset_ownership.asset_id,user_asset_ownership.amount FROM comp491.user_asset_ownership,comp491.asset_information WHERE user_asset_ownership.asset_id = asset_information.asset_id and user_asset_ownership.user_id={};".format(id),connection)
    portfolios = my_custom_sql("SELECT asset_information.name, asset_information.current_value, user_asset_ownership.portfolio_id, user_asset_ownership.asset_id, user_asset_ownership.amount, portfolio.name FROM comp491.user_asset_ownership, comp491.asset_information,  comp491.portfolio WHERE user_asset_ownership.asset_id = asset_information.asset_id and user_asset_ownership.user_id={};".format(id),connection)
    return(portfolios)
