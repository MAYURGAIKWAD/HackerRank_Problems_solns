class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        d={}
        for i in range(n):
            if a[i] not in d:
                d[a[i]]=1
            else:
                d[a[i]]+=1
            if d[a[i]]==k:
                return a[i]
        return -1
