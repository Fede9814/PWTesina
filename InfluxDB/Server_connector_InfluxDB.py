# import influxdb in py file
from influxdb import InfluxDBClient

#Connection string
dbClient = InfluxDBClient(host='localhost', port=8086, username='root', password='root')

#Create DB Main (Testing purpose)
Main_DB = dbClient.create_database('Main')
main_DB = 'Main'

#Get the list of databases
listDB = dbClient.get_list_database()

#Get the list of users
listUsers = dbClient.get_list_users()

#Print the list for fun
print(listDB)
print(listUsers)
print("\n")

#Logic for user and DB check.

#Do you have a user? NO! Then create one!
if len(listUsers) == 0:
    print("There is no user yet, create one"),
    Question = "Create a new user with Administrator Privileges?"
    reply = str(input(Question + ' (y/n): ')).lower().strip()
    if reply[0] == "y":
        #New user is Admin user!
        Username = input()
        Password = input()
        Username_quoted = "'" + Username + "'"
        Password_quoted = "'" + Password + "'"
        dbClient.create_user(Username_quoted, Password_quoted, admin=True),
        #Do you have a Db available (apart from _internal?) NO! Then create one!
        if len(listDB) <= 1:
            print("There is no DB yet, create one"),
            db_name = input("Insert db name: "),
            dbClient.create_database(db_name),
            dbClient.switch_database(db_name) 
    if reply[0] == "n":
        #New user is Basic user!
        Username = input()
        Password = input()
        Username_quoted = "'" + Username + "'"
        Password_quoted = "'" + Password + "'"
        dbClient.create_user(Username_quoted, Password_quoted, admin=False),
        #Do you have a Db available (apart from _internal?) NO! Then create one!
        if len(listDB) <= 1:
            print("There is no DB yet, create one"),
            db_name = input("Insert db name: "),
            dbClient.create_database(db_name),
            dbClient.switch_database(db_name)
        else:
        #Do you have a Db available (apart from _internal?) YES! Then login to main_DB!
            dbClient.switch_database(main_DB)

#Do you have a user? YES! Login as Admin or create a new one?
if len(listUsers) != 0:
    Question = "Login with Admin(a) privileges or create a new(n) user?"
    reply = str(input(Question +' (admin/new): ')).lower().strip()
    #Login as Admin and switch to main_DB
    if reply[0] == "a":
        dbClient = InfluxDBClient('localhost', 8086, username='root', password='root')
        #Do you have a Db available (apart from _internal?) NO! Then create one!
        if len(listDB) <= 1:
            print("There is no DB yet, create one"),
            db_name = input("Insert db name: "),
            dbClient.create_database(db_name),
            dbClient.switch_database(db_name)
        else:
        #Do you have a Db available (apart from _internal?) YES! Then login to main_DB!
            dbClient.switch_database(main_DB)
    #Create a new user as above (same logic as first block)
    if reply[0] == "n":
        Question = "Create a new user with Administrator Privileges?"
        reply = str(input(Question + ' (y/n): ')).lower().strip()
        if reply[0] == "y":
            Username = input()
            Password = input()
            Username_quoted = "'" + Username + "'"
            Password_quoted = "'" + Password + "'"
            dbClient.create_user(Username_quoted, Password_quoted, admin=True),
            if len(listDB) <= 1:
                print("There is no DB yet, create one"),
                db_name = input("Insert db name: "),
                dbClient.create_database(db_name),
                dbClient.switch_database(db_name)
            else:
                dbClient.switch_database(main_DB)
        if reply[0] == "n":
            Username = input()
            Password = input()
            Username_quoted = "'" + Username + "'"
            Password_quoted = "'" + Password + "'"
            dbClient.create_user(Username_quoted, Password_quoted, admin=False),
            if len(listDB) <= 1:
                print("There is no DB yet, create one"),
                db_name = input("Insert db name: "),
                dbClient.create_database(db_name),
                dbClient.switch_database(db_name)
            else:
                dbClient.switch_database(main_DB)

#Trial code to test the _internal InfluxDB database. Works just fine...in another .py file tho .-.
get = dbClient.query(("""SELECT * FROM cpu"""))
cpu_points = list(get.get_points(measurement='cpu'))
print(cpu_points, get)