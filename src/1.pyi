# conn  = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     charset='utf8',
#     database="db_test"
# )
# cursor = conn.cursor()
# sql='''
# CREATE TABLE IF NOT EXISTS tb_test (
# ID varchar(11) NOT NULL,
# DATEY date NOT NULL,
# DATEM date NOT NULL,
# LEVEL INTEGER(4) NOT NULL,
# VALUE float DEFAULT NULL,
# NUM tinyint DEFAULT NULL)
# '''
# cursor.execute(sql)
# cursor.close()
# conn.close()