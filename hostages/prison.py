from hostages.livingroom import LivingRoom
import random


class Prison(object):
    def __init__(self, hostages, number_of_hostages):
        self.hostages = hostages

        if len(hostages) != number_of_hostages:
            raise TooFewHostagesError(
                "There must be exactly %s hostages"
                % number_of_hostages
            )
        self.livingroom = LivingRoom()
        self.livingroom_register = []

    def attempt_to_release_hostages(self):
        self.notify_hostages()
        hostage = self.pick_hostage()
        self.livingroom_register.append(hostage)

        light = self.livingroom.get_light()
        new_light = hostage.visit_livingroom(light)
        self.livingroom.set_light(new_light)

        return hostage.were_all_hostages_in_livingroom()

    def notify_hostages(self):
        map(lambda h: h.start_new_day(), self.hostages)

    def pick_hostage(self):
        return random.choice(self.hostages)

    def were_all_hostages_in_livingroom(self):
        return set(self.livingroom_register) == set(self.hostages)


class TooFewHostagesError(ValueError):
    pass
