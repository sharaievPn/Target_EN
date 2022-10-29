import random
import string

print(*(random.choices(string.ascii_lowercase, k=9)))
