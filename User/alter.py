
from sql_connection import sql_connection
from mongo_connection import mongoconnection

db = mongoconnection('localhost',27017,'CREDEE')
print (db)
conn = sql_connection('SQL SERVER','DRANZER','credee')
connection = conn.connection()

print(connection)

class user:
    def __init__(self) -> None:
        pass
    def card_addition(self):
        pass



