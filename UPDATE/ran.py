#encoding=utf-8
import MySQLdb
import numpy as np
import random

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        db ='zufang',
	charset='utf8'
        )
cur = conn.cursor()

sql_s = "select hid,block.longitude,block.latitude from house left join block on house.bid = block.bid"
cur.execute(sql_s)
results= list(cur.fetchall())

for r in results:
	i = float(random.randint(-100, 100)) / 100
	j = float(random.randint(-100, 100)) / 100

	lon = r[1] + 1/111 * i
	lat = r[2] + 1/111 * j
	sql = "update house set longitude = %f ,latitude = %f where hid = %d"%(lon,lat,r[0])
	print sql
	cur.execute(sql)

conn.commit()
cur.close()
conn.close()
