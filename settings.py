import mysql.connector


#Following function will create a mysql connection.
def mysql_connection():
    #Get your DB connection from "DataBase Info" Tab
    HOST = 'localhost'
    USERNAME = 'bd69a05c'
    PASSWORD = 'Cab#22se'
    DATABASE = 'bd69a05c'

    mydb = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )
    
    return mydb
