#Numpy - numerical python used for scientific computing, data science and machine learning appl
#provide N-dimensional arrayobject (ndarray)

#29-06-2026
import numpy as np
print(np.__version__)

arr0D = np.array(42)                                              #0-dimensional array    
arr1D = np.array([1, 2, 3])                                       #1-dimensional array so, 1 sqr bracket
arr2D = np.array([[4, 5, 6], [7, 8, 0]])                          #2-dimensional array so, 2 sqr bracket
arr3D = np.array([[[10, 11], [12, 13], [14, 15], [16, 17]]])      #3-dimensional nested array so, 3 sqr bracket

print("the dimension of array: ")
print(arr0D.ndim)                                       #ndim give the nesting of the array
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

print("The shape of array :")
print(arr0D.shape)
print(arr1D.shape)                                              #(3,)        3 - elements
print(arr2D.shape)                                              #(2, 3)      2 - rows, 3 - columns
print(arr3D.shape)                                              #(1, 4, 2)   1-outermost block, 4 - rows, 2 - columns


print(arr0D.size)                                   #give the number of element in array
print(arr2D.size)


float_arr = np.array([0.9, 1, 2], dtype="f")                    # dtype='' used to specify array element type
print(float_arr)
print(type(float_arr))


#30-06-2026
#Creating Array
objList = {1, 2, 3, "hello"}
arraList = np.array(objList, dtype=None)    #np.array()
print(arraList)

print("\n")
arrZeros = np.zeros([5, 5])                                       #give an array of size consisting of only 1s  
print("Array with all zeros\n", arrZeros)
print("\n")

arrOnes = np.ones((4, 4))                                      
print("Array with all 1s\n", arrOnes)
print("\n")

arrEmpty = np.empty((2, 3), dtype=float)                        #gives an empty array, help us to prevent garbage values
print("Empty paranthesis to prevent garbage value \n", arrEmpty)
print("\n")

arrFull = np.full((3, 3), 69, dtype="f")                         #np.full consist of the array with same value (size, value)
print("Consisting of same element 69 at every pos..\n", arrFull)
print("\n")

arrEye = np.eye(3, 3, 1)                  #(numROWS, numCOLM, diaOFFSET)
print('IT CREATES IDENTITY MATRIX OF 1S on diagonal\n', arrEye)
print("\n")

arrIdentity = np.identity(5)                #creates only square matrix 
print("Creates only square matrix\n", arrIdentity) #NO offset parameter
print("\n")

arrArange = np.arange(1, 13, 2)             #np.arange(start, stop, step) create evenly spaced array within specific range
print("Array with spaced value within specific range :\n", arrArange)           #similar to range() but return NP array
print("\n")

arrLinespace = np.linspace(1, 10, 5)            #create an array upto specifiend range with value have equal range  
print("Array of evely spaced value between startand end value :\n", arrLinespace)
print("\n")

arrLogspace = np.logspace(1, 10, 10, 5)
print("Array with evely spaced logarithmic scale :\n", arrLogspace)
print("\n")



