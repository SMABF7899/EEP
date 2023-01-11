from sshtunnel import SSHTunnelForwarder
import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()
IP_SERVER = os.getenv('IP_SERVER')
PASSWORD_SERVER = os.getenv('PASSWORD_SERVER')
PASSWORD_MYSQL = os.getenv('PASSWORD_MYSQL')

server = SSHTunnelForwarder((IP_SERVER, 22),
                            ssh_username='root',
                            ssh_password=PASSWORD_SERVER,
                            ssh_proxy_enabled=True,
                            remote_bind_address=('localhost', 3306))

server.start()
print("connect to server")

connection = pymysql.connect(host='localhost',
                             port=server.local_bind_port,
                             user='sh',
                             password=PASSWORD_MYSQL,
                             db='energy',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect to energy")

myCursor = connection.cursor()
T = int(input("Enter Temp : "))
myCursor.execute("SELECT V FROM `Compressed_Liquid_Water` WHERE T=" + str(T) + " AND Bar=25")
myResult = myCursor.fetchone()
print(myResult)
print("-----------------------------------------------------------------------------------------------------------")