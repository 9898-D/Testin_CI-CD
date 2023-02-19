def bubble(arry):
    n=len(arry)
    for i in range(n):
        for j in range(0,n-i-1):
            if arry[j] > arry[j+1]:
                arry[j],arry[j+1]=arry[j+1],arry[j]
                
    return arry

if __name__ == "__main__":
    le=bubble([20,4,1,15,50,35])
    print(le)
