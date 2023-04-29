username = 'Anthony'
password = 'FTS'
api_key_name = 'example API Key name'
one_time_password = 12345

body = {
    'username': username,
    'password': password,
    'api_key_alias': api_key_name,
    'otp': one_time_password
}

print(type(body))

mystring = 'Anthony'
mystring[1:1:2] #String SLicing[start:stop:step]
myString[::-1]  #reverse a string

list4 = [5,3,4,6,1]
list4.sort()
sorted(list4, reverse=True) # One way to sort and reverse a list --> myList[::-1] is more efficient.

name = 'Sam'
age = 28
print(f'{name} is {age} years old')

set(1) #unordered collections of unique elements, can use to filter lists for uniquqe elements

'''
##Data types:
Numbers 
strings - ordered sequence of characters --> slicing, indexing, methods
lists - ordered sequence of objects and mutable --> append, pop, ordered ie: indexing, slicing, methods, literal notiations 'f'
dictionaries - unordered key value pairs: {'key':value"}
tuples - ordered sequence of objects but immutable --> t = (1,2) immutable pairs of data
sets - set(1) unordered collections of unique elements, can use to filter lists for uniquqe elements
bool - True False

--------

Jupyter --> pwd to "print working directory"

        --> Shift + Tab = check the argument parameters in a method or function
        --> Python has help() function same as above

        --> %%writefile myfile.txt
            input whatever content.

        --> After reading your file you need rto reset the cursor so myfile.seek(0)

        --> Can use myfile.readline() method to break each line as an element into a list.
        --> need to close the file myfile.close() as well to avoid python keeping it open
        --> Just assign it to a variable then close it and the info is stored without conflict
            with open('myfile.txt') as my_new_file:
                contents = my_new_file.read()

        --> xsrf saving issue: Just open another (non-running, existing) notebook on the same kernel, 
            and the issue is magically gone; you can again save the notebooks that were previously showing the _xsrf error.
'''
# Comparrison operators: ==, !=, <, >, <=, >=
# Logical Operators: and (both true), or (is one true), not (returns opposite boolean)

if True:
    print('Its True')

location = 'bank'

if location == 'auto shop':
    print('cars are cool')
elif location == 'bank':
    print('money is cool')
elif location == 'grocer':
    print('food is cool')
else:
    print('nothing is cool')

#----------------------------------
#for loops
#a list of Tuples:
mytup = [(1,2,),(3,4),(5,6)]
print(len(mytup))

for item in mytup:
    print(item)
    print("")

#tuple unpacking
for a,b in mytup:
    print(a)
    print(b)

#while loops:
x = 0

while x <= 5:
    print(f'The current value of of X is {x}')
    x += 1      #x = x + 1
else:
    print("X is now > 5")

    #Break - Breaks out of the current closest enclosing loop.
    #continue - goes to the top of the closest enclosing loop.
    #pass - does nothing, a placeholder after a for staement to prevent a syntax error

#pass
x= [1,2,3]

for items in x:
    pass 

#continue - it comes across the 'a' and stops and moves to the next
mystring2 = 'Sammy'

for letter in mystring2:
    if letter == 'a':
        continue
    print(letter)

#break stops the loop once it comes to an 'a'
for letter in mystring2:
    if letter == 'a':
        break
    print(letter)

#enumerate
#gives touples of index, item
word = 'abcde'
for item in enumerate(word):
    print(item)

#zip --> zips lists together
thislist1 = [1,2,3,4]
thislist2 = ['a','b','c']
thislist3 = [100, 200, 300]
zipped = zip(thislist1,thislist2,thislist3)

for item in zip(thislist1, thislist2):
    print(item)

print('')
#now zip in tuples of threes:
for item in zip(thislist1,thislist2,thislist3):
    print(item)

print('')
#turn your zip into a list
print(list(zip(thislist1,thislist2,thislist3)))

print('')

for a,b,c in zipped:
    print(b)

#the "in" operator as itself.  Check if something is in a list.
'fts' in [1,2,'fts'] #--> returns true

'a' in 'abc' #--> returns true

'fts' in {'fts':100} # --> returns true

ok = {'fts':100}
100 in ok.values() # --> True
'fts' in ok.keys() # --> True

#------------

mylist = [10,20,30,40,50]
max(mylist) # --> 50
min(mylist) # --> 10

#list comprehension
myword = 'fts for realz'

mylist = [];

for letter in myword:
    mylist.append(letter)
    
print(mylist) #--> ['f', 't', 's', ' ', 'f', 'o', 'r', ' ', 'r', 'e', 'a', 'l', 'z']

#easier way is list comprehension:
mylist = [element for element in 'Whatever String'] #--> ['W', 'h', 'a', 't', 'e', 'v', 'e', 'r', ' ', 'S', 't', 'r', 'i', 'n', 'g']

