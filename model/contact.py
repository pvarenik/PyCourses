__author__ = 'pvarenik'
from sys import maxsize

class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id

    def __repr__(self):
        return "%s,%s,%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize