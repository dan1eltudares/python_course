'''
# Rember our password checker? Lets write the password checker
# again but this time it will let users know if their caps lock is on!
# If the password is correct, the function will return
# 'Access Granted'
# If the password is correct, but in all capitals the function will return
# 'Access Denied, make sure your caps lock is off'
# If the password is incorrect, the function will return
# 'Access Denied'

"""
reminder!
if condition:
  code
elif condition:
  code
else:
  code
"""
'''

def dt_password_check(pwd):
    if pwd == 'chuckribas':
        return 'Access Granted'
    elif pwd == 'CHUCKRIBAS':
        return 'Access Denied, make sure your caps lock is off'
    else:
        return 'Access Denied'

print("test 1: ", dt_password_check('chuckribas') == 'Access Granted')
print("test 2: ", dt_password_check('churchribas') == 'Access Denied')
print("test 3: ", dt_password_check('CHUCKRIBAS') == 'Access Denied, make sure your caps lock is off')
