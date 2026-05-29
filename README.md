# pymysql-terminal

Lightweight wrapper around [PyMySQL](https://github.com/PyMySQL/PyMySQL) for executing queries and displaying results in the terminal.

## Install

```bash
pip install pymysql-term
```

Or from source:

```bash
pip install git+https://github.com/pymysql-term/pymysql-term.git
```

## Usage

```python
from pymysql_terminal import Connection, Executor

conn = Connection(host="localhost", database="mydb", user="root", password="root")
ex = Executor(conn)

# print query result as a table
ex.print_table("SELECT * FROM products WHERE discount > %s", (10,))

# fetch as list of dicts
rows = ex.fetch("SELECT * FROM orders")

# insert / update / delete
ex.execute("UPDATE products SET price = %s WHERE product_id = %s", (999.0, 1))

conn.close()
```
## API

### `Connection(host, database, user, password, port, charset)`
Connects to MySQL. Supports auto-reconnect.

### `Executor(connection)`
- `fetch(sql, params)` → `list[dict]`
- `fetch_one(sql, params)` → `dict`
- `execute(sql, params)` — INSERT / UPDATE / DELETE
- `print_table(sql, params)` — prints formatted table to terminal

### `Formatter`
- `print_table(rows)` — print list of dicts as ASCII table
- `to_csv(rows, delimiter)` → `str`
