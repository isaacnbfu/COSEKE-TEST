import os

import mysql.connector as database  #the mysql connector  

username = os.environ.get("root") #these have already been exported as env variables
password = os.environ.get("5555")

#these are the details to get us into the database
connection = database.connect(
    user="root",
    password="5555",
    host="localhost",
    database="userinfo"
)

#the cursor object is the one that retrieves and also updates data into the databse
cursor = connection.cursor()

#now add the databse entries into the database
#we start with the method for adding data into the database userinfo
def add_data(firstName, lastName, age):
    try:
        statement = "INSERT INTO userinfo (firstName, lastName, age) VALUES (%s, %s, %s)"
        data = (firstName, lastName, age)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entries into database")
    except database.Error as e:
        print("Error adding entry into databasr")
        
        
#next a method for retrieving the data
def get_data(first_Name, last_Name, Age):
    try:
        statement = "SELECT first_Name, last_Name, Age FROM userinfo"
        data = (first_Name, last_Name, Age)
        cursor.execute(statement, data)
        for (first_Name, last_Name, Age) in cursor:
            print("Successfully retrieved {first_Name}, {last_Name}, {Age}")
    except database.Error as e:
        print("Error retrieving entry database ")
        
        
add_data("Isaac", "Nambafu", "24")
get_data("Isaac", "Nambafu", "25")

connection.close()