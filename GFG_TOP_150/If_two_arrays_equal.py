#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        Ad={}
        Bd={}
        for i in range(N):
            if A[i] not in Ad:
                Ad[A[i]]=1
            else:
                Ad[A[i]]+=1
            if B[i] not in Bd:
                Bd[B[i]]=1
            else:
                Bd[B[i]]+=1
        for i in Ad.keys():
            if i not in Bd:
                return 0
            if Ad[i]!=Bd[i]:
                return 0
        return 1
