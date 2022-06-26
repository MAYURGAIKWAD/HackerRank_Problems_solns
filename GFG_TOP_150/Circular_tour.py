'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        psum=0
        dsum=0
        for i in range(n):
            psum+=lis[i][0]
            dsum+=lis[i][1]
        # print(lis)
        # print(lis[0][0], lis[0][1])
        # print(lis[2][0], lis[2][1])

        # print(psum,dsum, lis[0][:])
        if psum<dsum:
            return -1
        startpos=0
        tmp=0
        while startpos<n:
            if lis[startpos][0]>= lis[startpos][1]:
                #viable start position
                tmp=0
                for i in range(n):
                    tmp+=lis[(startpos+i)%n][0]-lis[(startpos+i)%n][1]
                    if tmp<0:
                        break
                # print(startpos,tmp)
                if tmp>=0:
                    return startpos
            startpos+=1
            # print(startpos,tmp)
        return -1
            
        

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends
