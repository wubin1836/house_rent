#encoding=utf-8
import MySQLdb
import numpy as np

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        db ='zufang',
	charset='utf8'
        )
cur = conn.cursor()

ID = np.load('newID.npy')
index = 0

f = open('MLP_out.txt')

while 1:
	line = f.readline()
	if not line:
		break
	price = int(line)
	sql = "update house set predictClassPrice = %d where hid = %d"%(price,ID[index])
	#print sql
	#cur.execute(sql)
	index = index + 1
conn.commit()
cur.close()
conn.close()
