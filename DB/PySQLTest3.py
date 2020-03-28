import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  auth_plugin='mysql_native_password',
  database='project'
)

print(mydb)

mycursor = mydb.cursor()

with open('countries of the world.csv', mode='r') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[3] for rows in reader}

print(mydict)

for i in mydict.items():
    word = i[0]
    count = i[1]
    sql = "INSERT INTO project (word, count) VALUES (%s, %s)"
    val = (word,count)
    mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
