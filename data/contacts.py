__author__ = 'pvarenik'
import random
import string
from model.contact import Contact


def random_str(prefix, maxlen):
    sym = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(sym) for i in range(random.randrange(maxlen))])

testdata = [Contact("", "", "", "")] + [
    Contact(name=random_str("name", 10), middlename=random_str("middlename", 10), lastname=random_str("lastname", 10), nickname=random_str("nickname", 10))
    for i in range(5)
]