import random
import string
password = ''.join(random.choice(string.ascii_uppercase + 
                                string.digits +
                                string.ascii_lowercase + 
                                string.punctuation) for x in range(12))
print("Your default secure password is: {}".format(password))

