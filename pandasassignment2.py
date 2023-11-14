import pandas as pd

#Load and Print first ten rows of the dataset.
data=pd.read_csv('Automobile_data.csv')
print(data.head(10))

#Drop a column.
data=data.drop(columns='length')

#Print the last five rows.
print(data.tail())

#Print All Toyota Cars details.
print(data[data['company']=='toyota'])

#Count total cars per company
print(data['company'].value_counts())

#Find each company’s Highest priced car.
print(data.loc[data.groupby('company')['price'].idxmax()])

#Get average mileage of all the cars.
print(data['average-mileage'].mean())

#Sort all cars by Price column.
print(data.sort_values('price'))