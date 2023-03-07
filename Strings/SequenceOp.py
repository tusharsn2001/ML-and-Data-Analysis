str = "Welcome"
print(len(str))
#output - 7
print(str[0])
#output - W

#Backward Indexing

print(str[-1])
#output - e
print(str[-2])
#output - m\

#negative indexing hard way

print(str[len(str)-1])
#output - e

#Slicing in Sequences

print(str[2:len(str)-2])
#output - lco
print(str[:3]) # Same as str[0:3]
#output - Wel
print(str[:-1]) # Everything but the last again, but simpler (0:-1)
#output - Welcom
print(str[:])  # All of str as a top-level copy (0:len(str))
#output - Welcome


#Concatenation And Repetition

print(str+' To Python') #Concatenation
#output - Welcome To Python
print(str*3) #Repetition
#output - WelcomeWelcomeWelcome

# IMMUTABILITY

''' 
Notice that in the prior examples, we were not changing the original string with any of
the operations we ran on it. Every string operation is defined to produce a new string
as its result, because strings are immutable in Python—they cannot be changed in-place
after they are created. For example, you can’t change a string by assigning to one of its
positions, but you can always build a new one and assign it to the same name. Because
Python cleans up old objects as you go (as you’ll see later), this isn’t as inefficient as it
may sound:
>>> str
'Welcome'
>>> str[0] = 'W' # Immutable objects cannot be changed
...error text omitted...
TypeError: 'str' object does not support item assignment
>>> str = 'z' + str[1:] # But we can run expressions to make new objects
>>> str
'zelcome'
Every object in Python is classified as either immutable (unchangeable) or not. In terms
of the core types, numbers, strings, and tuples are immutable; lists and dictionaries are
not (they can be changed in-place freely). Among other things, immutability can be
used to guarantee that an object remains constant throughout your program.
'''