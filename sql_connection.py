class sql_connection:
    def __init__(self,DRIVER_NAME,SERVER_NAME,DATABASE_NAME):
        self.driver = DRIVER_NAME
        self.server = SERVER_NAME
        self.database = DATABASE_NAME

    def connection(self):
        import pypyodbc as odbc
        connection_string = f"""
        DRIVER={{{self.driver}}};
        SERVER={self.server};
        DATABASE={self.database};
        Trust_Connection=yes;
        """
        conn=odbc.connect(connection_string)
        return conn


#import pypyodbc as odbc
#DRIVER_NAME = 'SQL SERVER'
#SERVER_NAME ='DRANZER'
#DATABASE_NAME ='credee'
