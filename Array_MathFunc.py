arrOperation = np.array([[1, 2, 3], [4, 5, 6]])
print("Array square root :\n", np.sqrt(arrOperation))
print("Array square :\n", np.square(arrOperation))
print("Array power :\n", np.power(arrOperation, 3))

NegativeArr = np.array([[-1, -2, -3], [+4, -5, -6]])
print("Array absolute :\n", np.abs(NegativeArr))            #Removes the sign

print("Array exponential :\n", np.exp(arrOperation))        #e^x
print("Array logarithm :\n", np.log10(arrOperation))         #log base 10
print("sin of array :\n", np.sin(arrOperation))
print("cos of array :\n", np.cos(arrOperation))