mylist3 = [num for num in range(0,8)]
print(mylist3)

#can even do operations
mylist4 = [num**2 for num in range(0,4)]
print(mylist4)

#Can even add in IF statements
mylist5 = [x for x in range(0,11) if x%2==0]
print(mylist5)

#another example
celcius = [0, 10, 20, 34.5, 100]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

#refactored
fahrenheit2 = []
for temp in celcius:
    fahrenheit2.append((9/5)*temp + 32)
print(fahrenheit2)

#if/else in list comprehension but not best practice as more un-readible
results = [x if x%2==0 else 'Odd' for x in range(1,11)]
print(results)

#nested for loops
mylist6 = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist6.append(x*y)
print(mylist6)

#refactored using list comprehension:
mylist7 = [a*b for a in [2,4,6] for b in [1,10,1000]]
print(mylist7)

#--------------------------------------------------------------------------------

#*args (Arguments) and **kwargs (keyword arguments)
def myfunc(a,b):
    #returns 5% of the sum of a & B
    return sum((a,b)) * 0.05

#can only give in 2 args here but *args allows for however many!  Creates a tuple of arguments
#*args can be any word ie: *spam if followed by asterisk but convention is "args"
def myfunc1(*args):
    return sum(args) * 0.05

print(myfunc1(40,60,1, 34))

#**kwargs creates a dictionary of keyword:value pairs.
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit = 'apple', veggie = 'lettuce')

#can even accept both!
def myfunc2(*args, **kwargs):
    print(args,kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
          
myfunc2(10,33,20,30,fruit='apple',food='pizza',animals='neko',testing='fts')

#--------------------------------------------------------------------------------

#Lambda expressions are anonymous functions, so one time use functions that you dont name, just use once and never use again.
#      - #filter function needs a boolean, will filter for all true.
#we can re-write the square function we made to a lambda
lst = [1,2,3,4,5,6,7,8,9,10]

def square(num):
    return num**2

squaredList = list(map(square,lst))

squareLambda = lambda num: num ** 2

print(squareLambda(5))  #--> returns same as the function we defined.

# so if you only want to use once then no need to define a function and pass in, can just add the lambda code as the argument,
# similar to JavaScript filter((a,b){return a * b})

print(list(map(lambda num: num ** 2, evenSquaredList)))

print(list(filter(lambda num: num > 50, evenSquaredList)))

#--------------------------------------------------------------------------------
 #Namespace and Scope:
 lambda num:num *2 #-->local variable is num

name = 'This is GLOBAL scope'

def greet():
    name = 'this is ENCLOSING scope'
    
    def hello():
        name = 'LOCAL Scope'
        print('Hello ' + name)
    
    hello()

greet() #--> LEGB: WIll first return the local, then would look to enclosing, then would look to global, then would look
        #    to build in functions like len()

x = 50

def someFunc():  
    global x   # This is now telling python to use the global scope for the X Variable.
    print(f'X is {x}')
    
    #Local Reassignment on a now Gobal variable due to the key word!
    x = 200
    print(f'Now X is reassigned to {x}')

# Best practive though is to just to pass in the global variable as an argument then
# re-assign it ie: x = someFunc(x)

#--------------------------------------------------------------------------------

# set comparrisons tutorial

my_list = [1,1,2,2,3,3]
my_set = set(my_list)
print(my_set)
print()

# union combines two sets keeps only unique
a = {1,2,3}
b = {3,4,5}
c = a.union(b)
print(c)
print()

# intersection takes two sets and only returns whats in both
a = {1,2,3}
b = {3,4,5}
cc = aa.intersection(bb)
print(cc)
print()

# Difference takes anything in one set that is NOT in another!
a = {1,2,3}
b = {3,4,5}
ccc = aaa.difference(bbb)
ddd = bbb.difference(aaa)
print(ccc)
print(ddd)
print()

# Symmetric difference will filter out anything common in both Sets
a = {1,2,3}
b = {3,4,5}
cccc = a.symmetric_difference(b)
dddd = b.symmetric_difference(a)
print(cccc)
print()

# Subset, is A a subset of B?  Returns Boolean
aa = {1,2,3}
bb = {1,2,3,4,5}
c5 = aa.issubset(bb)
d5 = bb.issubset(aa)
print(c5)
print(d5)
print()

# SuperSet, does A have everything another set does, does A encompas B?
aaa = {1,2,3,4,5}
bbb = {1,2,3}
c6 = aaa.issuperset(bbb)
d6 = bbb.issuperset(aaa)
print(c6)
print(d6)

#--------------------------------------------------------------------------------

# Remove spaces from a string
st
'Just like the pied piper'.replace(" ",'')

#--------------------------------------------------------------------------------
