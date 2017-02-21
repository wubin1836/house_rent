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
	bname = tmp[3].split('=')[1]
	dis = tmp[16].split('=')[1]

	if dis != '':
		try:
			dis = float(dis)/1000
			sql_s = "select bid from block where bname ='%s'"%bname
			cur.execute(sql_s)
			results= list(cur.fetchall())
			sql = 'update block set fromSubway = %f where bid = %d'%(dis,results[0][0])
			cur.execute(sql)
		except:
			pass
		#num = num + 1
conn.commit()
cur.close()
conn.close()
