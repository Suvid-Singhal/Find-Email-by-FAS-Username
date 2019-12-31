from fedora.client.fas2 import AccountSystem
import re

fas = AccountSystem(username='<Your FAS Username>', password='<Your FAS Password>')

user_id = input()

ret_val = fas.people_by_key(key='email', search=user_id, fields=['id'])

email = str(ret_val.keys()).split("'")[1::2]
print('\n'.join(email))
