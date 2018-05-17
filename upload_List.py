import os,csv,re
from flask import Flask, request, redirect, url_for, send_from_directory,render_template
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
#import linear_regrestion as lr
import s_l_r as slr
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['csv','xlsx'])

mysql_host='localhost'
mysql_user='root'
mysql_pw='jaga9538'
mysql_db='flaskapp'

app = Flask(__name__)
#db=yaml.load(open('db.yaml'))


app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql = MySQL()
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()



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
            line1=re.sub(r'b\'(.*)\\r\\n',r'\1',str(line))
            #print(line1)
            line_list=[]
            line_list=line1.split(',')
            line_list[1]=int(line_list[1].replace('\'',''))
            line_list[0]=int(line_list[0])
            lisline.append(line_list)
            li=a.split(',')
            cursor.execute('INSERT INTO dataset(data1,data2) VALUES(%d,%s)'(int(line_list[0]),line_list[1]))


        #print(fs)
        print(lisline)
        file.seek(0)
        print(len(lisline))
        print(file.filename)
        lisline=cursor.execute('select * from dataset')
        r_error,b0,b1 = slr.evaluate_slope_constant(lisline)
        print('RMSE: %.3f,%d,%d' % (r_error,int(b0),int(b1)))

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
            msg={"filename":filename,"r_error":r_error,"b0":b0,"b1":b1}

            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('uploaded_file',filename=filename,
                                    r_error=r_error,b0=b0,b1=b1))
    return render_template('uploadform.html')


#print(str(slr.B0)+' cap  '+str(slr.B1))
@app.route('/uploads/<filename>/<r_error>/<b0>/<b1>')
def uploaded_file(filename,r_error,b0,b1):
    #print(r)
    print(r_error)
    print(b0)
    print(b1)
    return render_template('add.html', obj =[r_error,b0,b1],b0=b0,b1=b1,r_error=r_error )


if __name__ == "__main__":
    app.run(debug=True)
