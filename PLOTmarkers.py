#-------------------------------------------------------------------------------------------------------------------
# Author : AKSHAY UDAY PADAMWAR
# Date: 25-08-2022
#-------------------------------------------------------------------------------------------------------------------


#importing libraries required for plotting
#
import matplotlib.pyplot as plt
import numpy as np
age=      np.array([30,32,34,36,38,40,42,44])
income =  np.array([24000,32000,42100,54720,87659,55777,34565,57643])
rent =    np.array([1200,2300,3400,3100,1500,1800,2200,1700])
insurance=np.array([300,500,200,0,532,645,853,353])
savings=  np.array([10000,14000,20000,230000,180000,30000,35000,360000])


plt.subplot(2,2,1)
plt.plot(age,income,label="INCOME",marker='*')
plt.legend()

plt.subplot(2,2,2)
plt.plot(age,rent,label="RENT",marker='.')
plt.legend()

plt.subplot(2,2,3)
plt.plot(age,insurance,label="INSURANCE",marker='*')
plt.legend()

plt.subplot(2,2,4)
plt.plot(age,savings,label="SAVINGS",marker='*')
plt.legend()

plt.show()
