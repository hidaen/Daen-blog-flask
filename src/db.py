from sqlalchemy import create_engine

MYSQL_HOST = 'localhost'
MYSQL_USER = 'dbuser'
MYSQL_PASS = 'dbpassword'
MYSQL_DB = 'wordpress'
MYSQL_PORT = 3306

DB_CONNECT_STRING = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (MYSQL_USER,MYSQL_PASS,\
    MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
mysql_db = create_engine( DB_CONNECT_STRING)
