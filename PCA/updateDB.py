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
validIDs = np.load('newID.npy')
print len(validIDs)

for i in range(len(validIDs)):
	validID = int(validIDs[i][0])
	#print validID
	sql = "update house set isValid=1 where hid=" + str(validID)
	cur.execute(sql)
try:   
	conn.commit() 
except: 
	conn.rollback()
conn.close()
