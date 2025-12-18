import mysql.connector

class User:
    @staticmethod
    def get_connection():
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbo_uas",
                connection_timeout=3
            )
            return mydb
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            return None

    @classmethod
    def user_login(cls, username, password):
        mydb = cls.get_connection()
        if not mydb:
            print("Tidak bisa konek DB")
            return None
        
        try:
            # dictionary=True supaya result['level'] bisa dibaca
            cursor = mydb.cursor(dictionary=True)

            # Pastikan kolom sesuai dengan tabel kamu!
            sql = """
                SELECT username, password, level 
                FROM user 
                WHERE username=%s AND password=%s
            """
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()

            print("DEBUG RESULT LOGIN =", result)  # Untuk cek hasil SEBENARNYA

            if result:
                return result["level"]  # return level
            return None

        except mysql.connector.Error as err:
            print("Error:", err)
            return None
        finally:
            if mydb:
                mydb.close()

    @classmethod
    def insert_user(cls, nama, username, password, level):
        mydb = cls.get_connection()
        if not mydb:
            return False
        try:
            cursor = mydb.cursor()
            sql = "INSERT INTO user (nama_lengkap, username, password, level) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nama, username, password, level))
            mydb.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
        finally:
            if mydb:
                mydb.close()

    @classmethod
    def read_users(cls):
        mydb = cls.get_connection()
        if not mydb:
            return []
        try:
            cursor = mydb.cursor(dictionary=True)
            sql = "SELECT * FROM user"
            cursor.execute(sql)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error:", err)
            return []
        finally:
            if mydb:
                mydb.close()

    @classmethod
    def get_user_by_username(cls, username):
        mydb = cls.get_connection()
        if not mydb:
            return None
        try:
            cursor = mydb.cursor(dictionary=True)
            sql = "SELECT username, password, level FROM user WHERE username=%s"
            cursor.execute(sql, (username,))
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print("Error:", err)
            return None
        finally:
            if mydb:
                mydb.close()

    @classmethod
    def update_user(cls, old_username, username=None, password=None, level=None):
        mydb = cls.get_connection()
        if not mydb:
            return False
        try:
            cursor = mydb.cursor()
            fields = []
            values = []

            if username:
                fields.append("username=%s")
                values.append(username)
            if password:
                fields.append("password=%s")
                values.append(password)
            if level:
                fields.append("level=%s")
                values.append(level)

            if not fields:
                return False

            values.append(old_username)
            sql = f"UPDATE user SET {', '.join(fields)} WHERE username=%s"
            cursor.execute(sql, tuple(values))
            mydb.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
        finally:
            if mydb:
                mydb.close()

    @classmethod
    def delete_user(cls, username):
        mydb = cls.get_connection()
        if not mydb:
            return False
        try:
            cursor = mydb.cursor()
            sql = "DELETE FROM user WHERE username=%s"
            cursor.execute(sql, (username,))
            mydb.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
        finally:
            if mydb:
                mydb.close()
