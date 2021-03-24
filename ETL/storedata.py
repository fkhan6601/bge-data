import mariadb
import sys
from fetchdata import monthlyGet
from fetchday import dailyGet

def storeDay(conn):
    for k in range(19,21):
        for j in range(1,13):
            if j < 12:
                value, time = monthlyGet('20'+ str(k) + '-' + str(f"{j:02d}") + '-01', '20' + str(k) + '-' + str(f"{(j+1):02d}") + '-01', 'day')
                cur = conn.cursor()
                for i in range(len(value)-1):
                    dtime = time[i].replace('T', ' ')
                    dtime = dtime[:-6]
                    try:
                        cur.execute("INSERT INTO daily (date, usage_amt) VALUES (?,?)", (dtime, value[i]))
                    except mariadb.Error as e: 
                        print(f"Error: {e}")
            else:
                value, time = monthlyGet('20'+ str(k) + '-' + str(j) + '-01', '20' + str(k+1) + '-' + str(f"{1:02d}") + '-01', 'day')
                cur = conn.cursor()
                for i in range(len(value)-1):
                    dtime = time[i].replace('T', ' ')
                    dtime = dtime[:-6]
                    try:
                        cur.execute("INSERT INTO daily (date, usage_amt) VALUES (?,?)", (dtime, value[i]))
                    except mariadb.Error as e: 
                        print(f"Error: {e}")

def storeHour(conn):
    for k in range(19,20):
        for j in range(1,3):
            for l in range(1, 29):
                value, time = dailyGet('20'+ str(k) + '-' + str(f"{j:02d}") + '-' + str(f"{l:02d}"), '20' + str(k) + '-' + str(f"{j:02d}") + '-' + str(f"{l:02d}"), 'hour')
                cur = conn.cursor()
                for i in range(len(value)-1):
                    dtime = time[i].replace('T', ' ')
                    dtime = dtime[:-6]
                    try:
                        cur.execute("INSERT INTO hourly (date, usage_amt) VALUES (?,?)", (dtime, value[i]))
                    except mariadb.Error as e: 
                        print(f"Error: {e}")

            value, time = dailyGet('20'+ str(k) + '-' + str(f"{j:02d}") + '-' + str(29), '20' + str(k) + '-' + str(f"{(j+1):02d}") + '-' + str(f"{1:02d}"), 'hour')
            cur = conn.cursor()
            for i in range(len(value)-1):
                dtime = time[i].replace('T', ' ')
                dtime = dtime[:-6]
                try:
                    cur.execute("INSERT INTO hourly (date, usage_amt) VALUES (?,?)", (dtime, value[i]))
                except mariadb.Error as e: 
                    print(f"Error: {e}")
