#append function example
#a=[10,20,30]
#a.append(50)
#print(a)
#a.append('ram')
#print(a)

#list inside list
#a = [10,20,30,[1,2,['a', 'b']]]
#print(a[3][1])
#print(a[3][2][1])

#insert function
#a=[10,20,30]
#a.insert(1,40)
#print(a)
#a.insert(3,'ram')
#print(a)

#mylist = []                   sdictionary function used
#mydic = {'name': 'abc',
#          'roll': 123}
#mydic1 = {'name': 'pqr',
#          'roll': 234}

#mydic2 = {'name': 'xyz',
#          'roll': 456}

#mylist.append(mydic)
#mylist.append(mydic1)
#mylist.append(mydic2)
#print(mylist[1]['name'])


#slicing operator

#a=[1,2,3,4,5,6,7,8]
#print(a[3:])
#b='india'
#print(b[1:4])


#recursion
#def sum(a):
#    if len(a)==1:
#        return a[0]
#    else:
#        return a[0]+sum(a[1:])
#print(sum([10,20,30,40]))


#def fact(n):
#  if n==1: # or n==0:
#        return 1
#  else:

#       return n*fact(n-1)
#
#print(fact(998))

#      class example

#class Student:
#    branch='cse'                                                                 #class member
#    count=0
#    def __init__(self,name,age,year):
#        self.name=name                                                            #object member
#        self.age=age
#        self.year=year
#        Student.count=Student.count+1
#
#    def getname(self):
#    def getage(self):
#        print(self.age)
#    def changeyear(self):
#        self.year=self.year+1
#s1=Student('roy',20,1)
#s1.getname()
#s1.getage()
#print(s1.year)
#s1.changeyear()
#print(s1.year)

#s2=Student('ram',22,4)
#s2.getname()
#s1.getname()
#s2.getage()
#print(s2.year)
#s2.changeyear()
#print(s2.year)

#s3=Student('ali',34,2)
#s3.getname()
#s3.getage()
#print(s3.year)
#s3.changeyear()
#print(s3.year)
#print(s1.branch)
#print(s2.branch)
#print(Student.count)

#  example

#class Employe:
#    total_employe = 0

#    def __init__(self,name,salary):
#        self.name=name
#        self.salary=salary
#        Employe.total_employe=Employe.total_employe+1
#    def getname(self):
#        print(self.name)
#
#    def getsalary(self):
#        print(self.salary)
#
#data=Employe('prathvi',1.000)
#data.getname()
#data.getsalary()
#print(Employe.total_employe)

 #Inheritence Example

#class Parent:
#    def __init__(self):
#        print('calling parent constructor')
#
#    def parentmethod(self):
#        print('calling parent method')

#class Child(Parent):                                                             #inherit syntax
#    def __init__(self):
#        print('calling child constructor')
#
#    def childmethod(self):
#        print('calling child method')
#
#c=Child()
#c.childmethod()
#c.parentmethod()
#p=Parent()
#p.parentmethod()
#p.childmethod()

#  Stack implement Example

#class Stack:
#    def __init__(self):
#        self.items=[]
#    def isempty(self):
#        return self.items==[]
#    def push(self,n):
#    def pop(self):
#        return self.items.pop()
#    def size(self):
#        return len(self.items)

#s=Stack()
#print(s.isempty())
#s.push(10)
#s.push(20)
#s.push(30)
#print('size of Stack is %d'%s.size())
#print(s.pop(),s.pop(),s.pop())
#print("size of stack is %d"%s.size())
#


#class Person:
#
#    def __init__(self,first,last):
#        self.firstname=first
#        self.lastname=last

#    def getname(self):
#        return self.firstname+ ' ' +self.lastname

#class Employee(Person):

#    def __init__(self,first,last,empid):
#        super(). __init__(first,last)                                            #Person.__init__(self,first,last)
#        self.empid=empid

#    def getEmp(self):
#        return self.getname()+" "+self.empid

#p=Person('Virat','Kohli')
#e=Employee('Leo','Messi','1007')
#p.getname()
#e.getEmp()
#print(p.getname())
#print(e.getEmp())

#=====extend example======
#a = [10,20,30]
#b = ['a','b','c']
#a.extend(b)
#print(a)

#====remove example===
#a = [10,20,'cow','ram',4.5,'cow']
#a.remove('cow')
#print(a)

#a=[15,18,19,10,6,3,0,9]
#print(a)
#a.sort()
#b=sorted(a,reverse=True) #b=sorted(a)
#print(a)
#print(b)
#add=lambda x,y,:x+y
#print(add(2,3,))

#def temperature(c):
# return (9/5)*c+32
#f=int(input('Enter ur temp in celcius '))
#print("degree celcius: %d\tdegree farenhiet: %.1f" %(f,temperature(f)))

#=============lambda function==============
#temperature=lambda c:(9/5)*c+32
#f=int(input('Enter ur temp in celcius '))
#print("degree celcius: %d\tdegree farenhiet: %.1f" %(f,temperature(f)))


#simple temperatur programe above2 examples

#Celsius = int(input('Enter the temperature in celsius : '))

#Fahrenheit = 9.0/5.0 * Celsius + 32

#print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")


#celcius = [39.2,37.3,37.8,45]
#f = map(lambda x : (9/5)*x+32,celcius)
#1stway:
#for ele in f:
#    print (ele)
#print(f)
#2ndway:
#fh = []
#for ele in f:s
#    fh.append(ele)
#print(fh)

#def sqr(n):
#    return n*n
#numbers=[2,4,8,9,6]
#s=map(lambda sqr:sqr*sqr,numbers)
#print(list(s))
#=============perfect square====================
#import math
#def is_prfect(n):
#    s=math.sqrt(n)
#    s=int(s)
#    return s*s==n
#def is_fibo(n):
#    if is_perfect(5*n*n+4) or (5*n*n-4):
#        print('%d is in fibonacci series' %n)
#
#    else:
#        print('%d is not in fibonacci'%n)

#a=int(input('Enter any no :\n'))
#is_fibo(a)

#===============Queue example=============
#class Queue:
#    def __init__(self):
#        self.item = []
#    def is_empty(self):
#        return self.item == []
#    def enqueue(self,n):
#        self.item.insert(0,n)
#    def dequeue(self):
#        self.item.pop()
#    def size(self):
#        return len(self.item)

#q=Queue()
#rint(q.is_empty())
#q.enqueue(10)
#q.enqueue('Ram')
#q.enqueue(4.5)
##print(q.item[1])
#print(q.item)


#q.dequeue()
#print(q.item)

#######################    sorting  ########
#def linear_search(a,item):
#    found=False
#    for ele in a:
#        if ele ==item:
#            found=True

#    return found

#b=[10,20,25,6,90,56,43]
#a=int(input('Enter a no u search:'))
#print(linear_search(b,a))



#binary search

#def binary_search(a,item):
#    f=0
#    l=len(a)-1
#    found=False

#    while f<=l and not found:
#        mid =(f+l)/2
#        if a[mid]==item:
#            found=True

#        else:

#            if item>a[mid]:
#                l=mid-1
#    return found
#a=[10,20,30,55,60]
##print(list(a))
#item=input('Enter u want to search: ')
#print(binary_search(a,item))

###
#def bubble_sort(a):
#    for passnum in range(len(a)-1,0,-1):
#        for i in range(passnum):
#            if a[i]>a[i+1]:
#                temp=a[i]
#                a[i]=a[i+1]
#                a[i+1]=temp
#a=[40,30,20,10,9,62,45,35]
#ubble_sort(a)
#print a
