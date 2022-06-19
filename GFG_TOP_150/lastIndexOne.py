#User function Template for python3

def findElement( arr, n):
    maxsofar=[0]*n
    minsofar=[0]*n
    maxsofar[0]=arr[0]
    minsofar[n-1]=arr[n-1]
    for i in range(1,n):
        maxsofar[i]=max(maxsofar[i-1],arr[i])
    for i in range(n-2,-1,-1):
        minsofar[i]=min(minsofar[i+1],arr[i])
    for i in range(1,n-1):
        if arr[i]>=maxsofar[i-1] and arr[i]<= minsofar[i+1]:
            return arr[i]
    return -1
        
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
