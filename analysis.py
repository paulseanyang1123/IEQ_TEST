# import testdigit as td   if  you import this you need to import name and gender again

import pandas as pd
from csv import writer
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest, describe
from scipy.stats import normaltest
from numpy.random import poisson
# from matplotlib.pyplot import hold
df = pd.read_csv(r'C:\Users\xuyan\Desktop\776-777-project\csv-file-for-776.csv')
print(df.iloc[:,2:3]) # this command is used to show the certain columns: iloc
print(df.iloc[0:3,:])# this command is used to show the certain rows: iloc
# n = len(df.ANIMALID)
# print (n)  #df.ANIMALID[0]
# for dfc in df:
#     print(dfc[1])
tdaveragetesttotal = df.STATISTICSIE
averagescore=np.average(tdaveragetesttotal)
# def compare_fm_beauty():
gender_type = df.gender
beauty_index = df.BEAUTY
kk=len(gender_type)
# print(gender_type[0])
sum1=0
sum2=0
m=0
n=0
listfemale=[]
listmale=[]
for i in range(kk):
    if gender_type[i] == "f":
          listfemale.append(beauty_index[i])
          sum1 += beauty_index[i]
          m += 1
    else:
        listmale.append(beauty_index[i])
        sum2 = sum2+ beauty_index[i]
        n += 1
ksresult1 = kstest(beauty_index, 'norm')   #  https://www.runoob.com/scipy/scipy-significance-tests.html  tdaveragetesttotal


print('Distribution test pvalue kstest:  ',ksresult1.pvalue)

print('scipy normal test result pvalue of beauty column:   ',round(normaltest(beauty_index).pvalue,2))  # scipy normal test result pvalue.

res = describe(beauty_index)  # describe all parametes of beauty column.
print(res)

ksresult2 = kstest(tdaveragetesttotal, 'norm')   #  https://www.runoob.com/scipy/scipy-significance-tests.html  tdaveragetesttotal

print('Distribution ks-test pvalue of total average:  ',ksresult2.pvalue)

print('scipy normal test result pvalue of average scores:   ',round(normaltest(tdaveragetesttotal).pvalue,2))  # scipy normal test result pvalue.


print('Female beauty score list ',listfemale,'\n','Male beauty score list ',listmale)  # '\n'  change line
print('Average score of female in beauty:  ', round(sum1/m,2),m )
print( 'Average score of male in beauty:  ', round(sum2/n,2),n)
std_f=np.std(listfemale)
std_m=np.std(listmale)
print('Standard deviation of female and male in beauty are:   ',  round(std_f,2),round(std_m,2))
print('Average score of all in beauty:  ', round(sum(beauty_index)/kk,2) )
# print('Average score of all in beauty:  ', round(statistics.mean(beauty_index),2) )
# print( sum1/m,'\n', sum2/n) #'Average score of female in beauty’,'Average score of male in beauty',
data = {'Female': sum1/m, 'Male': sum2/n }
genders = list(data.keys())
values = list(data.values())

fig = plt.figure(2)  #plt.figure(figsize=(10, 5))

# creating the bar plot
std_err=[std_f,std_m]
error_params=dict(elinewidth=4,ecolor='g',capsize=5)#设置误差标记参数
# #绘制柱状图，设置误差标记以及柱状图标签
# # plt.bar(x,y,color=['b','g','yellow','orange','gray'],yerr=std_err,error_kw=error_params,\
# #                     tick_label=['blue','green','yellow','orange','gray'])
# plt.bar(courses, values, color= 'red', width=0.4) #'maroon'
#
plt.bar(genders, values, color=['orange','orange'],width=0.4,yerr=std_err,error_kw=error_params,tick_label=['Female','Male']) #'maroon'
plt.legend(["Beauty"], title='Score of female and male',loc='best',facecolor='g',fontsize=16)  # empty is also ok
plt.ylim(0, 12)
# plt.xlim(0,1)
plt.xlabel("Gender")
plt.ylabel("score values of f and m")
plt.title("Score difference between female and male")
        #
        # plt.legend()
# plt.show()
# tdaveragetesttotalvv = np.zeros(len(tdaveragetesttotal))
k=len(tdaveragetesttotal)
# tdaveragetesttotalvv=[]   #one way of make an all 8 array.
# for i in range(k):
#    tdaveragetesttotalvv.append(8)

tdaveragetesttotalvv=np.zeros(k)
tdaveragetesttotalvv.fill(8)  #another way of make an all 8 array.
# fig = plt.figure(1)
fig = plt.figure(1)
plt.hist(tdaveragetesttotal,bins=30)
# 记住下面的作图参数xlabel, xlim, legend,title 等。
plt.xlabel('Index in x axis')
plt.ylabel('Score Values in y axis')
plt.title('The scores distribution as histogram', fontsize=22, color='blue')
plt.ylim(0, 26)
plt.xlim(0, 16)
# legend = plt.legend([tdaveragetesttotal, p2], ["CH", "US"], facecolor='blue')
plt.legend(["Frequency"], title='Frequency of score distribution',loc='best',facecolor='red',fontsize=16)  # empty is also ok
# plt.show()

fig = plt.figure(3)
plt.subplot(1,2,1)
plt.ylim(0, 12)
plt.xlim(0, 16)
plt.xlabel('Index in x axis')
plt.ylabel('Score Values in y axis')
plt.title('The score distribution of the sample', fontsize=22, color='r')
plt.scatter(tdaveragetesttotalvv, tdaveragetesttotal, c='g', marker='*', label='average score of each person')
plt.legend(["Total Score"], title='Average score of female and male',loc='best',facecolor='blue',fontsize=12)  # empty is also ok
plt.yticks(np.arange(0, 12, 0.5))  #set up step size

plt.subplot(1,2,2)
plt.ylim(0, 12)
plt.xlim(0, 16)
plt.xlabel('Score of each person')
plt.ylabel('Average score of the total sample')
plt.title('The mean score of the sample', fontsize=22, color='r')
tdaveragetesttotalvv.fill(averagescore)
plt.scatter( tdaveragetesttotal, tdaveragetesttotalvv,c='g', marker='+', label='average score of each person')
plt.axhline(y=averagescore,ls="-.",c="red")#添加水平直线
plt.legend(["Total Mean"], title='Average score of female and male',loc='best',facecolor='blue',fontsize=12)  # empty is also ok
plt.yticks(np.arange(0, 12, 0.5))  #set up step size
plt.show()   # this function conflict with score board show.



