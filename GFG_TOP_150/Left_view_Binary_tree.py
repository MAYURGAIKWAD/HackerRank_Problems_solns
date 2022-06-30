#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def Search(r,ans,level):
    if r ==None:
        return
    elif len(ans)<=level:
        #left level not found
        if r.left==None and r.right==None:
            ans.append(r.data)
            return
        elif r.left!=None:
            ans.append(r.data)
            Search(r.left,ans,level+1)
        elif r.right!=None:
            ans.append(r.data)
            Search(r.right,ans,level+1)
    elif len(ans)>level:
        if r.left==None and r.right==None:
            return
        elif r.left!=None:
            Search(r.left,ans,level+1)
        elif r.right!=None:
            Search(r.right,ans,level+1)
        
    else:
        print("I missed something")
    
    return ans
    
    return 
def LeftView(root):
    
    # code here
    r=root
    ans=[]
    level=0
    if r==None:
        return ""
    else:
        ans.append(root.data)
        Search(root.left,ans,level+1)
        Search(root.right,ans,level+1)
    return ans
        

#{ 
#  Driver Code Starts
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        result = LeftView(root)
        for value in result:
            print(value,end=" ")
        print()

# } Driver Code Ends
