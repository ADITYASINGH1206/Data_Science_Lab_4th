import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)





# arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# arr4 = arr1 * arr2
# print(arr4)
# arr3 = arr1 @ arr2 
# print(arr3) 

# arr5 = np.cross(arr1, arr2)
# print(arr5)

# # PANDAS 
import pandas as pd
# data = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9], [np.nan, 11, 12]])
# df = pd.DataFrame(data)
# print(df)
# mean = df.mean()
# df.fillna(value=mean, inplace=True)
# print(df)
# df = df.drop([0,1,2],axis=0)
# print("DROPPING ROWS")
# print(df)

# Mini practice 









data = {
    "Name" : ["Aditya","Gupta","Sharad","Bhatt"],
    "Age" : [20,19,19,42],
    "Score" : [75,100,90,90],
    "Heigth" : [193,183,190,156]
}

dfs = pd.DataFrame(data)
dfs.sort_values(by="Score",ascending = True, inplace= True)
print(dfs)
print("Describe")
l = dfs.describe()
print(l)