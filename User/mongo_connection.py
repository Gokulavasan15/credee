 
class mongoconnection:
    def __init__(self,ip,portno,db):
        self.ip=ip
        self.portno=portno
        self.db=db
    def database(self):
        from pymongo import MongoClient
        client = MongoClient(self.ip,self.portno)
        db = client[self.db]
        return db

