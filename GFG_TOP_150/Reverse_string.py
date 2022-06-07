
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        prev=len(S)
        ans=""
        for i in range(len(S)-1, -1,-1):
            # print(i)
            if S[i]==".":
                ans+=S[i+1:prev]+"."
                prev=i
            if i==0:
                ans+=S[0:prev]
        return ans
                    
            
        # code here 

#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends
