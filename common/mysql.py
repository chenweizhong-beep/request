# ***
# @autor CWZ
# ***
import pymysql

from common.config import cf
from common.log import log


class Mysql:
    """
    操作mysql的类
    """

    def __init__(self):
        """
        初始化mysql的conn对家，连接数据库
        """
        # 通过配置文件获取数据库的host，port，username，password，charset，database
        host = cf.get_value("mysql", "host")
        # 从配置文件获取的值是str，需要转化成int
        port = int(cf.get_value("mysql", "port"))
        user = cf.get_value("mysql", "user")
        password = cf.get_value("mysql", "password")
        charset = cf.get_value("mysql", "charset")
        # print(charset)
        database = cf.get_value("mysql", "database")
        # 当无法连接数据库，走异常处理处理
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user,
                                        password=password, charset=charset, database=database)
        except Exception as e:
            log.error(f"无法登陆数据库，错误原因：{e}")
        # self.cur = self.conn.cursor()

    def select(self, query):
        '''
        查询语句方法
        :param query:
        :return:
        '''
        log.info(f"select语句是{query}")
        try:
            cur = self.conn.cursor()
            # 执行查询语句
            cur.execute(query)
            # 获取查询语句的结果
            select_data = cur.fetchall()
            return select_data
        except Exception as e:
            log.error(f"select语句错误，错误原因是{e}")
        # cur.close()
        # self.conn.close()

    def update(self, query):
        '''
        修改语句方法
        :param query:
        :return:
        '''
        log.info(f"update语句是{query}")
        try:
            cur = self.conn.cursor()
            # 执行修改语句
            cur.execute(query)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            log.error(f"update语句错误，错误原因是{e}")
            # 语句错误，回滚事务
            self.conn.rollback()
        # cur.close()
        # self.conn.close()

    def insert(self, query):
        '''
        插入语句方法
        :param query:
        :return:
        '''
        log.info(f"insert语句为{query}")
        try:
            cur = self.conn.cursor()
            cur.execute(query=query)
            self.conn.commit()
        except Exception as e:
            log.error(f"insert语句错误，错误原因是{e}")
            self.conn.rollback()

    def delete(self, query):
        '''
        删除语句方法
        :param query:
        :return:
        '''
        log.info(f"delete语句为{query}")
        try:
            cur = self.conn.cursor()
            cur.execute(query=query)
            self.conn.commit()
        except Exception as e:
            log.error(f"delete语句错误，错误原因是{e}")
            self.conn.rollback()


mysql = Mysql()
if __name__ == '__main__':
    query = 'SELECT cal_id FROM calender;'
    data = mysql.select(query)
    print(data)
    print(type(data))
    # cal_id = [i[0] for i in data]
    # print(cal_id)
    lis = []
    for i in data:
        print(i[0])
        lis.append(i[0])
    print(lis)
    print(type(lis))
    # query = 'select * from dept;'
    # data = mysql.select(query)
    # print(data)
    # query1 = 'UPDATE dept SET loc= "haha3"  WHERE deptno = 10;'
    # mysql.update(query1)
    # print(mysql.select(query))
    # query2 = "INSERT INTO dept VALUES(50,'本部','武汉');"
    # mysql.insert(query2)
    # print(mysql.select(query))
    # query3 = "delete from dept where deptno = 50;"
    # mysql.delete(query3)
    # print(mysql.select(query))
