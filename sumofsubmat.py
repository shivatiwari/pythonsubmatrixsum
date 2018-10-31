ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def sumofsubm(n,k):
    if k > len(n):
        return
    else:
        for i in range(n-k+1):
            for j in range(n-k+1):
                sum = 0
                for p in range(i,k+i):
                    for q in range(j,k+j):
                        sum = sum + ls[p][q]
                print(sum, " ")
        print()
        
sumofsubm(ls,2)
