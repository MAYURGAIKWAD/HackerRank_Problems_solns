#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        d={}
        maxS=""
        tempS=""
        i=0
        while i<len(S):
            if S[i] not in d:
                d[S[i]]=i
                tempS+=S[i]
                if i!= len(S)-1:
                    i+=1
                    continue
            i=d[S[i]]+1
            d={}
            if i == len(S):
                i+=4
            i-=1
            if len(tempS)> len(maxS):
                # print(tempS,maxS)
                maxS=tempS
                tempS=""
            else:
                tempS=""
            i+=1
            # print(d, tempS)
        # print(maxS)
        return len(maxS)
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends
