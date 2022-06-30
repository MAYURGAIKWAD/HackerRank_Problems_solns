class Solution:
    # def dfs(self,image,sr,sc)
	def floodFill(self, image, sr, sc, newColor):
	    t=image[sr][sc]
	    stack=[]
	    stack.append([sr,sc])
	    visited={}
	    while len(stack)>0:
	        tr,tc=stack.pop()
	        if tr<0 or tr>len(image)-1 or tc<0 or tc>len(image[0])-1:
	           # print(tr,tc)
	            continue
	        if (str(tr)+"_"+str(tc)) in visited.keys():
	            continue
	        if image[tr][tc] == t:
	            visited[str(tr)+"_"+str(tc)]=1
	            image[tr][tc]=newColor
	            stack.append([tr+1,tc])
	            stack.append([tr-1,tc])
	            stack.append([tr,tc+1])
	            stack.append([tr,tc-1])
        return image
	        
	        


#{ 
#  Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends
