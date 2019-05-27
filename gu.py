for n in range(1,3):
	from random import randint
	d=randint(1,20)
	
	print(d)
	if d<15:
		print("try again")
	elif d==15:
		print("you score it")
		break
	elif d>15:
		print("try again")
