import mysql.connector
from config_pass import *

#function used for creating database
def db():
    mydb = mysql.connector.connect(host="localhost", user=str(username), passwd=str(sql_password))
    cursor = mydb.cursor()
    try:
        cursor.execute("Create database details")
        cursor.execute("Use details")
        cursor.execute(
        "Create table Office(vis_name varchar(255 ),vis_mail varchar(255),vis_mob varchar(255),"
        "check_in TIMESTAMP DEFAULT CURRENT_TIMESTAMP,check_out TIMESTAMP,"
        "host_name varchar(255),host_mail varchar(255),host_mob varchar(255))")
    except:
        cursor.execute("Use details")