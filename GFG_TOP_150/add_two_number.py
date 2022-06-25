#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        l1=0
        l2=0
        f=first
        s=second
        ans=[]
        while f!=None:
            l1+=1
            f=f.next
        while s!=None:
            l2+=1
            s=s.next
        f=first
        s=second
        # print(l1,l2)
        if l1>= l2:
            # prev=None
            for i in range(l1-l2):
                # prev
                ans.append(f.data)
                f=f.next
                
            while f!=None:
                ans.append(f.data+s.data)
                f=f.next
                s=s.next
            
            # return first
        else:
            for i in range(l2-l1):
                ans.append(s.data)
                s=s.next
                
            while s!=None:
                ans.append(s.data+f.data)
                f=f.next
                s=s.next
            
            # return second
        # print(ans)
        carry=0
        for i in range(len(ans)-1, -1,-1):
            if i==0:
                ans[i]=(ans[i]+carry)
            elif ans[i]+carry>=10:
                ans[i]=(ans[i]+carry)%10
                carry=1
            else:
                ans[i]=(ans[i]+carry)
                carry=0
        # print (ans)
        
        #adding the data to the ll
        if (l1>=l2):
            f=first
            for i in range(len(ans)):
                if ans[i]>=10 and i==0:
                    newNode=Node(ans[i]//10)
                    newNode.next=first
                    first.data=ans[i]%10
                    first=newNode
                    f=f.next
                    continue
                f.data=ans[i]
                f=f.next
            return first
        else:
            s=second
            for i in range(len(ans)):
                if ans[i]>=10 and i==0:
                    newNode=Node(ans[i]//10)
                    newNode.next=second
                    second.data=ans[i]%10
                    second=newNode
                    s=s.next
                    continue
                s.data=ans[i]
                s=s.next
            return second
            
                
                
                    
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
