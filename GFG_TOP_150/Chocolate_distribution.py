#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        # print(A)
        minc=1000000001
        if N==M:
            return (max(A)-min(A))
        for i in range(N-M+1):
            minc=min(A[i+M-1]-A[i],minc)
            # print (minc, i,i+M-1)
        return minc
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends
