#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        da={}
        db={}
        if len(a)!=len(b):
            return 0
        for i in a:
            if i in da:
                da[i]+=1
            else:
                da[i]=1
        for i in b:
            if i in db:
                db[i]+=1
            else:
                db[i]=1
        # print(da,db)
        for i in da.keys():
            # print(i)
            if i not in db.keys():
                # print("executed")
                return 0
            if da[i]!=db[i]:
                return 0
        return 1
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends
