#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        pref=arr[0]
        for i in arr:
            if len(i)<len(pref):
                pref=i
        
        for i in range(len(arr)):
            j=0

            while(j<len(pref)):
                if pref[j]!=arr[i][j]:
                    pref=pref[:j]
                    break
                j+=1
        if len(pref)==0:
            return -1
        return pref
        
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends
