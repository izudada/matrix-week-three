import re


class EmailParser:
    # regex pattern that validate email
    pattern = r'^[a-z0-9]+[\+]?[a-z0-9]+[@]\w+\.com$'
    keys = ['username', 'domain']

    def parse(self, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''
        # Add implementation here ...
        data = re.split('@', email)
        if re.match(self.pattern, email):
            return self.convert_to_dict(data[0], data[1])

    def convert_to_dict(self, user, dom):
        '''
          Takes in two lists as params and return them as a dictionary.'''  
        user_info  = {
            self.keys[0] : user,
            self.keys[1] : dom
        }
        
        return user_info

user1 = EmailParser()

info = 'tony+udeagbala@gmail.com'

print(user1.parse(info))