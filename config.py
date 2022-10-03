from distutils.debug import DEBUG
import os
from re import S
import mysql.connector

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print('BASE_DIR:',BASE_DIR)

DEBUG=True

# username=os.getenv("DB_USERNAME","root")
# password=os.getenv("DB_PASSWORD","Pk_123456")
# host=os.getenv("DB_HOST","localhost")
# database=os.getenv("DB_NAME","CSV_file")

# SQLALCEMY_DATABASE_URI="mysql+pymysql://{}:{}@{}/{}".format(username, password, host, database)
# SQLALCEMY_TRACK_MODIFICATIONS =False
# print(SQLALCEMY_DATABASE_URI)

#DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pk_123456",
    database="csv_file",
)

mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

def sql_var(sql, value):
    mycursor.execute(sql,value)
    mydb.commit()