class Driver():
    def passenger_names(self):
        passengers_driven = []
        for passenger in self.passengers:
            passengers_driven.append(passenger.name)
        return passengers_driven
# define driver class here
