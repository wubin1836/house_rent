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

	hname = ''	
        bname = ''
        bedroom = -1 
        area = -1
        price = -1
        heat = ''
        buildtime = -1
        floors = -1
        towards = ''
	decorate = ''
	tmp = line.split('#')
	for item in tmp:
		try:
			tt = item.split('=')
			if tt[0] == u'房屋名称':
				hname = tt[1].encode('utf8')
			if tt[0] == u'小区名称':
				bname = tt[1].encode('utf8')
			elif tt[0] == u'几室':
				bedroom = int(tt[1])
			elif tt[0] == u'面积':
				area = int(tt[1])
			elif tt[0] == u'总价':
				price = int(tt[1])
			elif tt[0] == u'供暖':
				heat = tt[1].encode('utf8')
			elif tt[0] == u'建造时间':
				buildtime = int(tt[1])
			elif tt[0] == u'共几层':
				floors = int(tt[1])
			elif tt[0] == u'朝向':
				towards = tt[1].encode('utf8')
			elif tt[0] == u'装修类型':
				decorate = tt[1].encode('utf8')
		except:
			pass
	sql_s = "select bid from block where bname ='%s'"%bname
	cur.execute(sql_s)
	results= list(cur.fetchall())

	try:
		sql = "insert into house(hid,bid,hname,decorate,area,price,bedroom,heat,buildtime,floors,towards) values(%d,%d,'%s','%s',%d,%d,%d,'%s',%d,%d,'%s')"%(num,results[0][0],hname,decorate,area,price,bedroom,heat,buildtime,floors,towards)
		print sql
		cur.execute(sql)
		num = num + 1
	except:
		pass
conn.commit()
cur.close()
conn.close()
