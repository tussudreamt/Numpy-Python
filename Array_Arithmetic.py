arrA = np.array([[1, 2, 3],
                  [4, 5, 6]])
arrB = np.array([[7, 8, 9],
                  [10, 11, 12]])
print("Array Addition :\n", np.add(arrA, arrB))             #also can use arrA + arrB
print("Array Subtraction :\n", np.subtract(arrA, arrB))     #also can use arrA - arrB
print("Array Multiplication :\n", np.multiply(arrA, arrB))  #also can use arrA * arrB
print("Array Division :\n", np.divide(arrA, arrB))          #also can use arrA / arrB
print("Array Power :\n", np.power(arrA, 2))                 #also can use arrA ** 2
print("Array Square Root :\n", np.sqrt(arrA))               
print("Array Logarithm :\n", np.log(arrA))                  #also can use np.log10(arrA) for log base 10
print("floor divide: \n", np.floor_divide(arrB, arrA))  #strictly divide
