__author__ = 'pvarenik'
import random
import string
from model.contact import Contact
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["Number of parameters", "Configuration file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_str(prefix, maxlen):
    sym = string.ascii_letters# + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(sym) for i in range(random.randrange(maxlen))])

testdata = [Contact("", "", "", "")] + [
    Contact(name=random_str("name", 10), middlename=random_str("middlename", 10), lastname=random_str("lastname", 10), nickname=random_str("nickname", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
