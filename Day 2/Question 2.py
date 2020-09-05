print('Questions 2. Dictionary and its default functions.')
student = {
	'name': 'first one',
	'age': 19,
	'no. of subjects': 4
}
# 1 get() - Return the value for key if key is in the dictionary, else default.
print(student.get('name'))
# 2 update - to update key, values
student.update({'name': 'another one', 'age': 20})
print(student)
# 3 pop() - remove specified key and return the corresponding value.
student.pop('name')
print(student)
# 4 keys() - a set-like object providing a view on D's keys
print(student.keys())
# 5 values() - an object providing a view on D's values
print(student.values())