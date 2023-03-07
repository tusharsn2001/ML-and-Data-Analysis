str = "Python"
# find Method

print(str.find('th')) #find thew offset of a SubString
#output - 2

# Replace occurrences of a substring with another
print( str.replace('Py','Mara')) 
#output - Marathon


# Split Method

line = 'aaa,bb,ccc,dd'
print(line.split(','))
#output - ['aaa', 'bb', 'ccc', 'dd']


''' Upper And Lower Case Conversions '''

S = 'spam'
print(S.upper()) # use upper() function for uppercase
#output - SPAM

L = S.upper()
print(L.lower()) # use lower() function for lowercase
#output - spam

print(L.isalpha()) # Content tests: isalpha, isdigit, etc.
#output - True

newLine = 'aa,bbb , ccc,d\n '
print(newLine.rstrip())  # Remove whitespace characters on the right side
#output - aa,bbb , ccc,d



''' Formatting '''

print('%s, eggs, and %s' % ('spam', 'SPAM!')) # Formatting expression (all)
#output - spam, eggs, and SPAM!

print('{0}, eggs, and {1}'.format('spam', 'SPAM!')) # Formatting method
#output - spam, eggs, and SPAM!


