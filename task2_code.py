import re
from settings import mysql_connection

##REference link for mysql with python (for students)
#https://www.w3schools.com/python/python_mysql_getstarted.asp



mydb = mysql_connection()
## create cursor
sql = mydb.cursor()

#Task 2
def display_shows():
    
    ##dynamically fetch shows from movie table and display
    #the name of the table is movies
    #use sql to fetch shows by selecting movie_name, show_time, date
    return_dict= {}
    my_list = []
    sql.execute("select movie_id,movie_name,show_time,date from movies")
    rows=sql.fetchall()
    sql.close()
    mydb.close()
    
    try:
        for row in rows:
            movie_id,movie_name,show_time,date=row
            show = {
                "movie_id":str(movie_id),
                "movie":movie_name,
                "show_time":show_time,
                "date":date
            }
            my_list.append(show)
            return_dict['show']=my_list
    except mysql.connector.Error as error:
        print("Error while fatching movie show",error)
    ##write your code here
    
    return_dict['show'] = my_list
    #result list of dict with keys  'movie_id', 'movie', 'show_time', 'date'
    return  return_dict
 
#verify the return string


#do not delete following function
def task_runner():
    print(str(display_shows()))
