import pandas as pd
import numpy as np

#User defined functions

def moment(data, k):
  data_mean = sum(data)/len(data)
  return sum((x-data_mean)**k for x in data)/len(data)

def skewness(data):
  return moment(data, 3)/(moment(data, 2)**1.5)

def kurtosis(data):
  return moment(data,4)/(moment(data, 2)**2)
CD_data.isnull().sum(axis = 0)

#Give correct source path

CD_data = pd.read_csv("source path")

Catvar=CD_data.select_dtypes(include=['object']).columns
print(Catvar) #Categorical Variable
Numvar=CD_data.select_dtypes(include=['int', 'float']).columns
print(Numvar) #Numerical Variable
columns = ['NumberOfOvservation','UniqueValue','Missing Value','Missing%','Mean','Median', 'Mode','Stdev','Variance','Min','Max','Range','Kurtosis','Skewness','1%tile','2%tile','3%tile','4%tile','5%tile','6%tile','7%tile','8%tile','9%tile','10%tile','20%tile','30%tile','40%tile','50%tile','60%tile','70%tile','80%tile','90%tile','91%tile','92%tile','93%tile','94%tile','95%tile','96%tile','97%tile','98%tile','99%tile','100%tile']
index =Numvar
df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0.00)

d=len(Numvar)
for x in range(d):
    df_.iat[x,0]=len(CD_data[Numvar[x]])
    df_.iat[x,1]=len(CD_data[Numvar[x]].unique().tolist())
    df_.iat[x,2]=CD_data[Numvar[x]].isnull().sum(axis = 0)
    df_.iat[x,3]=CD_data[Numvar[x]].isnull().sum(axis = 0)/len(CD_data[Numvar[x]])
    df_.iat[x,4]=statistics.mean(CD_data[Numvar[x]])
    df_.iat[x,5]=statistics.median(CD_data[Numvar[x]])
    df_.iat[x,6]=statistics.mode(CD_data[Numvar[x]])
    df_.iat[x,7]=statistics.stdev(CD_data[Numvar[x]])
    df_.iat[x,8]=statistics.variance(CD_data[Numvar[x]])
    df_.iat[x,9]=min(CD_data[Numvar[x]])
    df_.iat[x,10]=max(CD_data[Numvar[x]])
    df_.iat[x,11]=max(CD_data[Numvar[x]])
    df_.iat[x,12]=kurtosis(CD_data[Numvar[x]])
    df_.iat[x,13]=skewness(CD_data[Numvar[x]])
    df_.iat[x,14]=np.percentile(CD_data[Numvar[x]], 1)
    df_.iat[x,15]=np.percentile(CD_data[Numvar[x]], 2)
    df_.iat[x,16]=np.percentile(CD_data[Numvar[x]], 3)
    df_.iat[x,17]=np.percentile(CD_data[Numvar[x]], 4)
    df_.iat[x,18]=np.percentile(CD_data[Numvar[x]], 5)
    df_.iat[x,19]=np.percentile(CD_data[Numvar[x]], 6)
    df_.iat[x,20]=np.percentile(CD_data[Numvar[x]], 7)
    df_.iat[x,21]=np.percentile(CD_data[Numvar[x]], 8)
    df_.iat[x,22]=np.percentile(CD_data[Numvar[x]], 9)
    df_.iat[x,23]=np.percentile(CD_data[Numvar[x]], 10)
    df_.iat[x,24]=np.percentile(CD_data[Numvar[x]], 20)
    df_.iat[x,25]=np.percentile(CD_data[Numvar[x]], 30)
    df_.iat[x,26]=np.percentile(CD_data[Numvar[x]], 40)
    df_.iat[x,27]=np.percentile(CD_data[Numvar[x]], 50)
    df_.iat[x,28]=np.percentile(CD_data[Numvar[x]], 60)
    df_.iat[x,29]=np.percentile(CD_data[Numvar[x]], 70)
    df_.iat[x,30]=np.percentile(CD_data[Numvar[x]], 80)
    df_.iat[x,31]=np.percentile(CD_data[Numvar[x]], 90)
    df_.iat[x,32]=np.percentile(CD_data[Numvar[x]], 91)
    df_.iat[x,33]=np.percentile(CD_data[Numvar[x]], 92)
    df_.iat[x,34]=np.percentile(CD_data[Numvar[x]], 93)
    df_.iat[x,35]=np.percentile(CD_data[Numvar[x]], 94)
    df_.iat[x,36]=np.percentile(CD_data[Numvar[x]], 95)
    df_.iat[x,37]=np.percentile(CD_data[Numvar[x]], 96)
    df_.iat[x,38]=np.percentile(CD_data[Numvar[x]], 97)
    df_.iat[x,39]=np.percentile(CD_data[Numvar[x]], 98)
    df_.iat[x,40]=np.percentile(CD_data[Numvar[x]], 99)
    df_.iat[x,41]=np.percentile(CD_data[Numvar[x]], 100)
    
    
CD_orgnl=CD_data



