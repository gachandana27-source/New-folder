print("Hello, World!")
import keyword
print(len(keyword.kwlist))
a=10
a=20
print(a)#overwritten
a=10
print(id(a))
a,b,c,d=(10,10,10,20)
print(id(a),id(b))
a1=10
print(a1)
a=10.4
print(type(a))
a=True
print(a)
a=0
print(a)
print(bool(a))
a='hello'
print(a,type(a))
a='Hello' #indexing
print(a[3])
a="happy mother's day"
print(a[12]) #list
a= [10,23,4.5,5,6.5]
print (a[3])
a=[1,20.4,['10']]
print(a[-1][0] [0])
a=(10,) #tuple
print(type(a))
a={10,20,30,40} #set
print(a)
x=[1,2,3]
print(x*2)
a=5
b=2
print(a//b)
print(type(10/2))
print(type(lambda x:x))
def f(x):return x*2
res=map(f,[1,2,3])
print(list(res))


s='good morning good afternoon' #   slicing
print(s[-17:-21-1:-2])
print(s[-14:-22-1:-2])

a='india is best'
a[9:13:1]

s=int(input('enter the name:'))
print(type(s))
s=int(input('enter the number:'))
if s%2==0:
    print('even')
a=4
b=8
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")
    
a='A'
b="b"
if a.isupper():
    print("uppercase")
elif a.islower():
    print("lowercase")
else:
    print("not alphabet")
    
    char = input('enter:')
if 'A' <= char <= 'Z':
    print("uppercase")
elif 'a'<= char <= 'z':
    print("lower")
else:
    print("spl char")
    
s = input("alphabet:")
if s.isalpha():
    if s in 'aeiouAEIOU':
        print('vowel')
    else:
        print("consonant")
else:
        print("not alphanet")

a=eval(input("enter:"))
if type(a)==list:
    if len(a)%2==0:
        print("even")
    else:
        print('its odd')
else:
        print('not list')

i=1
while i<=5:
    print('hello')
    i=i+1
    
    a=[10,20,30,40]
while i<len(a):
    print(a[i])
    i=i+1    #print all the element in the list
    n= int(input("enter:"))
rev=0
while n>=0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
    print(rev)
    
    
s=input("enter:")
out=''
for i in  s:
    if  'A'<=s<='Z':
        oout=out+chr(ord(i)+32)
    elif  'a'<=s<='z':
            out=out+chr(ord(i)-32)
    else: 
        out=out+i      
print(out)


    
 
 
 
  