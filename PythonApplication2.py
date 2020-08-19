'''Python program to find who passed and who did not from a class
1. A list of students who failed has been set
2. User enter student name.
3. Returns students who passed.'''

black_list = ['Susan', 'John', 'Mick', 'Ron']

num_students = int(input('Enter number of students: '))
student_list = []
white_list = []
for student in range(num_students):
    prompt = input('Input a name: ')
    while prompt == '':
        prompt = input('Input a non empty name: ')
    student_list.append(prompt)
for student in student_list:
    if student not in black_list:
        white_list.append(student)
print('These ' + str(len(white_list)) + ' students passed.')
print(*sorted(white_list), sep='\n')

