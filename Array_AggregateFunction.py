import numpy as np
#Aggregation function
arrayAggre = np.array([1, 2, 5, 4, 3])
print("sum of all element :", np.sum(arrayAggre))
print("Mean of all element :", np.mean(arrayAggre))
print("median of all element :", np.median(arrayAggre)) #Middle value after sorting #3
print("Variance of array :", np.var(arrayAggre))
print("Standard deviation :", np.std(arrayAggre)) #spread of data
print("Min value of array :", np.min(arrayAggre))
print("Max value of array :", np.max(arrayAggre))
print("Index of smallest element :", np.argmin(arrayAggre)) #Index of smallest element
print("Index of largest element :", np.argmax(arrayAggre))

#for 2d array
arragg2d = np.array([[1, 2, 3],
                     [5, 6, 7]])
print("Array sum :", np.sum(arragg2d, axis=0)) 
print("Array sum :", np.sum(arragg2d, axis=1))
#this applies to  mean, min, max, std, var
print("Index of min value :", np.argmax(arragg2d)) #for 2d array it returns index number

#axis - tells the numpy along which direction to perform operation
#axis=0(one result for each column)       axis=1(one result for each row) 
