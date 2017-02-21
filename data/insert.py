#encoding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        db ='zufang',
	charset='utf8'
        )
cur = conn.cursor()

f = open('xiaoqu.csv')
line = f.readline()
num = 0	
while 1:
	line = f.readline().decode('utf8')
	if not line:
		break
	tmp = line.split(',')
	name = tmp[1].encode('utf8')
	sql = "insert into block(bid,bname,longitude,latitude) values(%d,'%s',%f,%f)"%(num,name,float(tmp[2]),float(tmp[3]))
	print sql
	cur.execute(sql)
	num = num + 1
conn.commit()
cur.close()
conn.close()
