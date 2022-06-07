class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        A=sorted(a)
        B=sorted(b)
        ans=0
        for i in range(n):
            ans+=A[i]*B[n-i-1]
        return ans
