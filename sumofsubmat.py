ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def sumofsubm(n,k):
    a = len(n)-(k)
    for i in range(a+1):
        for j in range(a+1):
            sum = 0
            for p in range(i,k+i):
                for q in range(j,k+j):
                    print(p,q)
                    sum = sum + ls[p][q]
            print(sum, " ")
    print(a)
        
sumofsubm(ls,2)
