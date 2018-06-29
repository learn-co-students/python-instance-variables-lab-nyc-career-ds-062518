# define driver class here
class Driver:

    def passenger_names(self):
        passengers = []
        for person in self.passengers:
            passengers.append(person.name)
        return passengers
