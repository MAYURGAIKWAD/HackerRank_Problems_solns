#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		ans=[0]*N
		for i in range(N):
		    ans[i]=arr[i]
        maxq=N//K
        lastr=N%K
        # print("Lastr= ", lastr)
        j=0
        while j<N:
            if j<N and j>=maxq*K:
                # print(j)
                # print((j//K)*K+lastr-1-j%K)
                arr[j]=ans[(j//K)*K+lastr-j%K-1]
                j+=1
                pass
            
            else:
                arr[j]=ans[(j//K)*K+K-1-j%K ]
                # print(ans)
                j+=1
        # print(ans)
        # arr=ans
        return ans
                
            
        
		        

#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends
