a=int(input("How many numbers do you want?: "))
lst1 = []
s = 0
for i in range(0,a):
    b=int(input("Enter number"+str(i+1)+":"))
    lst1.append(b)
    s += b   #s =+ i
print("lst1 =",s)

# ---------------------------------------------------------

lst2 = [10, 20, 30 , 5]
s = 0
for i in lst2:
    s = s + i
print("lst2 =",s)

# ---------------------------------------------------------

lst3 = [10, 20, 30 , 10]
print("lst3 =", sum(lst3))

# ----------------------------------------------------------

lst4 = [10 + 20 + 30 + 15]
print("lst4 =",lst4)
