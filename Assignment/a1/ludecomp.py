import numpy
if __name__ == "__main__" :
    a = numpy.ndarray((3,3))
    b = numpy.ndarray((3,1))
    print("Enter elements of matrix a \n")
    for i in range(0,3) :
        for j in range(0,3) :
            a[i][j] = int(input())
    print("Enter elments of matrix b \n")
    for i in range(0,3) :
        b[i][0] = int(input())
    l = numpy.ndarray((3,3))
    u = numpy.ndarray((3,3))
    for i in range(0,3) :
        for j in range (0,3) :
            if j < i :
                u[i][j] = 0
            elif i == j :
                l[i][j] = 1
            else :
                l[i][j] = 0
    for i in range(0,3) :
        u[0][i] = a[0][i]
    l[1][0] = a[1][0]/u[0][0]
    l[2][0] = a[2][0]/u[0][0]
    u[1][1] = a[1][1] - l[1][0]*u[0][1]
    if u[1][1] != 0 :
        u[1][2] = a[1][2] - l[1][0]*u[0][2]
        l[2][1] = (a[2][1] - l[2][0]*u[0][1])/u[1][1]
        u[2][2] = a[2][2] - l[2][0]*u[0][2] - l[2][1]*u[1][2]
        print("l = ",l,"\n")
        print("u = ",u,"\n")
        l1 = numpy.ndarray((3,3))
        u1 = numpy.ndarray((3,3))
        y1 = numpy.ndarray((3,3))
        l1 = numpy.linalg.inv(l)
        u1 = numpy.linalg.inv(u)
        y1 = numpy.dot(u1,l1)
        x = numpy.dot(y1,b)
        print("Solution to system of simultaneous equations is : \n")
        print(x)
    else :
        print("System of equations is inconsistent. It does not have unique solution. \n")
