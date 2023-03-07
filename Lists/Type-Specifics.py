
# Lists can grow and shrink on demand

L = [123,'spam',1.23]
L.append('New') #append adds object at end of List
print(L)
#output - [123, 'spam', 1.23, 'New']

L.pop()  # pop delete object at end of the List
print(L)
#output - [123, 'spam', 1.23]

# or we can state index in pop 
L.pop(1)
print(L)
#output - [123, 1.23]


# Soting a List

M = ['bb','aa','cc']
M.sort()
print(M)
#ouput - ['aa', 'bb', 'cc']

M.reverse()
print(M)
