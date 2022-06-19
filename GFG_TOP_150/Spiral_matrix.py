#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        ans=[]
        tc=c
        ltc=0
        tr=r
        ltr=0
        while not (ltc>=tc or ltr >=tr):
            
            # ans.append(matrix[ltc][ltr])
            for i in range(ltc,tc):
                # print(ltr,i)
                ans.append(matrix[ltr][i])
            for i in range(ltr+1,tr):
                # print(i,tc-1)
                ans.append(matrix[i][tc-1])
            if ltr!=tr-1:
                for i in range(tc-1-1,ltc-1,-1):
                    # print(tr-1,i)
                    ans.append(matrix[tr-1][i])
            if ltc !=tc-1:
                for i in range(tr-1-1, ltr,-1):
                    # print(i, ltc)
                    ans.append(matrix[i][ltc])
            tc=tc-1
            tr=tr-1
            ltc=ltc+1
            ltr=ltr+1
            
        return ans
        
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
