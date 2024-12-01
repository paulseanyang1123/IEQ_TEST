import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing, linear_model
from sklearn.model_selection import train_test_split
import numpy as np


from sklearn.svm import SVC

df = pd.read_csv(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\csv-file-for-776.csv')
# sex = pd.get_dummies(df.gender)

Y=df.gender
print(Y)
DF=df.iloc[:,2:20]
print(DF)
X=DF
clf = SVC(kernel='linear', probability=True)
clf.fit(X, Y)

yhat_prob = clf.predict_proba(X) #
print('probability of chosen data:', '\n', yhat_prob)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
yhat = clf.predict(X)  # probability [130, 164, 891, 1056]
confusion_matrix(Y, yhat)
acc_score = accuracy_score(Y, yhat)  # Yh
print("\n", "Related results data: ".format(format(acc_score, '.3f')))
print("\n", "CFM: \n", confusion_matrix(Y, yhat))
print("\n", "Classification report: \n", classification_report(Y, yhat))
# y_pred = clf.predict(X) # class label
print('Gender label of chosen data:', '\n', yhat)

from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, confusion_matrix, auc, accuracy_score
# k = len(DF.engnat)
# for i in range(k):
#     if DF.engnat[i] > 1:
#         DF.engnat[i] = 0
# DFxy=np.array(DF.engnat)
# # DFxy = DF.engnat
# Y=DFxy   # training data Y
# print(Y)
C = 1.0 # SVM regularization parameter
clf = SVC(kernel = 'linear', C = C,probability=True)
clf.fit(X, Y)
yhat_prob1 = clf.predict_proba(X) # probability
# y_pred = clf.predict(X) # class label
print('probability of gender in chosen data X:', '\n', yhat_prob1)

# roc_auc_0 = roc_auc_score (Y, 1-yhat[:, 2])
fpr_0, tpr_0, _ = roc_curve(Y, yhat_prob1[:, 0], pos_label='f') # here the label is NOT 0 or 1, but f or m
roc_auc_0 = roc_auc_score (Y, yhat_prob1[:, 0])
# class 1
fpr_1, tpr_1, _ = roc_curve(Y, yhat_prob1[:, 1], pos_label='m')
roc_auc_1 = roc_auc_score(Y, yhat_prob1[:, 1])
# class 2

# plot ROC curves
print('roc_auc_0: ', roc_auc_0)
print('roc_auc_1: ', roc_auc_1, '\n')
# fig = plt.figure()
# plt.subplot(1,2,1)

plt.plot(fpr_0, tpr_0, marker='.', label='Class f', color='b')
plt.plot(fpr_1, tpr_1, marker='+', label='Class m', color='r')
# plt.subplot(1,2,2)
plt.title('ROC curve of each class f or m',color='g',fontsize=16)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
