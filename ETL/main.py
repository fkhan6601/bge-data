import mariadb
import sys
from storedata import storeDay, storeHour

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="passowrd",
        host="127.0.0.1",
        port=3306,
        database="bge"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
try:
    cur.execute("DROP TABLE IF EXISTS monthly")
    cur.execute("DROP TABLE IF EXISTS daily")
    cur.execute("DROP TABLE IF EXISTS hourly")
    cur.execute("CREATE TABLE IF NOT EXISTS daily (id INT NOT NULL AUTO_INCREMENT, date DATETIME, usage_amt DOUBLE(6,2), PRIMARY KEY (id));")
    cur.execute("CREATE TABLE IF NOT EXISTS hourly (id INT NOT NULL AUTO_INCREMENT, date DATETIME, usage_amt DOUBLE(6,2), PRIMARY KEY (id));")
except mariadb.Error as e: 
    print(f"Error: {e}")

# storeDay(conn)
storeHour(conn)
conn.commit()
conn.close()

