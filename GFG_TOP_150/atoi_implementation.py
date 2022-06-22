#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        ans=0
        if string[0] =="-":
            #negative string detected
            for i in range(1, len(string)):
                if abs(ord(string[i])-ord("0"))>9 or ord(string[i])<ord("0"):
                    return -1
                ans+= (ord(string[i])-ord("0"))*(10**(len(string)-i-1))
            return ans*-1
        else:
            #positive number
            for i in range(len(string)):
                if abs(ord(string[i])-ord("0"))>9 or ord(string[i])<ord("0"):
                    return -1
                ans+= (ord(string[i])-ord("0"))*(10**(len(string)-i-1))
            return ans
                
            
            

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends
