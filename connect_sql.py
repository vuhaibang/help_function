import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=int(3306),
    user='bangvh',
    passwd='rmpxRdnGpT32XZL4cZweBMA',
    db='avy_api',
    charset='utf8mb4',
    autocommit=True)