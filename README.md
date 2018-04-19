
# Practice with Instance Variables

## Introduction
In this lab, we will practice using instance variables and differentiating them from local variables. We will continue with our awesome `fuber` theme. We have a couple files already provided for us in this directory, driver.py and ride.py. We will use these to define our classes and instance methods.

## Objectives

* Define instance variables.
* Distinguish instance variables from local variables.
* Describe how instance variables give objects attributes and properties.

## Defining Instance Variables

We have been writing functions and working with variables for a while now. We've talked about the difference between global variables and local variables. However, classes add another level of complexity with instance variables. Remember the difference between local and global variables is their scope. Local varibles have local or function scope, that is that they are only able to be accessed inside the function in which they are defined. Global variables can be accessed from anywhere in the file. Below is an example to jog your memory, if this is a little confusing:  


```python
name = "terrance" # global variable
def example_function():
    other_name = "jake" # local variable
    
print(name)
print(other_name)
```

    terrance



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-177fd1439fa8> in <module>()
          4 
          5 print(name)
    ----> 6 print(other_name)
    

    NameError: name 'other_name' is not defined


Again, our local variable is bound to its local or function scope, so when we try to print its value outside of the function it is undefined. This brings us to instance variables. They act similarly in that they are bound to their instance.

## Okay, but Why Do We Need Instance Variables?

Let's imagine we have two drivers. We istantiate them as instances of the `ExampleDriver` class and assign them to variables, `driver_one` and `driver_two`. Let's see this:


```python
class ExampleDriver:
    pass
    
driver_one = ExampleDriver()
driver_two = ExampleDriver()
print(driver_one)
print(driver_two)
```

    <__main__.ExampleDriver object at 0x10f3aa588>
    <__main__.ExampleDriver object at 0x10f3aa630>


Notice anything? Pretty hard to tell who is who... How can we fix this? We could probably give them names, right? That's where instance variables come in. Instance variables can be thought of as an attribute on an object. So, if we want our instance objects to have a `name` attribute, we simply need to add it to the object.


```python
driver_one.name = 'alex'
print(driver_one.name)
```

    alex


Great! We have made our first instance variable and we can now start to differentiate our instance objects and make them a bit more interesting. To reiterate, adding an attribute like `name` to an instance object is done by simply using the syntax, `variable-dot-attribute = value`. Let's add driver_two's name now, let's name them 'julian'.


```python
# add name to driver_two
```

Now, we can imagine these instance objects getting quite complex and we will want a way to look at the attributes -- similar to how we want to be able to look at the keys in a dictionary. Luckily for us, there is a method that shows us just that! `vars` is a method that returns a dictionary containing the keys and values that represent the attributes and values of an instance object. Let's see it in action:


```python
vars(driver_two)
```




    {'name': 'julian'}



Since `vars` returns a dictionary, we can even go a step further and just look at the attributes without their associated values by calling the `keys` method.


```python
vars(driver_two).keys()
```




    dict_keys(['name'])



Now, that we know how to add attributes as instance variables to our instance objects, let's look at how we would add an instance method as an attribute for our instance objects.


```python
class Person:
    def say_hello():
        print("Hi! How are you today?")
        
jeff = Person()
```

Okay, here we have defined an instance method called `say_hello` and an instance assinged to the variable, `jeff`. Let's try to call this method on our instance object, `jeff`: 


```python
jeff.say_hello()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-42-7ebd56e95aec> in <module>()
    ----> 1 jeff.say_hello()
    

    TypeError: say_hello() takes 0 positional arguments but 1 was given


Oh no! We got an error... :( 

`TypeError: say_hello() takes 0 positional arguments but 1 was given` as we can see we defined our method to not recieve any arguments. However, Python uses the instance object, `jeff` as the first argument of the instance method `say_hello`. So, this means Python is trying to pass in an argument into our method, but our method does not allow for any arguments. Don't worry about this behavior just yet, we can just define our instance method to take an argument and everything should work fine.


```python
class Person2:
    def say_hello(argument):
        print("Hi! How are you today?")
        
jeff2 = Person2()
```

Alright, round 2. Let's try this instance method again.


```python
jeff2.say_hello()
```

    Hi! How are you today?


Awesome! It worked. Again, we'll come back to exaclty what that `argument` is later. 

## Summary
In this lesson we saw how to define instance variables and saw how to use them in order to give our instance objects attributes and added complexity. We then saw how to define instance methods and call them on our instance objects. 
