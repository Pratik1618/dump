lim=int(input("Enter the limit:"))
first=0
second=1
next=0
for i in range (0, lim ,1):
 if i==0 or i==1:
    print(i, "",end= '')
 else:
    next= first + second
 print(next, "", end= '')
 first = second
 second = next
