from flask import Flask, render_template, request, redirect,  url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'contacts_db'
mysql = MySQL(app)

# Settings
app.secret_key = 'mySecretKey'

@app.route('/')
def Index():
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contact')
  data = cur.fetchall()
  return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO contact (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
    mysql.connection.commit()
    flash('Contact Add successfully')
    return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contact WHERE id = {}'.format(id))
  data =  cur.fetchall()
  return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<string:id>', methods=['POST'])
def update_contact(id):
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur = mysql.connection.cursor()
    res = cur.execute("""
      UPDATE contact
      SET
      fullname=%s,
      phone=%s,
      email=%s
      WHERE id=%s""",(fullname, phone, email, id))
    mysql.connection.commit()
    flash('Contact updated sucessfully')
    return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
  cur = mysql.connection.cursor()
  res = cur.execute('DELETE FROM contact WHERE id ={}'.format(id))
  mysql.connection.commit()
  flash('Contact Removed Successfuly')
  return redirect(url_for('Index'))

if __name__ == '__main__':
  app.run(port = 3000, debug = True)
