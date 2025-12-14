import mysql.connector


def create_database():    
   try: 
         # CONNECT TO MYSQL SERVER
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # CREATE DATABASE (NO SELECT / SHOW USED)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")
   except mysql.connector.Error as e:
       print(e)

   finally:
        # CLOSE CONNECTION
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
       