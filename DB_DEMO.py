import MySQLdb

class Category():
    def __init__():
        pass

    # 建立連線
    def categories():
        connection = MySQLdb.connect(
            host = "localhost",
            database = "sakila",
            user = "root",
            password = "P@ssw0rd"
        )
        if not connection:
            return None
        
        return connection