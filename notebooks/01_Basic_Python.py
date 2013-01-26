# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Basic Python(Short version)

# <markdowncell>

# This is just to give you a glimpse of what Python can do.
# We select only subset of the feature we think will be useful for doing analysis. We also leave links in various place in case you want to do your own further study and there is also an extended edition if you want to learn more.
# 
# For more complete features, you can look at Python [official documentation](http://docs.python.org/2/) or a book like [Think Python](http://www.greenteapress.com/thinkpython/html/index.html)
# 
# In this tutorial we will be using [IPython](http://ipython.org). To execute current cell and go to the next cell in this tutorial press ``Shift+Enter``. If things go wrong you can restart Kernel by either click on Kernel at the top bar and choose restart or press `Ctrl+M+.` (Press that DOT symbol too)

# <headingcell level=3>

# Hello World

# <codecell>

#press shift+enter to execute this
print 'Hello world'

# <codecell>

#ipython automatically show representation of 
#the return value of the last command
1+1

# <headingcell level=3>

# Data Type(Usual Stuff)

# <codecell>

x = 1 #integer
y = 2.0 #float
t = True #boolean (False)
s = 'hello' #string
s2 = "world" #double quotes works too
#there are also triple quotes google python triple quotes
n=None #Null like variable None.

# <codecell>

print x+y #you can refer to previously assigned variable.

# <codecell>

s+' '+s2

# <codecell>

#boolean operations
x>1 and (y>=3 or not t) and not s=='hello' and n is None

# <codecell>

#Bonus: The only language I know that can do this
0 < x < 10

# <markdowncell>

# ####Bonus: String formatting
# One of the best implentation. There are couple ways to do string formatting in Python.
# This is the one I personally like.

# <codecell>

'x is %d. y is %f'%(x,y)

# <codecell>

#even more advance stuff
#locals returns dictionary of
#local variables which you then use 
#in formatting by name
'x is %(x)d. y is %(y)f'%locals() #easier to read

# <markdowncell>

# ##List, Set, Tuple, Dictionary, Generator

# <markdowncell>

# List
# ----
# Think of it as std::vector++

# <codecell>

l = [1, 2, 3, 4, 5, 6, 7]
print l #[1, 2, 3, 4, 5, 6, 7]
print l[2] #3
print len(l) # list length
print l[-1] #7 negative index works from the back (-1)
l2 = [] #want an empty list?
print l2

# <codecell>

#doesn't really need hold the same type
#but don't recommend. You will just get confused
bad_list = ['dog','cat',1,1.234]

# <codecell>

l[1] = 10 #assignment
l

# <codecell>

l.append(999) #append list
l

# <codecell>

#can be created from list com
l.sort() #sort
l

# <codecell>

#searching O(N) use set for O(log(N))
#http://docs.python.org/2/tutorial/datastructures.html#sets
10 in l

# <codecell>

11 not in l

# <codecell>

#useful list function
range(10) #build it all in memory

# <codecell>

#List Comprehension
#we will get to for loop later but for simple one
#list comprehension is much more readable
print l
my_list = [2*x for x in l]
print my_list
my_list = [ (2*x,x) for x in range(10)]
print my_list
my_list = [3*x for x in range(10) if x%2==0]
print my_list

# <codecell>

#This might come in handy
[1]*10

# <markdowncell>

# ####Bonus: Python Autocomplete

# <codecell>

#in this cell try my_ and press tab
#IPython knows about local variables and
#can do autocomplete (remember locals()?)

# <codecell>

#try type len(<TAB> here
#python can give you documentation/function signature etc.

# <markdowncell>

# Tuple
# -----
# Think of it as immutable list

# <codecell>

tu = (1,2,3) #tuple immutable list
print tu
tu2 = tuple(l) #convert list to tuple
print tu2
tu3 = 4,5,6 #parenthesis is actually optional but makes it more readable
print tu3

# <codecell>

#access
tu[1]
#you can't assign to it

# <codecell>

#tuple expansion
print tu
x, y, z = tu
print x #1
print y #2
print z #3
print x, y, z #you can use tuple in print statement too

x, y, z = 10, 20, 30#parenthesis is actually optional
print z, y, x #any order

# <codecell>

#useful for returning multiple values
def f(x,y):
    return x+y, x-y #parenthesis is implied
a, b = f(10,5)
print a #15
print b #5
print a, b #works too

# <markdowncell>

# Dictionary
# ----------
# 
# Think of it as std::map - ish. It's actually a hash table. There is also OrderedDict if you also care about ordering.

# <codecell>

d = {'a':1, 'b':10, 'c':100}
print d #{'a': 1, 'c': 100, 'b': 10}
d2 = dict(a=2, b=20, c=200) #using named argument
print d2 #{'a': 2, 'c': 200, 'b': 20}
d3 = dict([('a', 3),('b', 30),('c', 300)]) #list of tuples
print d3 #{'a': 3, 'c': 300, 'b': 30}
d4 = {x:2*x for x in range(10)}#comprehension (key doesn't have to be string)
print d4 #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
d5 = {} #empty dict
print d5 #{}

# <codecell>

print d['a'] #access
print len(d) #count element
d['d'] = 1000#insert
print d #{'a': 1, 'c': 100, 'b': 10, 'd': 1000}
del d['c']#remove
print d #{'a': 1, 'b': 10, 'd': 10}
print 'c' in d #keyexists?

# <codecell>

#use dictionary in comprehension
#d.items() return generator which gives tuple 
#k,v in d.items() does tuple expansion in disguise
new_d = {k:2*v for k,v in d.items()}
print new_d #{'a': 2, 'b': 20, 'd': 20}

# <markdowncell>

