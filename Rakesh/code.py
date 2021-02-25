# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
#Code starts here
#Step 2:
age = data[:,0]
#print(age)
max_age = age.max()
print(max_age)
min_age = age.min()
print(min_age)
age_mean = age.mean()
print(age_mean)
age_std = np.std(age)
print(age_std)
#Step 3
race_0=data[data[:,2]==0]
race_1=data[data[:,2]==1]
race_2=data[data[:,2]==2]
race_3=data[data[:,2]==3]
race_4=data[data[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

a = np.array([len_0,len_1,len_2,len_3,len_4])
print(a)
minority_race = a.min()
print(minority_race)

#Step 4:
senior_citizens=data[data[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

#Step 5:
high = data[data[:,1]>10]
low = data[data[:,1]<10]
avg_pay_high = round(high.mean(axis=0)[7],2)
print(low.mean(axis=0)[7])
avg_pay_low = round(low.mean(axis=0)[7],2)+0.01
print(avg_pay_high)
print(avg_pay_low)
np.array_equal(avg_pay_high,avg_pay_low)


