from pymysql_terminal.connection import Connection
from pymysql_terminal.formatter import Formatter


class Executor:
    """выполняет sql-запросы и возвращает результат в нужном формате"""

    def __init__(self, connection: Connection):
        self._conn = connection
        self._formatter = Formatter()

    def fetch(self, sql, params=None):
        """выполнить select и вернуть список словарей"""
        with self._conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.fetchall()

    def fetch_one(self, sql, params=None):
        """выполнить select и вернуть одну строку"""
        with self._conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.fetchone()

    def execute(self, sql, params=None):
        """выполнить insert / update / delete с автоматическим commit"""
        with self._conn.cursor() as cur:
            cur.execute(sql, params or ())
        self._conn.commit()

    def print_table(self, sql, params=None):
        """выполнить select и вывести результат в терминал в виде таблицы"""
        rows = self.fetch(sql, params)
        if rows:
            self._formatter.print_table(rows)
        else:
            print("нет данных")
