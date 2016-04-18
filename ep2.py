
class IllegalState(Exception):
	pass

class IllegalArgument(Exception):
	pass

# return true if a matrix is square,
# 		 false otherwise
#
# throws IllegalArgumentException if matrix does not have
# 		 the same number of elements for each row
def isSquareMatrix(matrix):
	rows = len(matrix)
	
	mit = iter(matrix)
	first = len(next(mit))
	while(hasNext(mit)):
		others = len(next(mit))
		if(others != first):
			raise IllegalArgument('Expected a matrix <%s>', matrix)
	
	return first == rows

# return a vector that is the result between
# 		 the product of a square matrix with
# 		 another vector
def product(matrix, v):
	if(not isSquareMatrix(matrix)):
		raise IllegalArgument('Expected square matrix <%s>', matrix)

	if(len(matrix) != len(v)):
		raise IllegalArgument('Expected vector to have same size as '+
				'matrix. vector.size=%d, matrix.size=%d', len(matrix), len(vector))
	#
	#TODO: implement me
	return 0

# return true if both vectors are the same,
# 		 false otherwise
#
# throws IllegalArgumentException if both vectors
#		 does not have same size
def equals(v1, v2):
	if(len(v1) != len(v2)):
		raise IllegalArgument('Expected vectors of same ' +
			'size v1.size=%d, v2.size=%d', len(v1), len(v2))
	#
	# TODO: implement me
	return false


#Ax=d
#
# [2, 1, 0][x1]   [4]
# [1, 2, 1][x2] = [8]
# [0, 1, 2][x3]   [8]
a = [0, 1, 1]
b = [2, 2, 2]
c = [1, 1, 0]
d = [4, 8, 8]


u = [float(b[0])]
l = [0]

for i in range(1, 3):
	li = a[i]/u[i-1]
	ui = b[i]-li*c[i-1]
	u.append(ui)
	l.append(li)

print "u=" + str(u)
print "l=" + str(l)

#Ly=d
y = [float(d[0])]
for i in range(1, 3):
	yi = d[i]-l[i]*y[i-1]
	y.append(yi)

#Ux=y:
x = [0, 0, y[2]/u[2]] #<= this should be xn
for i in reversed(range(0, 2)):
	print i
	xi = y[i]-c[i]*x[i+1]/u[i]
	x.insert(i, xi)

print "x=" + str(x)

# Main

## Creates a list containing 5 lists initialized to 0
#Matrix = [[0 for x in range(5)] for x in range(5)] 