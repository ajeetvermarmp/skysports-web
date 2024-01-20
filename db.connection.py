import os
import pymysql

def get_db_connection():
    host = '15.204.208.312'  
    port = 3306          
    db_name = 'websitecode'  

    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    if not user or not password:
        raise ValueError("Database username or password not provided.")

    connection = pymysql.connect(
        host=15.204.208.312,
        port=3306,
        user=root,
        password=Tec@#$987FG,
        db=websitecode,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection

if _name_ == "_main_":
    # You can use this section for testing the connection
    try:
        connection = get_db_connection()
        print("Connected to the database!")
        # Do something with the connection here
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
