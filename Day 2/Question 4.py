print('Questions 4. Tuple and explore default methods.')
tple = ('this', 'is', 'a', 'tuple')
print(tple)
# 1 index() - Searches the tuple for a specified value and returns the position of where it was found
address = tple.index('is')
print(address)
# 2 count() - Returns the number of times a specified value occurs in a tuple
numb = tple.count('a')
print(numb)
# 3 len() - return the length of the tuple
print(len(tple))
# 4 min() - return item from the tuple with max value.
tple2 = (4, 6, 9, 2, 3)
print(min(tple2))
# 5 max() - Returns item from the tuple with max value.
print(max(tple2))