from pymysql_terminal import Connection, Executor

# пример использования библиотеки
if __name__ == "__main__":
    conn = Connection(host="localhost", database="mydb", user="root", password="root")
    ex = Executor(conn)

    print("=== товары ===")
    ex.print_table("SELECT product_id, product_name, price, discount FROM products")

    print("\n=== заказы ===")
    ex.print_table("SELECT order_id, product_id, status_id, order_date FROM orders")

    conn.close()
