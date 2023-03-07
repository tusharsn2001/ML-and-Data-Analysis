'''One nice feature of Python’s core data types is that they support arbitrary nesting—we
can nest them in any combination, and as deeply as we like (for example, we can have
a list that contains a dictionary, which contains another list, and so on). One immediate
application of this feature is to represent matrixes, or “multidimensional arrays” in
Python.'''


M = [[1,2,3],  # A 3 × 3 matrix, as nested lists
     [4,5,6],   # Code can span lines if bracketed
     [7,8,9]]

print(M)
#output - [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Accesing items

print(M[1])  # Get row 1
#output - [4, 5, 6]

print(M[1][0]) #  Get row 1 , then get item 0 within row 1
#output - 4


''' List Comprehenssion in Python'''

col2 = [row[1] for row in M]  # Collect the items in column 2
print(col2)
#output - [2, 5, 8]



# List comprehensions can be more complex in practice:

print([row[1] + 1 for row in M]) # Add 1 to each item in column 2
#output - [3, 6, 9]

print([row[1] for row in M if row[1] % 2 == 0]) # Filter out odd items
#output - [2, 8]

diag = [M[i][i] for i in [0, 1, 2]] # Collect a diagonal from matrix
print(diag)
#output - [1,5,9]

doubles = [c * 2 for c in 'spam']  # Repeat characters in a string
print(doubles)
#output - ['ss', 'pp', 'aa', 'mm']


'''comprehension syntax in
parentheses can also be used to create 
generators that produce results on demand (the
sum built-in, for instance, sums items in a sequence):'''

G = (sum(row) for row in M )  # Create a generator of row sums
print(next(G))
#ouptut - 6
print(next(G))
#ouptut - 15
print(next(G))
#ouptut - 24


