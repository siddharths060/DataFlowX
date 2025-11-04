import mysql.connector
from mysql.connector import Error

hostname = "ezydkr.h.filess.io"
database = "DataFlowX_silkgasfor"
username = "DataFlowX_silkgasfor"
password = "1acbfe105f7cc7e4796ae8558fa8fa39fb2b57da"
port = "61002"


try : 
  connection = mysql.connector.connect(host = hostname, database = database, user = username, password = password, port = port)
  if connection.is_connected():
    db_info = connection.get_server_info()
    print("Database is connected with MQSQL version : ", db_info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You are connected to database : ", record)

except Error as e:
  print("error while connecting to SQL: ", e)
finally: 
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MYSQL connection is closed")   