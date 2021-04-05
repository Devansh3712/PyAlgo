"""
module for calculating
nth fibonacci number
"""

def fibonacci(n: int):
	
	matrix = [[1, 1],
		[1, 0]]

	if (n == 0):
		return 0

	power(matrix, n - 1)
		
	return matrix[0][0]
	
def multiply(matrix: list, matrix2: list):
	
	num1 = (matrix[0][0] * matrix2[0][0] + matrix[0][1] * matrix2[1][0])
	num2 = (matrix[0][0] * matrix2[0][1] + matrix[0][1] * matrix2[1][1])
	num3 = (matrix[1][0] * matrix2[0][0] + matrix[1][1] * matrix2[1][0])
	num4 = (matrix[1][0] * matrix2[0][1] + matrix[1][1] * matrix2[1][1])
	
	matrix[0][0] = num1
	matrix[0][1] = num2
	matrix[1][0] = num3
	matrix[1][1] = num4

def power(matrix, n):

	if( n == 0 or n == 1):
		return

	matrix2 = [[1, 1],
		[1, 0]]
		
	power(matrix, n // 2)
	multiply(matrix, matrix)
		
	if (n % 2 != 0):
		multiply(matrix, matrix2)

"""
PyAlgo
Devansh Singh, 2021
"""
