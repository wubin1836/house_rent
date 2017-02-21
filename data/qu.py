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

f = open('zufang')
line = f.readline()
num = 0	
while 1:
	line = f.readline().decode('utf8')
	if not line:
		break
	tmp = line.split('#')
	name = tmp[0].split('=')[1]
	qu = tmp[25].split('=')[1]
	try:
		sql = "update house set qu = '%s' where hname = '%s'"%(qu,name)
		print sql
		cur.execute(sql)
	except:
		pass
conn.commit()
cur.close()
conn.close()
