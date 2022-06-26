#User function Template for python3

class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		d={}
		top=[]
		ans=""
		for i in A:
		    if i not in d:
		        d[i]=1
		        top.append(i)
		        ans+=top[0]
	        else:
	            if d[i]==1:
	                top.remove(i)
	            if len(top)==0:
	                ans+="#"
                else:
                    ans += top[0]
                d[i]+=1
        return ans
		        
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends
