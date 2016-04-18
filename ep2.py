#Ax=d
#
# [2, 1, 0][x1]   [4]
# [1, 2, 1][x2] = [8]
# [0, 1, 2][x3]   [8]
a = [0, 1, 1]
b = [2, 2, 2]
c = [1, 1, 0]
d = [4, 8, 8]

#
# matrix size
n = 3


u = [float(b[0])]
l = [0]

for i in range(1, n):
	li = a[i]/u[i-1]
	ui = b[i]-li*c[i-1]
	u.append(ui)
	l.append(li)

print "u=" + str(u)
print "l=" + str(l)

#Ly=d
y = [float(d[0])]
for i in range(1, n):
	yi = d[i]-l[i]*y[i-1]
	y.append(yi)

print "y=" + str(y)

#Ux=y:
x = [0, 0, y[n-1]/u[n-1]] #<= this should be xn
for i in reversed(range(0, n-1)):
	xi = (y[i]-c[i]*x[i+1])/u[i]
	x.insert(i, xi)

print "x=" + str(x)