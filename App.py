from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'flask_contacts'

mysql = MySQL(app)

@app.route('/')
def Index():
  return 'Hello World'

@app.route('/add_contact')
def add_contact():
  return 'add_contact'

@app.route('/edit')
def edit():
  return 'edit'

if __name__ == '__main__':
  app.run(port = 3000, debug = True)
