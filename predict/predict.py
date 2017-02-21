from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.externals import joblib
from wsgiref.simple_server import make_server

def application(environ, start_response):
	start_response('200 OK',  [('Content-Type', 'text/plain'),("Access-Control-Allow-Origin", "*"),("Access-Control-Allow-Methods", "GET")])
	print environ['QUERY_STRING']

	x = np.zeros(23);
	qs = environ['QUERY_STRING'];
	qslist = qs.split('&');
	for i in range(len(qslist)):
		item = qslist[i].split('=')
		x[i] = float(item[1])
	
	print len(x), x
	LR = joblib.load("train_model.m")
	y = LR.predict(x)
	return str('rent: ' + str(int(y[0][0])))

httpd = make_server('0.0.0.0', 8888, application) 

print "Serving HTTP on port 8888..."
httpd.serve_forever()


