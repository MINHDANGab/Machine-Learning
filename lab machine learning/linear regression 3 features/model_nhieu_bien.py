import pandas as pd
import numpy as np
from sklearn import linear_model
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#doc file csv
data_frame = pd.read_csv("housing-dataset.csv",header= None,names=["AREA","BEDROOM","PRICE"])
print(data_frame.columns)
#goi ham linear regression
linear_regression = linear_model.LinearRegression()
#train model linear_regression.fit(dataset,label)
linear_regression.fit(data_frame[['AREA','BEDROOM']],data_frame['PRICE'])
# w=[w1,w2,...,wn] = coef_  b= bias = intercept_
w= linear_regression.coef_
b= linear_regression.intercept_
print(w)
print(b)
p = linear_regression.predict([[4000,6]])
print("Giá nhà dự đoán là:",p)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dữ liệu để vẽ đồ thị
area = data_frame['AREA']
bedroom = data_frame['BEDROOM']
price = data_frame['PRICE']

# Vẽ các điểm dữ liệu ban đầu
ax.scatter(area, bedroom, price, color='red', label='Dữ liệu thực tế')

# Tạo lưới giá trị cho diện tích và số phòng ngủ để vẽ mặt phẳng hồi quy
area_grid, bedroom_grid = np.meshgrid(np.linspace(area.min(), area.max(), 20),
                                      np.linspace(bedroom.min(), bedroom.max(), 20))
price_grid = w[0] * area_grid + w[1] * bedroom_grid + b

# Vẽ mặt phẳng hồi quy
ax.plot_surface(area_grid, bedroom_grid, price_grid, color='blue', alpha=0.5, rstride=100, cstride=100)

# Đặt tiêu đề và nhãn cho các trục


# Hiển thị đồ thị
plt.show()
