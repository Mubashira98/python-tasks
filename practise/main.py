a=input("enter 2 numbers:")
b=input()
sum = (int(a)+int(b))
print (str(sum))

# Average of three numbers-

a= input("enter 3 numbers:")
b= input()
c= input()
avg=(int(a)+int(b)+int(c))/3
print(str(avg))

# swapping

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("a:"+str(a))
print("b:"+str(b))
temp=a
a=b
b=temp
print("after swapping-3")
print("a:"+str(a))
print("b:"+str(b))

# list operations

list=["mubi","shafa","hy"]
list[2]="fam"
list.append(334)
print(list)
list.remove(list[2])
print(list)
list.append(input("enter a value:"))
print(list)

