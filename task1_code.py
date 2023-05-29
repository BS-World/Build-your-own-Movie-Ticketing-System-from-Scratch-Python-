import re
from settings import mysql_connection


## write a function to check if a number has string or  not
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
 
# write a function for for validating an Email
def check_email(email):
    pattern = r"^.+@.+\.(com)$"
    # pass the regular expression
    # and the string into the fullmatch() method
    
    #return Boolean Value
    if  re.match(pattern,email):
        return "Invalid email"
        


## form to validate
def register(registration_form): 
    name =registration_form['name']
    email =registration_form['email']
    username=registration_form['username']
    date =registration_form['dob']
    password =registration_form['password']
    #your input from your input string (assume from front end , json)
    if len(name)<=3 or has_numbers(name):
        return "the name should have a minimum length of 4 characters and must not contain any digits."
    if len(username) < 5:
        return "the username must have a minimum length of 5 characters."
    if len(password) < 8 or not has_numbers(password):
        return "password should be greater than 8 digits and must have numbers."
    #name lenth should be greater than 3 and should not have any digits
    if not check_email(email):
        return "Invalid email."
    ## check email validation here 
    return True
    ## password should be greater than 8 digits and must have numbers, reuse has_number function
    
    ## after validation insert into database
    ## create connection
    
    
def capture_data(registration_form):
    ## if registration is valid
    data = register(registration_form)
    if data == True:
        
        name = registration_form['name']
        email = registration_form['email']
        username = registration_form['username']
        date = registration_form['dob']
        password = registration_form['password']
        
        ## connect with database
        mydb = mysql_connection()
        ## returns cursor
        sql = mydb.cursor()
        
        ## check if username already in database, use 'where' clause
        sql.execute(f"select * from my_users where username='{username}'")
        existing_user =sql.fetchone()
        if existing_user:
            return "username already taken, try another username."
        ## if 
        sql.execute(f"insert into my_users (name,email,username,date,password)values('{name}','{email}','{username}','{date}','{password}')")
        mydb.commit()
        mydb.close()
        return 'registration successful'
        #if username not taken create a new record, insert values into table
    else:
        return data
    

#do not delete following function
def task_runner():
    ## Test data
    name ='test_data'
    user_name = 'testusername'
    email_value = 'testgmail.com'
    date_value = '15-12-1999'
    password_value = 'testdfs77ds'
    registration_form = {'name' : name,  'username' :user_name, 'email': email_value, 'dob' : date_value, 'password': password_value}
    print(capture_data(registration_form))

task_runner()
