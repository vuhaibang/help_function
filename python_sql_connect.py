import pymysql
from sqlalchemy import create_engine

def connect_sql(host, port, user, pw, db, auto=True):
    conn = pymysql.connect(
        host=host,
        port=int(port),
        user=user,
        passwd=pw,
        db=db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=auto)
    return conn


def engine_sql(host, port, user, pw, db):
    return create_engine(f'mysql+pymysql://{user}:{pw}@{host}:{port}/{db}')


with conn().cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()


