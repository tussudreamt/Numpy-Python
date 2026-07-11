import numpy as np
#Array Reshape : only change the shape of the array, not the data
#Not even change the original array, it return a new array with new shape

arrReshape = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Original array :\n", arrReshape)

print("Reshaped array :\n", arrReshape.reshape(4, -2))  #reshape(rows, columns) rows*colm = total elements
                                                        # -1 means 2 & -2 means 3
                                                        
print("flattened array :\n", arrReshape.flatten(order="F"))   #Return a copy of the array collapsed into one dimension. order = 'C' means row-wise, order = 'F' means column-wise, order = 'A' , order = 'K' 

print("Raveled array :\n", arrReshape.ravel(order="C"))      #Return a copy of the array collapsed into one dimension. order = 'C' means row-wise, order = 'F' means column-wise, order = 'A' , order = 'K' 
arrReshape[0, 0]= 99
print("First element :\n", arrReshape.ravel(order="C")[0])

print("Transposed array :\n", arrReshape.T) #transpor or T
