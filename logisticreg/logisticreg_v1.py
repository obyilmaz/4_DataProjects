# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 22:16:09 2022

@author: oby_pc
"""

import pandas as pd
import csv
import numpy as np
traindata1=pd.read_csv("data_ready_for_ML_GENIE.txt",delimiter="\s")
testdata1=pd.read_csv("data_ready_for_ML_TCGA.txt",delimiter="\s")

#%%
traindata=traindata1.sample(n=10000)
testdata=testdata1.sample(n=5000)


# data=pd.read_csv("testdata.txt",delimiter="\s")
# data.iloc[3,1]=True
# if data.iloc[4,1]=="\"yes\"":
#     print ("ah")
# a=data.shape[0]

# a=testdata.iloc[1,51]

for i in range (traindata.shape[0]):
    for j in range (23):
        if traindata.iloc[i,j]=="\"yes\"":
            traindata.iloc[i,j]=True
        if traindata.iloc[i,j]=="\"no\"":
            traindata.iloc[i,j]=False

for i in range (testdata.shape[0]):
    for j in range (23):
        if testdata.iloc[i,j]=="\"yes\"":
            testdata.iloc[i,j]=True
        if testdata.iloc[i,j]=="\"no\"":
            testdata.iloc[i,j]=False

# nan values

traindata=traindata.dropna()
testdata=testdata.dropna()


X_train=traindata.iloc[:,0:51].values
y_train=traindata.iloc[:,51].values
X_test=testdata.iloc[:,0:51].values
y_test=testdata.iloc[:,51].values





# from sklearn import preprocessing
# le=preprocessing.LabelEncoder()
# outlook [:,0]=le.fit_transform(veriler.iloc[:,0])
# ohe= preprocessing.OneHotEncoder()
# outlook=ohe.fit_transform(outlook).toarray()


from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,np.ravel(y_train))

y_pred = logr.predict(X_test)



from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print("logistic regresion \n" , cm)

"""
confusion matrix
A true positive (TP) is a datapoint we predicted positively that we were correct about.
A true negative (TN) is a datapoint we predicted negatively that we were correct about.
A false positive (FP) is a datapoint we predicted positively that we were incorrect about.
A false negative (FN) is a datapoint we predicted negatively that we were incorrect about.
                    (actual +) (actual -)
predicted positive     TP          FP
predicted negative     FN          TN
                    (total +)  (total -)
                    
skitlearn reverse it (do??ruland?? +1)

                 predicted -   predicted +
   (actual -)       TN          FP
   (actual +)       FN          TP
                    (total +)  (total -)
                    
cm matrix te her    sat??r toplam?? ger??ek de??er,
                    sutun toplam?? tahmin edilen de??er
                                pred 0  pred 1  pred 2
                    actual 0    3       2       1
                    actual 1    0       5       2
                    actual 2    1       3       4
                    
                    
0 dan ger??ekte  6 adet var 
1 den ger??ekte  7 adet
2 den ger??ekte  8 adet
biz 4 adet 0 tahmin etmi??iz, bunlar??n 3 ??  do??ru 0(TN - 0 negatif) 1i yanl???? 2
biz 10 adet 1 tahmin etmi??iz bunlar??n 5 i do??ru (TP- 1 pozitif ????nk??)2 tanesi 0 3 tanesi 2.toplam 5 yanl????
biz 7 adet 2 tahmin etmi??iz bunlar??n 4 ?? do??ru. 1 tanesi 0 ,2 tanesi 1 toplam 3 yanl????
"""


a=pd.DataFrame(y_pred)














