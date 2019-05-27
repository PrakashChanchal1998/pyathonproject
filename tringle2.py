for n in range(5):
    for m in range(9):
         if n==0:
             print("*",end="")
         elif m==n:
             print("*",end="")
         elif m==8-n:
             print("*",end="")
         else:
             print(" ",end="")
    print()
         
