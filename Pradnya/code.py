# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
print("\nType of data: \n\n", type(data))
census = np.concatenate((data, new_record))
print(census)


# --------------
#Code starts here
age = census[:,[0]]
print(age)
max_age = age.max()
print("max age:",max_age)
min_age = age.min()
print("min age:",min_age)
age_mean = np.mean(age)
print("mean:", age_mean)
age_std = np.std(age)
print("std dev:", age_std)


# --------------
#Code starts here
#race = census[:,2]
race_0 = census[census[:,2]==0]

race_1 = census[census[:,2]==1]

race_2 = census[census[:,2]==2]

race_3 = census[census[:,2]==3]

race_4 = census[census[:,2]==4]


#length of race arrays
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

#minimum lemgh
min_len_race = min(len_0,len_1,len_2,len_3,len_4)
print(min_len_race)
#minority_race
if(len(race_0) == min_len_race):
    minority_race = 0
elif(len(race_1) == min_len_race):
    minority_race = 1
elif(len(race_2) == min_len_race):
    minority_race = 2
elif(len(race_3) == min_len_race):
    minority_race = 3
elif(len(race_4) == min_len_race):
    minority_race = 4

print(minority_race)




# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]
working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np
#subset of highly educated 
high = census[census[:,1] > 10]
#subset of low educated 
low = census[census[:,1] <= 10]
#calculate average pay for both
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)


