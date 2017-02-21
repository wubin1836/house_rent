from sklearn import metrics
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

linreg = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)

X = np.load('newX.npy')
y = np.load('newY.npy')

print type(X)
exit()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.001,random_state=0)

print X_train.shape
print X_test.shape
print y_train.shape
print y_test.shape

linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)

#print y_test
#print y_pred

print np.sqrt(metrics.mean_squared_error(y_test, y_pred))

for i in range(len(y_test)):
	#print (y_test[i][0]-y_pred[i][0])/y_test[i][0]
	print y_test[i][0], y_pred[i][0]

#linreg.fit(X, y)
#y_pred = linreg.predict(X)

#for item in y_pred:
#	print item[0]

joblib.dump(linreg, "train_model.m")
