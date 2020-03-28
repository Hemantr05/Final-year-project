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

thisdict = {
  "brand": 6,
  "model": 8,
  "year": 10
}
print(thisdict)

for i in thisdict.items():
    word = i[0]
    count = i[1]
    sql = "INSERT INTO project (word, count) VALUES (%s, %s)"
    val = (word,count)
    mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
