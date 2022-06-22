#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		ans=""
		d={}
		for i in S:
		    if i in d.keys():
		        continue
		    else:
		        d[i]=1
		        ans+=i
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends
