# see https://pynative.com/python-generate-random-string/
import random
import string

def randomString(stringLength=10, alpha=string.ascii_lowercase):
    """Generate a random string of fixed length """
    return ''.join(random.choice(alpha) for i in range(stringLength))