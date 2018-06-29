# define driver class here
class Driver:
    def passenger_names(self):
        passenger_names = []
        for passenger in self.passengers:
            passenger_names.append(passenger.name)
        return passenger_names
