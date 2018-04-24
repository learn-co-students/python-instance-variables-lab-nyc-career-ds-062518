
# Practice with Instance Variables

## Introduction
In this lab, we will practice using instance variables, and continue with our awesome `fuber` theme. In this directory, we have a couple files already provided for us, driver.py and passenger.py. We will use these to define our classes and instance methods.

## Objectives

* Define instance variables.
* Describe how instance variables give objects attributes and properties.

## Defining Instance Variables

We have been writing functions and working with variables for a while now. We've talked about the difference between global variables and local variables. However, classes add another level of complexity with instance variables. Remember the difference between local and global variables is their scope. Local varibles have local or function scope, that is that they are only able to be accessed inside the function in which they are defined. Global variables can be accessed from anywhere in the file. Below is an example to jog your memory, if this is a little confusing:  


```python
name = "terrance" # global variable
def example_function():
    other_name = "jake" # local variable
    print(other_name)

example_function() # executing fuction with local variable
print(name) # printing global variable
print(other_name) # printing local variable
```

Again, our local variable is bound to its local or function scope, so when we try to print its value outside of the function it is undefined. This brings us to instance variables. They act similarly in that they are bound to their instance. This means we define instance variables **on** instance objects. These instance variables are then only accessible through the instance on which they were defined.

The following is an example of adding an instance variable to an instance object and then accessing it later. Don't worry if it is confusing right now, the rest of this lesson will clear things up.


```python
class Person:
    pass

terrance = Person() # instantiating instance object from Person class called 'terrance'
terrance.first_name = "terrance" # adding an instance variable, first_name to the instance
print(terrance.first_name) # printing instance variable accessed from the instance
print(first_name) # undefined since it is not being accessed from the instance
```

## Okay, But Why Do We Need Instance Variables?

Let's imagine we have two drivers. We istantiate them as instances of the `ExampleDriver` class and assign them to variables, `driver_one` and `driver_two`. Let's see this:


```python
class ExampleDriver:
    pass
    
driver_one = ExampleDriver()
driver_two = ExampleDriver()
print(driver_one)
print(driver_two)
```

Notice anything? Pretty hard to tell who is who... How can we fix this? We could probably give them names, right? Well, how do we assign a name to these instances?

That's where instance variables come in. Instance variables can be thought of as an attribute on an object. So, if we want our instance objects to have a `name` attribute, we simply need to add it to the object.


```python
driver_one.name = 'alex'
print(driver_one.name)
```

Great! We have made our first instance variable and we can now start to differentiate our instance objects and make them a bit more interesting. To reiterate, adding an attribute like `name` to an instance object is done by simply using the following syntax: `variable-dot-attribute = value`. Let's add driver_two's name now, let's name them 'julian'.


```python
# add name to driver_two
```

Now, we can imagine wanting to add many instance variables to these instance objects which would make them quite complex. We will want a way to look at the instance variables -- similar to how we want to be able to look at the keys in a dictionary. Luckily for us, there is a method that shows us just that! 

`vars` is a method that returns a dictionary containing the keys and values that represent the instance variable names and values of an instance object. Let's see it in action:

> **Note:** instance variables and instance methods can both be referred to as `attributes` of an instance object. 


```python
vars(driver_two)
```

Since `vars` returns a dictionary, we can even go a step further and just look at the attributes without their associated values by calling the `keys` method.


```python
vars(driver_two).keys()
```

Awesome! As the note above states, instance variables aren't the only attribute. Our instance methods are also attributes, so, let's see again how we make those:


```python
class Person:
    def say_hello(self):
        print("Hi! How are you today?")
        
jeff = Person()
jeff.say_hello()
```

So, as we can see instance variables and instance methods look very similar syntactically. In fact, the main difference between the two is that instance methods are callable attributes on an instance object and instance variables are not callable. This makes sense since instance methods have a block of code to execute and instance variables do not. 

Remember how we said that there were a couple files provided for us? Let's put them to use and define both a Driver and a Passenger class -- for now just define the classes and remember to include the keyword `pass`. Below we'll import them and load the `autoreload` extension from IPython.


```python
%load_ext autoreload
%autoreload 2
```


```python
from driver.py import Driver
from passenger.py import Passenger
```

Now let's instantiate a new instance of a passenger and a new instance of a driver. Give the passenger a `rating` of `4.9` and give the driver a `miles_driven` attribute of `100,000`.


```python
driver = None # assign a driver instance
# give the driver instance object 'miles_driven' of 100000
passenger = None # assign the passenger instance
# give the passenger instance object a 'rating' of 4.9
```

Say we wanted to find a driver with a given name -- how would we do that? Let's take a look at how we could write a function that would take in a list of instance objects and return the one with the desired name. That sounds like the functionality we want.


```python
def find_driver_by_name(list_drivers, name):
    for driver in list_drivers:
        if driver.name == name:
            return driver
    return "Sorry we couldn't find a driver with the name, {}! :(".format('allison')
```


```python
alex_driver = Driver()
alex_driver.name = "alex"
michelle_driver = Driver()
michelle_driver.name = "michelle"
jake_driver = Driver()
jake_driver.name = "jake"
ashleigh_driver = Driver()
ashleigh_driver.name = "ashleigh"
list_of_drivers = [alex_driver, michelle_driver, jake_driver]
print(find_driver_by_name(list_of_drivers, "jake"))
print(find_driver_by_name(list_of_drivers, "allison"))
```

Cool! That looks like it worked. We can see that the method returns the Driver instance object when it finds an instance with the given name and returns a message saying that driver does not exist, if it cannot find a driver with that name. Now try writing a method that will return a list of instance objects that start with the letter `a`.


```python
# write your method here that returns the list of 
# drivers whose name starts which the letter 'a'
```

## Summary
In this lesson we saw how to define instance variables and saw how to use them in order to give our instance objects attributes and added complexity. We then saw how to define instance methods and call them on our instance objects. 

## Bonus

Okay, now let's work on creating more complex instance objects. Let's make a driver, `best_driver`, that has the attributes `name`, `car_make`, `car_model`, `age`, and `passengers`. The `passengers` attribute will point to a list of rider instances. The list of riders is already provided for you below:


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
best_driver = None # instantiate a driver
# add the name attribute and assign it 'Garol'
# add the car_make attribute and assign it 'toyota'
# add the car_model attribute and assign it 'camry'
# add the age attribute and assign it '30'
# add the passengers attribute and assign it to the list_of_passengers
```

Alright, great! Now we have some attributes on our driver that we can work with. Let's create an instance method in the Driver class called `passenger_names` which returns a list of all the passengers' names that a driver has driven (i.e. a driver's `passengers`). 
Your output should look like `['alex', 'michelle', 'jake', 'ashleigh']`.


```python
names_of_passengers = None # assign the return of best_driver.passenger_names()
```

If you would like to see a more formatted list, try calling the method below on the best_driver instance:


```python
def display_names(list_of_names):
    i = 1
    for name in list_of_names:
        print("{}. {}".format(i, name))
        i += 1

# call display_names with your list of passenger names
```

Neat -- great work! 
