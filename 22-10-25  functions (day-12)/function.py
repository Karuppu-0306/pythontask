#1. Find tha key
def stars(**a):
    for a in a.keys():
        print ("key valve", a)
stars(a=4,b=4,c=90)

#2. find value

def stars(**a):
    for a in a.values():
        print ("valve", a)
stars(a=4,b=4,c=9)

#3.sum all sum in list

def add(**a):
    sum=0
    for i in a.values():
        sum=+i
        print("sum is:, sum")
add(a=13,b=23,c=56)


#4. print even numberes
def bad (*a):
    for i in a:
        if i%2==0:
            i+=i+1
            print ("the even numbers are:",i,"/n")
bad(12, 34, 23, 45)


#5.

def pertect_number (*a):
                 for n in a:
                      sum1=0
                      for n in range (1,n):
                          if n%n==0:
                              sum1=sum1+n
                      if sum1==n:
                          print (n, "1s a perfect num")
                      else:
                          print (n, "is not apertect nu")
pertect_number (6, 28, 12)
print()


#6.remove a last key

def remove_last(**a):
    print("before remove:",a)
    a.popitem()
    print("after remove:",a)
remove_last(a=10,b=25,c=90,d=100)
print()


#7. simple calculator using function

def calculator(a,b,op):
    if op == '+':
        print("Addition is:",a+b)
    elif op == '-':
        print("Subtraction is:",a-b)
    elif op == '*':
        print("Multiplication  is:",a*b)
    elif op == '/':
        print("Division is:",a/b)
    else:
        print("Invalid operator")
calculator(10,5, '+')
calculator(10,5, '*')
print()

#8. check wjether a passed string is palindrome or not

def palindrome(a):
    if a== a[::-1]:
        print(a,"is palindrome")
    else:
        print(a,"is not palindrome")

palindrome("madam")
palindrome("hello")
print()


#9. count number of vowels, consonant and character in a string

def count_string(a):
    v = c = s = 0
    for ch in a:
        if ch.lower() in "aeiou":
            v = v + 1
        elif ch.isalpha():
            c = c + 1
        else:
            s = s + 1
    print("vowels:",v)
    print("consonants:",c)
    print("secial characters:",s)

count_string("karuppu@34")





      
