user_id = input('id? ')
user_pwd = input('password? ')


'''
if user_pwd == '1111':
    print('correct')
else:
    print('incorret')
'''
'''
if user_id == 'atesi':
    if user_pwd == '1111':
        print('correct')
    else:
        print('incorret')
else:
    print('who are you? ')
'''

if user_id == 'atesi' and user_pwd == '1111':
    print('hello', user_id)
elif user_id == 'ate' and user_pwd == '1234':
    print('hello', user_id)
else:
    print('who are you? ')
