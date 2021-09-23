import snowflake.connector as sf
from config import config
from snowflake.connector import DictCursor

conn = sf.connect(user=config.username,password=condig.password,account=config.account)

def execute_sql(connection,query):
    cusrsor = connection.cursor()
    cusror.execute(query)
    cusror.close()


try:
    sql = 'use {}'.format(config.database)
    execute_sql(conn,sql)

    sql = 'use warehouse {}'.format(config.warehouse)
    execute_sql(conn,sql)

    sql = 'alter warehouse {} resume'.format(config.warehouse)
    execute_sql(conn,sql)

    sql = 'select * from demodata'
    cursor.conn.cursor(DictCursor)
    cursor.execute(sql)
    for c in cursor:
        print(c)
    cusror.close()

except Exception as e:
    print(e)
finally:
    conn.close()


