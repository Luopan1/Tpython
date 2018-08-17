# coding=utf-8
import pymysql


class DbHelper(object):
    def __init__(self, host, user, passwd, db, port, charset="utf-8"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.chartset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port,
                                    charset=self.chartset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_All(self, SQL, parames=()):
        list = ()
        try:
            self.connect()
            self.cursor.execute(SQL, parames)
            list = self.cursor.fetchall()
            self.close()
        except Exception as  e:
            print(e)
        return list

    def get_one(self, sql, patames=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, patames)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count
