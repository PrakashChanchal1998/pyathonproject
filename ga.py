Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for n in range(1,3):
	import random
	#d=gradient(1,20)
	d=14;
	print(d)
	if d<15:
		print("try again")
	elif d==15:
		print("you score it")
		break
	elif d>15:
		print("try again")
