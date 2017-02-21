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

from math import radians, cos, sin, asin, sqrt  
  
def haversine(lon1, lat1, lon2, lat2): 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 
    return c * r 

#csvfile = open('POI/sss.csv', 'r')
#data = []
#for line in csvfile:
#    data.append(list(line.strip().split(',')))

cur.execute("select bid,longitude,latitude from block")
results= list(cur.fetchall())

for block in results:
	long1 = block[1] 
	lat1 = block[2]
	

	long2 = 39.908719
	lat2 = 116.397517
	dis = haversine(long1,lat1,long2,lat2)
	#for item in data:
	#	long2 = float(item[1])
	#	lat2 = float(item[2])

	#	dis = haversine(long1,lat1,long2,lat2)
	#	
	#	if dis < max_dis:
	#		max_dis = dis
	try:
		sql = "UPDATE block SET fromCenter = %f where bid = %d"%(dis,block[0])
		print sql
		cur.execute(sql)
		conn.commit()
	except:
		pass
cur.close()
conn.close()
