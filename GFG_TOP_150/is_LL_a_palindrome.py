#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        l=0
        h=head
        while h!=None:
            l+=1
            h=h.next
        h=head
        h1=head
        h2=head
        if l==1:
            return True
        if l%2==0:
            #reverse till l/2
            count=0
            prev=None
            while count<l/2:
                count+=1
                temp=h.next
                h.next=prev
                prev=h
                h=temp
            h1=prev
            h2= temp
        else:
            #implement something similar for odd count
            count=0
            prev=None
            while count<l//2:
                count+=1
                temp=h.next
                h.next=prev
                prev=h
                h=temp
            h1=prev
            h2= temp.next
            # pass
        while h1!=None or h2!=None:
            if h1.data!=h2.data:
                return False
            h1=h1.next
            h2=h2.next
        return True
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends
