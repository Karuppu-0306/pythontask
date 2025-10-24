#1
a=[]
number=int(input("enter the number :"))
for i in range(number):
    num=input("enter the value:")
    a.append(num)
print(a)
print()
                                  

#2

fruites=["apple","orange","grapes","pineapple","mango"]
for fruites in fruites:
    print(fruites)
print()

#3
name=[]
for i in range(1):
    n=input("enter the name")
    name.append(n)

    if n=='stop':
        break
    print()
print()

#4                                
L=[1,2,3]
for i in range(4,7):
    L.append(i)
print()
                                  
#5
city=["madurai","chennai","erode","coimbatore",]
print(city)
city.remove('chennai')
print("remove one city",city)
print()
                                  
#6
a=[12,45,64,4,4]
a.pop()
print(a)
                                   
#7

sub=[]
for i in range(5):
      s=input("enter the subject")
      sub.append(s)
print(sub)
print()
                                     
#8

l=['tamil','english','commecre','accounts','economice','histroy']
print(l)
r=input("enter you want to remove s specific item")
l.remove(r)
print(l)
print()
   
                                    
#9

num=[]
for i in range(1,11):
    num.append(i)
print(num)
print()
                                 
#10

num=[1,2,3,4,5,6,7,8,9,10]
odd=[]
print(num)
for i in num:
    if i%2!=0:
        odd.append(i)
print("remove even mumbers :",odd)



