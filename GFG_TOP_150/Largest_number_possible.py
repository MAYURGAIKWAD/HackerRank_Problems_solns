#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        t=""
        if S==0 and N>1:
            return -1
        if S<=9:
            t=str(S)
            for i in range(1,N):
                t+="0"
            return t
        while S>0:
            if S>9:
                t+="9"
                S=S-9
                continue
            else:
                t+=str(S)
                S=S-S
                if len(t)>N:
                    return -1
                for i in range(len(t),N):
                    t+="0"
                    
        return t
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends
