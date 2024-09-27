import pandas as pd
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

#mo file csv
data_frame = pd.read_csv("ChirpsPerMinute.csv")
#goi ham trainning
linear_regression=linear_model.LinearRegression()
#cho input label
linear_regression.fit(data_frame[['Cricket_chirps_per_Minute']],data_frame['Temperature'])
p=linear_regression.predict([[180]])
w = linear_regression.coef_
b = linear_regression.intercept_

print("Du doan nhiet do:",p)
#ve do thi
plt.scatter(data_frame['Cricket_chirps_per_Minute'],data_frame['Temperature'])
#plt.plot(data_frame['Cricket_chirps_per_Minute'],data_frame['Temperature'])
plt.xlabel("Cricket Chirps per Minute")
plt.ylabel('Temperature')
#x_values = np.linspace(data_frame['Cricket_chirps_per_Minute'].min(), data_frame['Cricket_chirps_per_Minute'].max(), 100)
x_values = np.linspace(data_frame['Cricket_chirps_per_Minute'].min(), data_frame['Cricket_chirps_per_Minute'].max(), 2)
# Tính giá trị y dựa trên phương trình đường thẳng
y_values = w * x_values + b

# Vẽ đường thẳng plt.plot(x_values, y_values, color='blue', label='Đường hồi quy')
# plt.plot(x, y, *args, **kwargs)
plt.plot(x_values, y_values, color='blue', label='Đường hồi quy')
plt.show()