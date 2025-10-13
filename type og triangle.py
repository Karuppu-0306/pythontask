a=int(input("enter the lenth:"))
b=int(input("enter tha breath:"))
c=int(input("enter tha height:"))

if a == b and a == c:
    print("the triarhle is equlateral")
elif a == b or b == c:
    print("the triangle is isoceles")
else:
    print("the triangle is scalen")
