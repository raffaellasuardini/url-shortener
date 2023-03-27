import string
import random
from datetime import datetime

allowed_char = string.ascii_letters + string.digits
random.seed(datetime.now())

def create_random_short_url(length) :
    result_str = ''.join(random.choice(allowed_char) for i in range(length))
    return result_str

