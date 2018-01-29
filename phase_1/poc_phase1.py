import sys
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

url="/home/vishal/Documents/healtCareDataSet.data"
names=['cigratePerDay','weight','height','waterIntakePerDay','exerciseInHoursperDay','healtConditions']

#it will match the names and the csv content row and column put together
dataset=pandas.read_csv(url,names=names)

#put the dataSet into an array
array=dataset.values

#it will take all value before 5th element 0,1,2,3,4,5..everything before 5
#X=array[0,0:4]
X=array[:,0:5]
#health condition is stored
Y=array[:,5]


lr=LogisticRegression()
lr.fit(X, Y)


T_validation=[[10,65,6,5,1]]
predictions = lr.predict(T_validation)
print(type(predictions))
print(predictions)