
class Horse:  # This class creates a Horse

    def __init__(self, name, speed, stamina, endurance):
        self.name = name
        self.speed = speed
        self.stamina = stamina
        self.endurance = endurance
        self.cur_pos = 0  # this value is used to represent a horse on the map in track.py

    def update_speed(self):  # this function updates the horses speed value during the race
        self.speed *= self.stamina


class SkeletonHorse(Horse):  # this child class overwrites the function above to give the horse infinite stamina
    def update_speed(self):
        pass
