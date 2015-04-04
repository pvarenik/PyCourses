__author__ = 'pvarenik'
from sys import maxsize

class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, id=None,
                 homephone=None, workphone=None, mobilephone=None, all_phones_from_home_page=None,
                 address=None, mail=None, mail2=None, mail3=None, all_mails_from_home_page=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.mail = mail
        self.mail2 = mail2
        self.mail3 = mail3
        self.all_mails_from_home_page = all_mails_from_home_page

    def __repr__(self):
        return "%s,%s,%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize