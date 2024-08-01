import MySQLdb

class Category():
    def __init__():
        pass

    # Step1 建立連線
    def create_connection():
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

    # 讀取所有資料
    def category_all():
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

    # 讀取單筆資料
    def category_single(id):
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

    # 新增資料
    def category_create(category_name):
        connection = Category.create_connection()
        if not connection:
            return None

        # step2 SQL INSERT
        sql = 'INSERT INTO category (name) VALUES (%s)'

        # step3 cursor 執行 SQL
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql,(category_name,))
                    # step 3-2
                    connection.commit()
                    return cursor.rowcount
                except MySQLdb.MySQLError as e:
                    print(f"資料新增失敗：{ e }")
                    return None
                
    # 修改資料
    def category_upodate(id, category_name):
        connection = Category.create_connection()
        if not connection:
            return None

        # step2 SQL update
        sql = "UPDATE category SET name=%s WHERE category_id=%s"

        # step3 cursor 執行 SQL
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql,(category_name,id)) # tutple (id, )
                    # step 3-2
                    connection.commit()
                    return cursor.rowcount
                except MySQLdb.MySQLError as e:
                    print(f"資料修改失敗：{ e }")
                    return None
                # 已用 with 就不用再寫此段
                # finally:
                #     connection.close()
    

    # 刪除資料
    def category_delete(id):
        connection = Category.create_connection()
        if not connection:
            return None

        # step2 SQL delete
        sql = "DELETE FROM category WHERE category_id=%s "

        # step3 cursor 執行 SQL
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql,(id, )) # tutple (id, )
                    # step 3-2
                    connection.commit()
                    return cursor.rowcount
                except MySQLdb.MySQLError as e:
                    print(f"資料刪除失敗：{ e }")
                    return None
