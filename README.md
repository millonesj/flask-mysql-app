# flask-mysql-app

First, create your enviroment:
```ssh
python3 -m venv .env
```
activate it:
```sh
source .env/bin/activate
```

Create your instance mysql's docker with:
```sh
docker run --name mysql-for-flask-mysql-app -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.0

```
Install the next dependencies:
```sh
pip install flask
pip install mysql-connector
pip install flask-mysqldb
```

En linux mint I was the next error:
```sh
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-hbja_mr7/mysqlclient/
```
and solve it with:
```sh
sudo apt install default-libmysqlclient-dev
```