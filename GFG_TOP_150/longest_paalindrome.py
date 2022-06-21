#User function Template for python3

def search(S, i, j):
    count=0
    if i==j:
        count=1
    else:
        count=0
            
    while(i>=0 and j< len(S)):
        if S[i]==S[j]:
            if i==j:
                i-=1
                j+=1
                continue
            count+=2
            i-=1
            j+=1
        else:
            break
    return S[i+1:j]
            


class Solution:
    
    def longestPalin(self, S):
        # code here
        maxc=0
        maxs=""
        for i in range(len(S)):
            t1=search(S,i,i)
            t2=""
            if i+1<= len(S)-1:
                t2=search(S,i, i+1)
            if len(t2)>len(t1):
                if len(t2)>maxc:
                    maxc=len(t2)
                    maxs=t2
                continue
            else:
                if len(t1)>maxc:
                    maxc=len(t1)
                    maxs=t1
                # continue
                    
        return maxs
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends
