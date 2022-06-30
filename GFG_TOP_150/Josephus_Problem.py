#{ 
#Driver Code Starts
import math



 # } Driver Code Ends
#Complete this function

class Solution:
    def josephus(self,n,k):
        arr=[i for i in range(1,n+1)]
        start=0
        while len(arr)!=1:
            nkill=(start+k-1)%len(arr)
            if nkill==len(arr)-1:
                start=0
                arr=arr[:nkill]
                continue
            else:
                start=nkill
            arr=arr[:nkill]+arr[nkill+1:]
        return int(arr[0])

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(Solution().josephus(n,k))
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends
