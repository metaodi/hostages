class LivingRoom(object):
    light = False

    def toggle_light(self):
        self.light = not self.light

    def get_light(self):
        return self.light
