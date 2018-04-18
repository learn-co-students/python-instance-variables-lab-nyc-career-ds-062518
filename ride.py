class Ride:
    def __init__(self):
        self.distance_driven = 0

    def set_distance(self, trip_distance):
        self.distance_driven += trip_distance
        return self.distance_driven

    def get_distance(self):
        return self.distance_driven
