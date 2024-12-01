'''
To do statistic job of the data collected.
'''
import math

import numpy as np
import analysis as alsis
from scipy.stats import ks_2samp
from numpy.random import poisson
from scipy.stats import normaltest
import scipy.stats as stats
from scipy.stats import kstest
# from scipy.stats.mstats_basic import Ttest_indResult
# from scipy.stats import ttest_ind
# from scipy.stats import kstest, describe
# from scipy.stats import normaltest as norm
# from numpy.random import seed
#set seed (e.g. make this example reproducible)
# seed(0)

group1 = np.array(alsis.listfemale )
group2 = np.array(alsis.listmale)


res=stats.ttest_ind(a=group1, b=group2, equal_var=True)
# print(res)
print('Results of ttest of beauty between female and male:  ',res.pvalue)


print('The average score of all average indexes:  ',sum(alsis.tdaveragetesttotal)/alsis.k,'    ',alsis.k)

datapossion = poisson(sum(alsis.tdaveragetesttotal)/alsis.k,alsis.k)
res1= ks_2samp(alsis.tdaveragetesttotal,datapossion)
print('Poisson test:  ',res1.pvalue)

res2=normaltest(alsis.tdaveragetesttotal)
print('Results of normal test of total average:   ',round(res2.pvalue,2))
if res2.pvalue> 0.05:
    print('Most probably it is normal distribution of the data of average score')
else:
    print('Most probably it is not normal distribution of the data of average score')

# res3=kstest(alsis.tdaveragetesttotal,'norm') # if p<0.05 ,reject null hypothesis: x comes from a normal distribution
# print(res3.pvalue)   # result is weird, self-controdiction!!!

gender_type = alsis.df.gender
average_index = alsis.df.STATISTICSIE

sum1=0
sum2=0
m=0
n=0
listfemalemean=[]
listmalemean=[]
for i in range(alsis.kk):
    if gender_type[i] == "f":
          listfemalemean.append(average_index[i])
          sum1 += average_index[i]
          m += 1
    else:
        listmalemean.append(average_index[i])
        sum2 = sum2+ average_index[i]
        n += 1
ksresult1 = kstest(average_index, 'norm')   #  https://www.runoob.com/scipy/scipy-significance-tests.html  tdaveragetesttotal
print('Distribution test pvalue kstest:  ',ksresult1.pvalue)

group1 = np.array(listfemalemean )
group2 = np.array(listmalemean)
print('Female average score list ',listfemalemean,'\n','Male average score list ',listmalemean) # '\n'  change line)
print('Female average score mean: ',round(sum(listfemalemean)/len(group1),2),'\n','Male average score mean: ',round(sum(listmalemean)/len(group2),2) )# '\n'  change line)
std_f=np.std(listfemalemean)
std_m=np.std(listmalemean)
print('Standard deviation of female and male in average indexes are:   ',  round(std_f,2),round(std_m,2))
res_ave=stats.ttest_ind(a=group1, b=group2, equal_var=True)
# print(res)
print('Results of ttest of total average score between female and male:  ',round(res_ave.pvalue,2))