# ##Control Flow
# ###if else elif
# Indentation in python is meaningful. There is "NO" bracket scoping in python.
# 
# Recommended indentation is 4 spaces not Tab. Tab works but not recommended
# Set your text editor to soft tab. [PEP8](http://www.python.org/dev/peps/pep-0008/) which list all the
# recommended style: space, comma, indentation, new line, comment etc. Fun Read.

# <codecell>

x = 20
if x>10: #colon
    print 'greater than 10'#don't for get the indentation
elif x>5: #parenthesis is not really needed
    print 'greater than 5'
else:
    print 'not greater than 10'
x+=1#continue your execution with lower indentation
print x

# <codecell>

#shorthand if
y = 'oh yes' if x>100 else 'oh no' #no colon
print y

# <codecell>

#since indentation matters sometime we don't need any statement
if x>10:
    print 'yes'
else:
    pass #pass keyword means do nothing
x+=1
print x

# <codecell>

#why is there no bracket??
from __future__ import braces # easter egg

# <markdowncell>

# ###For loop, While loop, Generator, Iterable
# 
# There is actually no `for(i=0;i<10;i++)` in python. `list` is an example of iterable.

# <codecell>

#iterate over list
for i in xrange(5): # xrange is a generator
    print i # again indentation is meaningful
print '------'
for i in xrange(20,25): # xrange is a generator see extended version if you wonder
    print i # again indentation is meaningful

# <codecell>

#looping the list
l = ['a','b','c']
for x in l:
    print x

# <codecell>

#if you need index
l = ['a','b','c']
for i,x in enumerate(l):
    print i,x

# <codecell>

#looping dictionary
d = {'a':1,'b':10,'c':100}
#items() returns a generator which return tuple
#k,v in d.items() is tuple expansion in disguise
for k,v in d.items():
    print k,v

# <codecell>

#looping over multiple list together
lx = [1,2,3]
ly = [2*x+1 for x in lx]
print lx, ly
for x,y in zip(lx,ly): #there is also itertools.izip that does generator
    print x,y

# <codecell>

#complete the list with while loop
x = 0
while x<5:
    print x
    x+=1

# <markdowncell>

# ####See Also
# For more complex looping you can look at [itertools](http://docs.python.org/2/library/itertools.html)

# <markdowncell>

# ###Function
# Functions in python is a first class object(except in a very few cases).

# <codecell>

def f(x, y): #remember the colon
    print 'x =',x #again indentation
    print 'y =',y
    return x+y
f(10,20)

# <codecell>

#python is dynamic typing language
#specifically it's Duck Typing(wikipedia it. Fun Read.)
#this means as long as it has the right signature
#Python doesn't care
f('hello','world')

# <codecell>

#you can pass it by name too
#this is useful since you can't always remember the order
#of the arguments
f(y='y',x='x') # notice I put y before x

# <codecell>

#default/keyword arguments
def g(x, y, z='hey'):
    #one of the most useful function
    print locals() # return dictionary of all local variables
g(10,20)
g(10,20,30) # can do it positionally

# <codecell>

g(10,z='ZZZZ',y='YYYY') #or using keyword

# <codecell>

def myfunc(x,y,z, long_keyword="111000"):
    return None

# <codecell>

#IPython knows about keyword arguments name try type this
#myfunc(x, y, z, lon<TAB>

# <markdowncell>

# ####Be careful

# <codecell>

#in your programming life time you might be
#you might be tempting to put a mutable object like list
#as default argument. Just Don't
def f(x,y,z=[]): #Don't do this
    pass
def f(x,y,z=None):
    z = [] if z is None else z

# <markdowncell>

# It has to do with [closure](http://en.wikipedia.org/wiki/Closure_(computer_science)). If you wonder why, you can read [“Least Astonishment” in Python: The Mutable Default Argument](http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument). 

# <markdowncell>

# ####Bonus
# This might comes in handy

# <codecell>

#arbitary number of argument C's va_arg
def h(x,y,*arg,**kwd):
    print locals()
h(10,20,30,40,50,custom_kwd='hey')

# <codecell>

#Bonus: more cool stuff.
#argument expansion
def g(x, y, z):
    print locals()
t = (1,2,3)
g(*t)

# <codecell>

#If you know lambda calculus
f = lambda x: x+1
f(3)

# <markdowncell>

# ###Classes, Object etc.
# 
# Think about Object as pointer to object in C. This will answer so many question about whether we are passing by reference or value or is it copy or assignment. Internally, it actually is C pointer to struct.

# <codecell>

#define a class
class MyClass:
    x = 1 #you can define a field like this
    
    #first argument is called self. It refers to itself
    #think of it as this keyword in C
    def __init__(self, y): #constructor
        self.y = y #or define it here
    
    def do_this(self, z):
        return self.x + self.y + z

# <codecell>

a = MyClass(10)
print a.do_this(100)

# <codecell>

#press a.<TAB> here for IPython autocomplete

# <codecell>

#you can even add field to it
a.z = 'haha'
print a.z

# <codecell>

#remember when I said think of it as C pointer??
b = a
b.x = 999 #change b
print a.x #printing a.x not b.x

# <codecell>

#you may think you won't encounter it but...
a = [1,2,3]
b = a
b[1]=10
print a

# <codecell>

#shallow copy is easy
a = [1,2,3]
b = a[:] #remember slicing? it creates a new list
b[1] = 10
print a, b

# <markdowncell>

# ####Inheritance
# Python support multiple inheritance aka [mixin](http://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful). You can read about it [here](http://docs.python.org/2/tutorial/classes.html#inheritance)
# We won't need it in our tutorial. The basic syntax is the following.

# <codecell>

class Parent:
    x = 10
    y = 20
    
class Child(Parent):
    x = 30
    z = 50

p = Parent()
c = Child()
print p.x
print c.x

