#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        sum=0
        maxi=0
        d={"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        for i in range(len(S)):
            if i==len(S)-1:
                sum += d[S[i]]
                continue
            if d[S[i]]>= d[S[i+1]]:
                sum+=d[S[i]]
            else:
                sum-=d[S[i]]
        return sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends
