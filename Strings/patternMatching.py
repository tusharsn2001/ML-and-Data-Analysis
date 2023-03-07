import re


match = re.match('Hello[ \t]*(.*)world','Hello  Python world')
print(match.group(1))
#output - Python
'''This example searches for a substring that begins with the word “Hello,” followed by
zero or more tabs or spaces, followed by arbitrary characters to be saved as a matched
group, terminated by the word “world.” If such a substring is found, portions of the
substring matched by parts of the pattern enclosed in parentheses are available as
groups.'''

match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())
#output - ('usr', 'home', 'lumberjack')
