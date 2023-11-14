import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'], 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5,
np.nan, 8, 19], 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'qualify': ['yes', 'no', 'yes',
'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#Create and display a DataFrame from the above dictionary data which has index labels.
data=pd.DataFrame(exam_data,index=labels)
print(data)
print()

#Select and display the rows where the number of attempts in the examination is greater than 2.
print(data[data['attempts']>2])
print()

#Count the number of rows and columns of the DataFrame.
print(data.shape)
print()

#Select the rows where the score is missing, i.e. is NaN.
print(data[data['score'].isnull()])
print()

#Change the score in row 'd' to 11.5
data.loc['d','score']=11.5 #.loc is useful when working with DataFrames that have custom row and column labels. 
#It allows you to perform label-based indexing in a clear and explicit manner.
#df.loc[row_labels, column_labels]
print(data)
print()

#Calculate the sum of the examination attempts by the students.
print(data['attempts'].sum())
print()

#Append a new row 'k' to DataFrame with given values for each column.
#Values for each column will be:
#name : ‘Suresh’, score: 15.5, attempts: 1, qualify: ‘yes’; label: ‘k’
#Now delete the new row and return the original data frame.
new_row = pd.DataFrame({'name': ['Suresh'], 'score': [15.5], 'attempts': [1], 'qualify': ['yes']}, index=['k'])
data = pd.concat([data, new_row])
print(data)
print()
data=data.drop('k')
print(data)
print()

#Sort the data frame first by 'name' in descending order, then by 'score' in ascending order.
print(data.sort_values('name',ascending=False))
print()
print(data.sort_values('score'))
print()
