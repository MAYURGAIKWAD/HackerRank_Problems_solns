#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=-1

    def push(self,x):
        #CODE HERE
        # print (self.s,self.minEle)
        if self.minEle==-1:
            self.minEle=x
            self.s.append(x)
            return 
            
        elif x<self.minEle:
            self.minEle=(x)
            self.s.append(x)
            return
        self.s.append(x)
        # print (self.s,self.minEle)

    def pop(self):
        #CODE HERE
        if len(self.s)==0:
            self.minEle=-1
            return -1
        t=self.s.pop()
        if t==self.minEle :
            if len(self.s)>0:
                self.minEle=min(self.s)
            else:
                self.minEle=-1
        return t
        

    def getMin(self):
        #CODE HERE
        return self.minEle

#{ 
#  Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends
