print('Questions 3. Sets and its default functions.')
sett = {'some', 'items' ,'of', 'sett'}
print(sett)
# 1 add() - to add element to the set
sett.add('new')
print(sett)
# 2 discard() - remove the specified item of the set
sett.remove('some')
print(sett)
# 3 pop() - remove an element of set
sett.pop()
print(sett)
# 4 remove() - remove the specified element
sett.remove('new')
print(sett)
# 5 clear() - removes all the elements of the set
sett.clear()
print(sett)