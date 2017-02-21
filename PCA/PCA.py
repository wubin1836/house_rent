import numpy as np
from sklearn.decomposition import PCA  

X = np.load('all/all_X.npy')
Y = np.load('all/all_Y.npy')
ID = np.load('ID.npy')
newX = []
newY = []
newID = []

print X.shape

for i in range(len(X)):
	error = 0
	for j in range(len(X[i])):
		if j != 0 and j != 3 and j != 6:
			if X[i,j] < 0:
				error = 1
	if Y[i,0] < 1000 or X[i,1] > 500 or Y[i,0]/X[i,1] > 1000 or Y[i,0]/X[i,1] < 10:
		error = 1
	if error == 0: #true data
		newX.append(X[i])
 		newY.append(Y[i])
		newID.append(ID[i])

newX = np.array(newX)
newY = np.array(newY)
newID = np.array(newID)

print newX.shape

np.save(open('newX.npy','w'),newX)
np.save(open('newY.npy','w'),newY)
np.save(open('newID.npy','w'),newID)

pca=PCA(n_components='mle')  
newX_PCA = pca.fit_transform(newX) 

print "before PCA:"
print newX.shape
print newX

print "\n after PCA:"
print newX_PCA.shape
print newX_PCA

np.save(open('newX_PCA.npy','w'),newX_PCA)
