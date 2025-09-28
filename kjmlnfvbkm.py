z=int(input("Введите число:"))
if z%2==0: print("Число четное")
else: print("Число нечетное")

z=int(input("Введите двузначное число:"))
x=z//10
c=z%10
if x>c: print("first")
if x<c: print("second")
if x==c: print("equal")