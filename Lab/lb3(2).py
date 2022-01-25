# person = {
#     'fname': 'abc',
#     'lname': 'bcd',
#     'age': '23',
#     'city': 'bangalore',
#     'skills': ['python', 'java', 'c++', 'JavaScript'],
#     'address': {
#         'street': 'space street',
#         'city': 'bangalore',
#         'state': 'karnataka',
#         'pincode': '560068'
#     }
# }

# print(person['fname'])
# print(person['skills'])
# print(person.get('city'))
# person['skills'].append('c')
# print(person['skills'])
# print('skills' in person)

# print(person.popitem())
# print(person.pop('fname'))

# print(person)

# # ---- # #
dog = {}
dog['name'] = 'buddy'
dog['color'] = 'brown'
dog['breed'] = 'labrador'
dog['age '] = '2'
dog['legs'] = '4'

student = {
    'first_name': 'john',
    'last_name': 'doe',
    'gender': 'male',
    'martial_status': 'Single',
    'skills': ['python', 'java', 'Javascript', 'HTML', 'React']
}
print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('c')
student['skills'].append('c++')
# print(len(student['skills']))
print(student.keys())
print(student.values())
print(list(student.items()))
student.pop(('martial_status'))

del dog
print(student)