class StackNode:

# Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:

    def __init__(self):
        self.rear=None
    #Function to push an integer into the stack.
    def push(self, data):
        
        # Add code here
        temp=StackNode(data)
        if self.rear==None:
            self.rear=temp
        else:
            temp.next=self.rear
            self.rear=temp
        


    #Function to remove an item from top of the stack.
    def pop(self):
        if self.rear==None:
            return -1
        temp=self.rear.data
        self.rear=self.rear.next
        return temp


        # Add code here


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends
