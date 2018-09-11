
# Practice with Instance Variables

## Introduction
In this lab, we will practice using instance variables, which we use to store information about a particular instance object. We will use our `fuber` theme and create some methods that operate on our instance variables to return some valuable information about our passenger and driver instance objects.

## Objectives

* Define instance variables
* Describe how instance variables give objects attributes and properties

## Instructions

Below, define classes for both a Driver and a Passenger -- for now just define the classes and remember to include the keyword `pass` so that we will have valid syntax for our classes.


```python
# Driver class
class Driver:
    pass
```


```python
# Passenger class
class Passenger:
    pass
```

Now let's instantiate a new instance of a passenger and a new instance of a driver. Give the passenger a `rating` of `4.9` and give the driver a `miles_driven` attribute of `100,000`.


```python
driver = Driver() # assign a driver instance
# give the driver instance object 'miles_driven' of 100000
driver.miles_driven = 100000
passenger = Passenger() # assign the passenger instance
# give the passenger instance object a 'rating' of 4.9
passenger.rating = 4.9
```

Say we wanted to find a driver with a given name -- how would we do that? Well, we could define a function that takes in a list of driver instance objects and the name we are searching for. We'll have to check each driver instance for their name and see if it matches the one given.

If there are no drivers with the name we are searching, our function should return a message telling us it couldn't find that particular driver. For example, if we are looking for a driver named 'Jack' but cannot find one, we should get the message:
```python
"Sorry we couldn't find a driver with the name, Jack! :("
```


```python
alex_driver = Driver()
alex_driver.name = "alex"
alex_driver.rating = 9.0
michelle_driver = Driver()
michelle_driver.name = "michelle"
michelle_driver.rating = 8.0
jake_driver = Driver()
jake_driver.name = "jake"
jake_driver.rating = 9.7
ashleigh_driver = Driver()
ashleigh_driver.name = "ashleigh"
ashleigh_driver.rating = 8.75
list_of_drivers = [alex_driver, michelle_driver, jake_driver, ashleigh_driver]
```


```python
def find_driver_by_name(drivers, name):
    # write your code here
    for driver in drivers:
        if driver.name == name:
            return driver
    return f"Sorry we couldn't find a driver with the name, {name}! :("        
```


```python
print(find_driver_by_name(list_of_drivers, "jake"))
print(find_driver_by_name(list_of_drivers, "michelle"))
print(find_driver_by_name(list_of_drivers, "allison"))
```

Cool! That looks like it worked. We can see that the method returns the Driver instance object when it finds an instance with the given name and returns a message saying that driver does not exist, if it cannot find a driver with that name. Now try writing a method that will return a list of instance objects that start with a given substring like the letter `'a'`.


```python
# write your method here that returns the list of 
# drivers whose name starts which the letter 'a'
def name_starts_with(drivers, substring):
    return [driver for driver in drivers if driver.name.startswith(substring)]
```

Next, let's use our list of drivers to define a method that returns the driver with the highest rating.


```python
# write your method here that returns the driver with the highest rating
def highest_rated_driver(drivers):
    highest_rated = drivers[0]
    for driver in drivers:
        if driver.rating > highest_rated.rating:
            highest_rated = driver
    return highest_rated
```

## Summary
In this lesson we saw how to define instance variables and saw how to use them in order to give our instance objects attributes and added complexity. We then saw how to define instance methods and call them on our instance objects. 

## Bonus

Okay, now let's work on creating more complex instance objects with more interesting instance methods. Let's define a `NewDriver` class with an instance method called, `passenger_names`. Then, instantiate a new instance of the NewDriver class called `best_driver` that has the attributes `name`, `car_make`, `car_model`, `age`, and `passengers`. The `passengers` attribute will point to the list of passenger instances, which is provided below as `list_of_passengers`:


```python
class NewDriver:
    
    def passenger_names(self):
        # your code goes here
        pass
```


```python
alex_passenger = Passenger()
alex_passenger.name = "alex"
michelle_passenger = Passenger()
michelle_passenger.name = "michelle"
jake_passenger = Passenger()
jake_passenger.name = "jake"
ashleigh_passenger = Passenger()
ashleigh_passenger.name = "ashleigh"
list_of_passengers: [alex_passenger, michelle_passenger, jake_passenger, ashleigh_passenger]
```


```python
best_driver = None # instantiate a NewDriver instance object
# add the name attribute and assign it 'Garol'
# add the car_make attribute and assign it 'toyota'
# add the car_model attribute and assign it 'camry'
# add the age attribute and assign it '30'
# add the passengers attribute and assign it to the list_of_passengers
```

Alright, great! Now we have some attributes on our driver that we can work with. Let's create an instance method in the Driver class called `passenger_names` which returns a list of all the passengers' names/
Your output should look like `['alex', 'michelle', 'jake', 'ashleigh']`.


```python
names_of_passengers = None # assign the return of best_driver.passenger_names()
```

If you would like to see a more formatted list, try calling the method below on the best_driver instance:


```python
def display_names():
    i = 1
    for name in best_driver.passenger_names():
        print("{}. {}".format(i, name))
        i += 1

# call display_names to see a formatted list of names
```

Neat -- great work! 

## Summary

In this lab, we practiced creating instance variables that add information to our instance objects. We then used instance methods that used and operated on these instance variables to answer questions and return information about our instance objects.
