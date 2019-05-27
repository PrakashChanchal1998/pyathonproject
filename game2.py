for n in range(1,4):
        from random import randint
        
        d=randint(1,20)
        print(d)
        n =int(input())
        if n<d:
                print("you almost there")
        elif n==d:
                print("yes you got answer")
                break
        elif n>d:
                print("you go far from number")

