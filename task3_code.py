import re
from settings import mysql_connection


mydb = mysql_connection()
## create cursor
sql = mydb.cursor()
#select ticket and ids
def select_movie(movie_id, no_of_tickets):
    
    ##take movie id and no of tickets as inputs
    if no_of_tickets>5:
        print("Maximum 5 tickets allowed per person.")
        return False
    ## only 5 tickets for a person condition validation
    
    ##select movie_id and avaibility from the database
    sql.execute("select movie_id,availability from movies where movie_id=%s",(movie_id,))
    result=sql.fetchone()

    ##validate if a particular movie id is available
    if not result:
        print("movie not found.")
        return False
    ## Display how many tickets available
    movie_id,availability=result
    print(f"Available tickets for movie ID {movie_id}:{availability}")
    ## assume that payment gateway has processed (at the counter)

    #update the tickets dynamically into database (Change the type to int) (tickets available - ticket booked)
    try:
        updated_availability=int(availability)-no_of_tickets
    ## this is to maintain realistic records
    
    ## write update query, change from int to string record where movie_id = 'value'
        sql.execute("update movies set availability=%s where movie_id=%s",(str(updated_availability),movie_id))
        mydb.commit()
        return True
    except ValueError:
        print("Invalid availability count in the database.")
        return False
    #return True when success
    #default return should be False
    return False

    ##challenge since the ticket count is in varchar format in table, you have to dynamically convert type and validate


#do not delete following function
def task_runner():
    print(select_movie(1001, 2))
