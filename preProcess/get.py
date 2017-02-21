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

sql_s = "select decorate,area,bedroom,heat,buildtime,floors,towards,fromSubway,fromFood,fromStation,fromAirport,fromKindergarten,fromPrimarySchool,fromMiddleSchool,fromCollege,fromGarden,fromCenter,numRepast,numGym,numMedical,numCultureFacilities,numLifeService,price,hid,qu from house left join block on house.bid = block.bid"
cur.execute(sql_s)
results= np.array(list(cur.fetchall()))

X = np.zeros([58994,23])
Y = np.zeros([58994,1])
ID = np.zeros([58994,1])
error = []

for i in range(len(results)):
	item = results[i]
	for j in range(len(item)):
		if j == 0:
			if item[0] == '':
				value = -1
			elif item[0] == u'精装修':
				value = 1
			else:
				value = 0
		elif j == 3:
			if item[3] == '':
				value = 0 #no
			elif item[3] == u'集中供暖':
				value = 1
			else:
				value = -1
		elif j == 6:
			if u"北" in item[6]:
				value = -1
			elif u"南" in item[6]:
				value = 1
			else:
				value = 0
		elif j == 24:
			if item[24] == 'haidian':
				value = 1
			elif item[24] == 'chaoyang':
				value = 2
			elif item[24] == 'changping':
				value = 3
			elif item[24] == 'xicheng':
				value = 4
			elif item[24] == 'dongcheng':
				value = 5
			elif item[24] == 'tongzhou':
				value = 6
			elif item[24] == 'fengtai':
                                value = 7
			elif item[24] == 'shunyi':
                                value = 8
			elif item[24] == 'daxing':
                                value = 9
			elif item[24] == 'yizhuangkaifaqu':
                                value = 10
			elif item[24] == 'fangshan':
                                value = 11
			elif item[24] == 'shijingshan':
                                value = 12
			elif item[24] == 'mentougou':
                                value = 13
			elif item[24] == 'yanjiao':
                                value = 14
			elif item[24] == 'yanqing':
                                value = 15
		else:
			if item[j] is None:
				value = 0
			else:
				value = item[j]
		
		if j < 22 or j == 24:
			pos = j
			if j == 24:
				pos = 22
			X[i,pos] = value
		elif j == 23:
			ID[i,0] = int(value)
		else:
			Y[i,0] = value

print X
print Y
print ID

np.save(open('all_X.npy','w'), X)
np.save(open('all_Y.npy','w'), Y)
np.save(open('ID.npy','w'),ID)			
