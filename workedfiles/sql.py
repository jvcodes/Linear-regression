a='59,Fri Jun 30 19:34:54 CEST 2017,gdc1pbkpapp002,ebsmeypdc007.d1.ad.local,GDC1-BKP-Test,full-weekly'
li=[]
li=a.split(',')

from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jaga9538'
app.config['MYSQL_DATABASE_DB'] = 'flaskapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()
line_list=[2,4]
cursor.execute("INSERT INTO dataset(data1,data2) VALUES(%s,%s)",(int(line_list[0]),int(line_list[1])))
cursor.execute("SELECT * from dataset")
data = cursor.fetchall()

print(data)
data1=[]

for i in data:
    data1.append(list(i))

print(data1)
