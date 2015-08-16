from livingroom import LivingRoom

from pprint import pprint
import random

NUMBER_OF_HOSTAGES = 100

class Prison(object):
    def __init__(self, hostages):
        self.hostages = hostages

        if len(hostages) != NUMBER_OF_HOSTAGES:
            raise TooFewHostagesError("There must be exactly %s hostages" % NUMBER_OF_HOSTAGES)
        self.livingroom = LivingRoom()
        self.livingroom_register = []

    def check_if_hostages_must_be_released(self):
        hostage = self.pick_hostage()
        self.livingroom_register.append(hostage)

        light = self.livingroom.get_light()
        toggle = hostage.visit_livingroom(light)
        if toggle:
            self.livingroom.toggle_light()

        return hostage.were_all_hostages_in_livingroom()


    def pick_hostage(self):
        return random.choice(self.hostages)

    def were_all_hostages_in_livingroom(self):
        return set(self.livingroom_register) == set(self.hostages)


class TooFewHostagesError(ValueError):
    pass
