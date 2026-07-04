import numpy as np
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
