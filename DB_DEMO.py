import MySQLdb

class Category():
    def __init__():
        pass

    def create_connection():
        # Step1 建立連線
        try:
            connection = MySQLdb.connect(
                host = "localhost",
                database = "sakila",
                user = "root",                    password = "P@ssw0rd"
            )
            return connection
        except MySQLdb.MySQLError as e :
            print(f"資料庫連線錯誤: {e}")
            return None


    def all():
        # 其他程式 如爬蟲程式

        connection = Category.create_connection()
        if not connection:
            return None
        
        # Step2 SQL語法
        sql = "select * from category"

        # Step3 建立cursor物件執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    # Step3-1
                    results = cursor.fetchall()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯誤: {e}")
                    return None


    def single(id):
        # 其他程式 如爬蟲程式

        # Step1 建立連線
        # connection = MySQLdb.connect(
        #     host = "localhost",
        #     database = "sakila",
        #     user = "root",
        #     password = "P@ssw0rd"
        # )
        connection = Category.create_connection()
        if not connection:
            return None
        
        # Step2 SQL語法
        sql = "select * from category where category_id=%s"

        # Step3 建立cursor物件執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql,(id,))
                    # Step3-1
                    results = cursor.fetchone()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯誤: {e}")
                    return None
