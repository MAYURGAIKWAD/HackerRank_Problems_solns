
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code 
        ans=[]
        maxsofar=A[N-1]
        if N==1:
            return A[0]
        for i in range(N-1,-1,-1):
            if i==N-1:
                ans.append(A[i])
                maxsofar=A[i]
                continue
            if A[i]>=maxsofar:
                maxsofar=A[i]
                ans.append(A[i])
        ret=[]
        for i in range(len(ans)-1,-1,-1):
            ret.append(ans[i])
            
        return ret

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
