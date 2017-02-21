import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier  
from sklearn.utils import column_or_1d
from sklearn.externals import joblib

X = np.load('newX.npy')
y = np.load('newY.npy')

y_class = []
for item in y:
	y_class.append(int(item[0]/500))

y_class = np.array(y_class)

X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.01,random_state=0)

clf = MLPClassifier(activation='relu', solver='adam', alpha=1e-5,  
                hidden_layer_sizes=(500, ), random_state=0,
		batch_size='auto',learning_rate_init=0.01,
		shuffle=True,max_iter=1000000)  

#clf.fit(X_train, y_train)  
#y_pred = clf.predict(X_test)

#print y_pred
#print y_test

clf.fit(X, y_class)
y_pred = clf.predict(X)

for i in range(len(y_pred)):
	#print float(y_pred[i] - y_test[i]) / y_test[i]
	#print i, y_class[i], y_pred[i]
	print y_pred[i]

joblib.dump(clf, "train_model.m")
