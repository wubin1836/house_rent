# data 负责读写和存储数据
### dis,image,in_house,num,qu,sub,url分别负责对应数据

# preProcess 负责预处理，过滤不可靠的数据
### preProcess/get_filter.py 过滤，存取在X.npy,Y.npy,ID.npy

# 降维
## PCA 负责主成分分析算法实现
### PVA/PCA.py
## RBC 负责有限状态玻尔兹曼机降维
### RBM/rbm.py
## VAE 负责varitional auto-encoder 降维
### VAE/vae.py

# 线性回归LR，多项式回归Polynomial
### LR/LR.py LR/Polynomial.py

# 多层感知机
### MLR/MLP.py

# 图像分类
### 图像像素转位numpy数组 image/image_to_numpy.py
### image/cifar10_train.py图像分类，用了tensorflow tutorial 的源代码cifar10_train.py (https://github.com/tensorflow/models.git)
