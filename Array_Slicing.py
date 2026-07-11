import numpy as np
#09-07-2026
#Slicing of array
                                #arr[start(inclusive) : stop(exclusive) : step]
arrslice1 = np.array([1, 2, 3, 4, 5])
print("Sliced array : ", arrslice1[1:4:1])  #[2, 3, 4]
print("Omit start :", arrslice1[:4:1])      #[1, 2, 3, 4]
print("Omit end :", arrslice1[1::1])        #[2, 3, 4, 5]
print("Omit Both :", arrslice1[::1])        #[1, 2, 3, 4, 5] print whole array
print("Using step :", arrslice1[::2])       #[1, 3, 5]

#                    -5 -4 -3 -2 -1
#Negative slicing    [1, 2, 3, 4, 5]
#                     0  1  2  3  4

print("Negative slicing :", arrslice1[-3:-1])   #[3, 4]
print("Negative slicing with step :", arrslice1[-1:-4:-2])  #[5, 3]
print("Reverse an array:", arrslice1[::-1])  #[5, 4, 3, 2, 1] reverse the array


        #2D array slicing 
"""               
            Column
        0   1   2   3
    0   +---+---+---+
        |10 |20 |30 |
    1   +---+---+---+
        |40 |50 |60 |
    2   +---+---+---+
        |70 |80 |90 |
    3   +---+---+---+

        arr[row_slice, Column_slice]
       
 """
#Note:  0 to 1 means 1row and 1column, 0 to 2 means 2row and 2column, 1 to 2 means 1row and 1column


arrslice2d = np.array([[10, 20 , 30], [40, 50, 60], [70, 80, 90]])
#syntax : arr[ ROWstrt : Rowend : ROWstep, COLstrt : COLend : COLstep]
print("1st 2 row :\n", arrslice2d[0:2:1, :])
print("1st 2 column :\n", arrslice2d[:, :1:1])
print("Middle of 2D array :\n", arrslice2d[1:2:1, 1:2:1])
print("\n")

#3d Array arr[block_slice, row_slice, column_slice]
arrslice3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(arrslice3d, "\n")
print("Sliced 3D array :\n", arrslice3d[1:2:1, :, :])

#Slice assignment
arrsliceassign = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arrsliceassign[0:2, 0:3] = 99
print("Slice assignment :\n", arrsliceassign)

#Common error: 1-stop excluded, 2-Invalid step, 3-Invalid slicing, 4-Invalid shape, 5-Invalid data type, 6-Index out of range
