'''
Method of machine learning with Linear regression to show the Thetas ,ie, importance of all features.
'''
# import analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder as enc
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df = pd.read_csv(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\csv-file-for-776.csv')
# Linear regression analysis to 18 features to show the importance of each variable.
# love=np.array(df.LOVE)
# # loc=np.array(sy.Location)
# # ss=np.array(sy.SelfAssessedHealthStatus)
# # sm=np.array(sy.Smoker)
# kindness=np.array(df.KINDNESS)
# pure=np.array(df.PURITY)
# fair=np.array(df.FAIRNESS)
# generalous=np.array(df.GENERALNESS)
# humble=np.array(df.MODESTY)
avge=np.array(df.STATISTICSIE)
# Dummy Variables using pandas or sklearn
sex = pd.get_dummies(df.gender)
# print(dmy,'\n')
# sex = np.array(sex,'\n')
# sex=sex[:,0]
# print(sex)

# X=np.array([age,hg,wg]) #,sex,ss,sm,loc
# ZX = preprocessing.scale(X)  #[sy.Age, sy.Height, sy.Weight]
# print(ZX, '\n') # zscore of X
# print('\n')
# print(ZX.mean(axis=0), '\n',ZX.std(axis=0))

# XX=pd.concat([ZX,sex,ss,sm,loc]) #,sex,ss,sm,loc
# XX=np.array([ZX,sex,ss,sm,loc]) #,sex,ss,sm,loc
XX=pd.concat([df.LOVE, df.KINDNESS, df.PURITY, df.FAIRNESS,df.GENERALNESS, df.MODESTY,df.JOY,df.TOLERATE, df.FAITHFULNESS, df.TRUTHFULNESS,df.BEAUTY, df.FOREVER,
              df.FULLNESS,df.WISDOM, df.RICHNESS, df.CONTROL,df.PREDICT, df.CREATING,sex], axis=1) #,sex,ss,sm,loc
#  df.JOY,df.TOLERATE, df.FAITHFULNESS, df.TRUTHFULNESS,df.BEAUTY, df.FOREVER,
#               df.FULLNESS,df.WISEDOM, df.RICHNESS, df.CONTROL,df.PREDICT, df.CREATING,
XX['LOVE'] = preprocessing.scale(XX['LOVE'])
# print(XX['Age'])
XX['KINDNESS'] = preprocessing.scale(XX['KINDNESS'])
XX['PURITY'] = preprocessing.scale(XX['PURITY'])
XX['FAIRNESS'] = preprocessing.scale(XX['FAIRNESS'])
# print(XX['Age'])
XX['GENERALNESS'] = preprocessing.scale(XX['GENERALNESS'])
XX['MODESTY'] = preprocessing.scale(XX['MODESTY'])
XX['JOY'] = preprocessing.scale(XX['JOY'])
# print(XX['Age'])
XX['TOLERATE'] = preprocessing.scale(XX['TOLERATE'])
XX['FAITHFULNESS'] = preprocessing.scale(XX['FAITHFULNESS'])
XX['TRUTHFULNESS'] = preprocessing.scale(XX['TRUTHFULNESS'])
# print(XX['Age'])
XX['BEAUTY'] = preprocessing.scale(XX['BEAUTY'])
XX['FOREVER'] = preprocessing.scale(XX['FOREVER'])
XX['FULLNESS'] = preprocessing.scale(XX['FULLNESS'])
# print(XX['Age'])
XX['WISDOM'] = preprocessing.scale(XX['WISDOM'])
XX['RICHNESS'] = preprocessing.scale(XX['RICHNESS'])
XX['CONTROL'] = preprocessing.scale(XX['CONTROL'])
# print(XX['Age'])
XX['PREDICT'] = preprocessing.scale(XX['PREDICT'])
XX['CREATING'] = preprocessing.scale(XX['CREATING'])
# enc.fit(X)
# xx = enc.transform(sm).toarray()
# print(xx)

# print(ZX.shape,bp.shape)

# y_train=sy.Sytolic
# ZXb = scaler.fit_transform(X) # zscore of X
# print(scaler.mean_, scaler.var_)

# Create linear regression object
regr = linear_model.LinearRegression()
regr.fit(XX, avge)
# Make predictions using the testing set
# y_pred = regr.predict(ZX)
# The coefficients
print('The regression coefficients (thetas): \n', regr.coef_,regr.intercept_ )#,regr.intercept_
# print(regr.coef_[0])

fig = plt.figure(6)
plt.scatter(regr.coef_,regr.coef_, color='g')
plt.legend(["Weights"], title='Distribution of weights',loc='best',facecolor='r',fontsize=16)#'upper right','best'
plt.axhline(y=0.08,ls="-.",c="b")#添加水平直线
plt.axvline(x=0.08,ls="-.",c="r")#添加v直线
plt.title('Distribution of weights of all predictors',color='g',fontsize=16)# 中文


fig = plt.figure(4)  #plt.figure(figsize=(10, 5))
data = {'LOVE': 0.07784871, 'KIND': 0.0731731 ,'PURITY': 0.11515592, 'FAIR': 0.08221612 ,'GENERAL':  0.07777214 , 'MODESTY': 0.08843202 ,'JOY': 0.08479981, 'TOLERATE': 0.10921603,
        'FAITH': 0.12108048, 'TRUTH': 0.07514078 ,'BEAUTY': 0.09185854, 'FOREVER': 0.10076314,'FULL': 0.09639698, 'WISDOM': 0.09981101 ,'RICH': 0.10387958, 'CONTROL': 0.07664658  ,'PREDICT': 0.11116337, 'CREATING': 0.09280703 , 'GENDER': 0.00599103}
importances = list(data.keys())
print('key of importance',importances)
values = list(data.values())
print('Values of importance',values)
# creating the bar plot
plt.bar(importances,values, color= 'red', width=0.4) #'maroon'
plt.legend(["Importances"], title='Importance values of all features',loc='best',facecolor='g',fontsize=16)  # empty is also ok
plt.ylim(0, 0.2)
# plt.xlim(0,1)
plt.xlabel("Features")
plt.ylabel("Importance values")
plt.title("Importance values of all features")

from sklearn.linear_model import Lasso
for alp in np.arange(0.0000001, 1.1, 0.1):#-1.1,
    clf = Lasso(alpha=alp)  # = l
clf.fit(XX, avge)
print(np.round(alp, 2), np.round(clf.coef_, 2),
      np.round(clf.intercept_, 2))
# list=[]
# for i in range(len(regr.coef_)):
#     list.append(regr.coef_[i])
# print(list)
# fig = plt.figure()
# # plt.plot(list)
from sklearn.linear_model import LassoCV, LassoLarsCV
model_lars = LassoLarsCV(cv=10, normalize=False)
model_lars.fit(XX, avge)

# plot coefficient progression lasso lars
m_log_alphas_lars = -np.log10(model_lars.alphas_)
# m_log_alphas_lars = model_lars.alphas_
print('alpha or lambda, amount of regularization: ','\n',model_lars.alphas_) # alpha or lambda, amount of regularizationm_log_alphas_lars
print('alpha or lambda, values as -np.log10(model_lars.alphas_): ','\n',-np.log10(model_lars.alphas_)) # alpha or lambda, amount of regularizationm_log_alphas_lars
print('coefficients over different regularization: ','\n',model_lars.coef_path_.T) # coefficients over different regularization
fig = plt.figure(5)
ax = plt.gca()
plt.plot(m_log_alphas_lars, model_lars.coef_path_.T)
plt.axvline(-np.log10(model_lars.alpha_), linestyle='dashdot', color='r', label='alpha CV')
plt.axhline(y=0.08,ls="-.",c="b")#添加水平直线
plt.ylabel('Regression Coefficients')
plt.legend(["alpha CV"], title='Progression for Lasso Using LARS Alg',loc='lower center',facecolor='g',fontsize=16)#'upper right','best'
plt.xlabel('-log(alpha)')
plt.title('Regression Coefficients Progression for Lasso Using LARS Alg')
# plt.show()


plt.show()

