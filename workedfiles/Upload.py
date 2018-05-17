import os,csv
from flask import Flask, request, redirect, url_for, send_from_directory,render_template
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['csv','xlsx'])

mysql_host='localhost'
mysql_user='root'
mysql_pw='jaga9538'
mysql_db='flaskapp'

app = Flask(__name__)
#db=yaml.load(open('db.yaml'))

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='jaga9538'
app.config['MYSQL_DATABASE_DB'] = 'flaskapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql = MySQL()
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
a='59,Fri Jun 30 19:34:54 CEST 2017,gdc1pbkpapp002,ebsmeypdc007.d1.ad.local,GDC1-BKP-Test,full-weekly'
li=[]
li=a.split(',')

cursor.execute('INSERT INTO backup(status,Fdate,mserver,bserver,policy,btype) VALUES(%d,%s,%s,%s,%s,%s)'(int(li[0]),li[1],li[2],li[3],li[4],li[5]))
conn.commit()
#cur.close()
cursor.close()
conn.close()
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        print(file)
        #fs=file.read()
        lisline=[]
        for line in file:
            print(line)
            lisline.append(line)

        #print(fs)
        file.seek(0)
        print(len(lisline))
        print(file.filename)
        #ith open('abc.txt','w')
#        print(file.read())
#        file.seek(0)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print('\n'+'its redrintng')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #abc.readera(file)
            print('\n'+'its redrintng')

            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('uploadform.html')



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return '''successfully upladed '''


if __name__ == "__main__":
    app.run(debug=True)
