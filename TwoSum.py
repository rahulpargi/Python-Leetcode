class Test:
	def sum(self,a,b):
		for i in range(len(a)):
			for j in range(1,len(a)):
				if a[j]==b-a[i]:
					print([i,j])
			
			


					
					
					
					
				
			
			

c=Test()
c.sum([3,2,4],6)