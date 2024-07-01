
x = int(input("Enter a number \n"))
flag = True
for i in range(2, x-1):
    if x % i != 0:
        flag = True


    else:
        flag = False
        break

if flag == True: print("x is a prime number")
else: print("x is not a prime number")

