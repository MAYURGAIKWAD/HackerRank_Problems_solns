#User function Template for python3

class Solution:
    def pageFaults(self, N, C, pages):
        fault=0
        cache=[]
        for i in range(N):
            if pages[i] not in cache:
                fault+=1
                if len(cache)<C:
                    cache.append(pages[i])
                else:
                    cache.pop(0)
                    cache.append(pages[i])
            else:
                for j in range(len(cache)):
                    if pages[i]==cache[j]:
                        cache.pop(j)
                        cache.append(pages[i])
                        break
        return fault
                    
                    
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        pages = input().split()
        for itr in range(N):
            pages[itr] = int(pages[itr])
        C = int(input())

        ob = Solution()
        print(ob.pageFaults(N, C, pages))

# } Driver Code Ends
