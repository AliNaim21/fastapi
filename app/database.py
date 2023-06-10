from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#import mysql.connector
#import time

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
 
"""        
while True: 
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='fastapi',
                                             user='root',
                                             password='NFWJRZNrMo$')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            break

    except Error as e:
        print("Error while connecting to MySQL", e)
        time.sleep(2)
"""

