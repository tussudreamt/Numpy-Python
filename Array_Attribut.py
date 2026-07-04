import numpy as np
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
