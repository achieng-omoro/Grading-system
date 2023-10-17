bio=float(input('Biology marks: '))
if bio not in range(0,100):
    print("enter valid marks")
chem=float(input('Chemistry marks: '))
if chem not in range(0,100):
    print("enter valid marks")
phy=float(input('Physics marks: '))
if phy not in range(0,100):
    print("enter valid marks")
agric=float(input('Agriculture marks: '))
if agric not in range(0,100):
    print("enter valid marks")

sum = agric+chem+bio+phy
average = sum/4

if  0<=average<31:
     print(f"you're avarage is {average} which is grade D")
elif 30<average<51:
     print(f"you're avarage is {average} which is grade C")
elif 50<average<71:
     print(f"you're avarage is {average} which is grade B")
elif 70<average<101:
     print(f"Your average is {average} which grade A")
else :
     print("unsupported avarage")






