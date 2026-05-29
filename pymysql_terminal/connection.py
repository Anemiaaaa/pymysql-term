import pymysql
from pymysql.cursors import DictCursor


class Connection:

    def __init__(self, host="localhost", database="", user="root",
                 password="", port=3306, charset="utf8"):
        self._config = dict(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port,
            charset=charset,
            cursorclass=DictCursor,
        )
        self._conn = None
        self.connect()

    def connect(self):
        self._conn = pymysql.connect(**self._config)

    def cursor(self):
        # переподключаемся если соединение было сброшено
        try:
            self._conn.ping(reconnect=True)
        except Exception:
            self.connect()
        return self._conn.cursor()

    def commit(self):
        self._conn.commit()

    def close(self):
        if self._conn:
            self._conn.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
