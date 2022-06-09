class Solution:
	def countTriplet(self, arr, n):
		# code here
		d={}
		count=0
		for i in arr:
		    d[i]=1
	    for i in range(len(arr)):
	        for j in range(i+1,len(arr)):
	            if (arr[i]+arr[j]) in d.keys():
	                count+=1
        return count
