Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[6,4,2,9,1]
>>> for i in range(len(l)-1):
	for j in range(len(l)-1):
		if l[j]>l[j+1]:
			l[j],l[j+1]=l[j+1],l[j]
	print(l)

	
[4, 2, 6, 1, 9]
[2, 4, 1, 6, 9]
[2, 1, 4, 6, 9]
[1, 2, 4, 6, 9]
>>> 