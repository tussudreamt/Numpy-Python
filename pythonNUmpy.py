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

#03-07-2026
#Array attributes

arrndim = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])   #ndim    tells you how many dimesnions (axes) the array have
print(arrndim, end="\n")
print("array dimension are: ", arrndim.ndim)

arrshape1 = np.array([[1, 2, 3], [5, 6, 7], [4, 5, 6], [7, 8, 9]])               #shape   tells you how many elements in each dimension
print(arrshape1, end="\n")
print("array shape is: ", arrshape1.shape)

arrshape2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])               #shape   tells you how many elements in each dimension
print(arrshape2, end="\n")                              #(2, 2, 2)  2-outermost block, 2 - rows, 2 - columns
print("array shape is: ", arrshape2.shape)              #(no. of blocks , ROWS, COLUMNS )

arrsize = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[2, 3, 4], [5, 6, 7], [8, 9, 10]]])               #size    tells you how many total elements in the array
print(arrsize, end="\n")                                #2block size = (rows x columns) * no of blocks = (3x3)*2 = 18
print("array size is: ", arrsize.size, end="\n")              

arrdtype = np.array([1, 2, 3], dtype="f")               #dtype   tells you the data type of the array elements
print(arrdtype, end="\n")
print("array data type is: ", arrdtype.dtype)


arritemsize1 = np.array([1, 2, 3], dtype=np.int16)               #itemsize   tells you the size in bytes of each element in the array
arritemsize2 = np.array([1, 2, 3], dtype=np.int32)
arritemsize3 = np.array([1, 2, 3], dtype=np.int64)
arritemsize4 = np.array([1, 2, 3], dtype=np.float32)
arritemsize5 = np.array([1, 2, 3], dtype=np.float64)
print("array 1 item size is: ", arritemsize1.itemsize, "bytes")
print("array 2 item size is: ", arritemsize2.itemsize, "bytes")
print("array 3 item size is: ", arritemsize3.itemsize, "bytes")
print("array 4 item size of float is: ", arritemsize4.itemsize, "bytes")
print("array 5 item size of float is: ", arritemsize5.itemsize, "bytes")
print(end="\n")

arrnbytes1 = np.array([[1, 2, 3],[3, 5, 3]], dtype=np.int16)               #nbytes   tells you the total size in bytes of the array
arrnbytes2 = np.array([1, 2, 3], dtype=np.int32)
arrnbytes3 = np.array([1, 2, 3], dtype=np.int64)
arrnbytes4 = np.array([1, 2, 3], dtype=np.float32)
arrnbytes5 = np.array([1, 2, 3], dtype=np.float64)
print("array 1 total size is: ", arrnbytes1.nbytes, "bytes")
print("array 2 total size is: ", arrnbytes2.nbytes, "bytes")
print("array 3 total size is: ", arrnbytes3.nbytes, "bytes")
print("array 4 total size of float is: ", arrnbytes4.nbytes, "bytes")
print("array 5 total size of float is: ", arrnbytes5.nbytes, "bytes\n")


#array indexing
#array indexing means accesing an array element by its index number

arrindex1 = np.array([1, 2, 3, 4, 5])                                     #1D array indexing
arrindex2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])                   #2D array indexing
arrindex3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])                #3D array indexing

#1D array : front(0 - (N-1)) , Back(N - 1)
#2D array :     0   1              arrname[row, column]
#           0  |9   8| -2 
#           1  |6   7| -1
#              -2  -1

#3D array :   arrname[block, row, column]
#              0   1                    0   1  
#          0  |1   2| -2            0  |5   6| -2
#          1  |3   4| -1            1  |7   8| -1
#             -2   -1                  -2  -1
#            block 1                  block 2
print("2D array indexing : ", arrindex2[[1, 2]])    #Bracket matters for accessing single or multiple elements
                                                    

#Modifying array element
arrindex1[4] = 99
print("Modified 1D array : ", arrindex1)
print(end="\n")

#Fancy Indexing let you access multiple elements at once
print("array 1D fancy indexing : ", arrindex1[[0, 2, 4]])    #single bracket single element, double bracket multiple elements
print("array 2D fancy indexing : ", arrindex2[[0, 1], [1, 2]])    
print(end="\n")

#Boolean Indexing let you access multiple elements at once using boolean values
arrbool = np.array([1, 2, 3, 4, 5])
print(arrbool > 2)    #return boolean array
print("Boolean array indexing : ", arrbool[arrbool > 2])

#ERROR due TO :    1.. Index out of Range, 2.. Invalid Indexing, 3.. Invalid Data Type, 4.. Invalid Shape, 5.. Invalid 