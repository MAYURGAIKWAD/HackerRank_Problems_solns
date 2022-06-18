#User function Template for python3
import math
class Solution:
    

	def checkTriplet(self,arr, n):
    	# code here
    	d={}
    	for i in arr:
    	    d[i]=1
	    maxn=max(arr)
	    arr.sort()
	    for i in range(n):
	        for j in range(i+1, n):
	            t1=  math.sqrt(arr[i]*arr[i]+ arr[j]*arr[j])
	            if t1>maxn:
	                break
	           # print(arr[i], arr[j], t1)
	            if ((int(t1)==t1) and (t1 in d.keys())):
	               # print(arr[i], arr[j], t1)
	                return True
        return False
	                

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
