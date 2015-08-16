import random

class Hostage(object):
    def __init__(self, id):
        self.id = id
    
    def __repr__(self):
        return 'Hostage(id=%s)' % (self.id)

    def visit_livingroom(self, light):
        return True

    def were_all_hostages_in_livingroom(self):
        return False


class RatHostage(Hostage):
    def __repr__(self):
        return 'RatHostage(id=%s)' % (self.id)

    def visit_livingroom(self, light):
        return True

    def were_all_hostages_in_livingroom(self):
        return random.choice([True, False, False, False, False, False, False, False, False, False])
