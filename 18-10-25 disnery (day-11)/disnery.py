#1. check the key 

a={23:"leo",4:"batman",58:108,22:"sanji"}
if 50 in a:
z    print("is already exit")
else:
    print("not exit")

#2. merge two disnery
a={23: "leo",4:"batman",58:108,22:"sanji"}
b={1:22,6:78}
a.update(b)
print(a)

#3. sum of item

d={}
num=int(input("enter the count :"))
for i in range(num):
    key=int(input("enter the key :"))
    value=key**2
    d[key]=value
print("dictory :",d)

#4. iterte dict

a={23:"leo",4:"batman",58:103,22:"sanji"}
for key, value in a.items():
    print(f"key:{key},value:(value)")


#5.

a={x:x**2 for x in range(1,16)}
print(a)

#6. remove a key

a={23:"leo",4:"batman",58:103,22:"sanji"}
a.pop(4)
print(a)

#7 length

a={23:"leo",4:"batman",58:103,22:"sanji"}
b=len(a)
print("the length of the dict is:",b)

#8. defalu key

a={23:"leo",4:"batman",58:103,22:"sanji"}
a.setdefault(2,"nill")
print(a)

#9.neu dict trom exixting dict


d={}
num=int (input ("enter a count:"))
for i in range (num):
    keys=input ("enter the keys value:")
    value=input ("enter the value:")
    d[keys] =value
print ("dictinory:", d)
print (d.keys())
print ()
       
#10 type of

d={}
num=int (input ("enter a count:"))
for i in range(num):
    keys= input("enter the key value:")
    value= input ("enter the value:")
    d[keys]=value
print ("dictinory: ", d)
print (type (keys))




