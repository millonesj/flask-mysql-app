# flask-mysql-app

![app's screenshot](https://repository-images.githubusercontent.com/208533999/f41d0300-dc05-11e9-87e8-31c7fb0725d3)

First, create your enviroment:
```ssh
$ python3 -m venv .env
```
activate it:
```sh
source .env/bin/activate
```

Create your instance mysql's docker with:
```sh
$ docker run --name mysql-for-flask-mysql-app -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -v ~/workspace/docker-volumes/flask-mysql-db:/var/lib/mysql -d  mysql:8.0
```
Connect to mysql container and run commands:
```sh
$ docker exec -it mysql-for-flask-mysql-app sh
# mysql -u root -p 123456
```
Create database:
```sh
mysql> create database contacts_db;
```
Create table:
```sh
mysql> create table contact (id int primary key not null  auto_increment, fullname varchar(255) not null, phone varchar(12) null, email varchar(255) null);
```
Install the next dependencies:
```sh
$ pip install flask
$ pip install mysql-connector
$ pip install flask-mysqldb
```

En linux mint I was the next error:
```sh
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-hbja_mr7/mysqlclient/
```
and solve it with:
```sh
$ sudo apt install default-libmysqlclient-dev
```
