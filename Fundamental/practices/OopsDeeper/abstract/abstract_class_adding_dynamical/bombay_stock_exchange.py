# import abc
#
#
# class BombayStockExchange(metaclass=abc.ABCMeta):
#     pass
#
#
# def add_abstract_method(cls, name):
#     cls._abstract_registry.clear()
#     setattr(cls, name, abc.abstract_method(lambda self: None))
#     cls.__abstract_methods__ = frozenset(cls.__abstract_method__ | {name})
#     cls._abc_registry = None
#
#
# add_abstract_method(BombayStockExchange, "UpStockBrokerage")
# add_abstract_method(BombayStockExchange, "ZerodhaBrokerage")
#
#
#
#
#
# The update_abstractmethods method is a special method in Python that is used to update the abstract methods of a class. Abstract methods are methods that are declared in an abstract base class but have no implementation. Any class that inherits from the abstract base class must implement all of its abstract methods.
#
# The update_abstractmethods method is typically used in the metaclass of the abstract base class. It is called whenever a subclass is created and updates the abstract methods of the subclass with any new abstract methods that may have been added to the parent class.
#
# Here is an example of how the update_abstractmethods method can be implemented:
#
# python
# Copy code
# class MyMeta(type):
#     def __new__(cls, name, bases, attrs):
#         new_class = super().__new__(cls, name, bases, attrs)
#         new_class.update_abstractmethods()
#         return new_class
#
# class MyBaseClass(metaclass=MyMeta):
#     def __init__(self):
#         pass
#
#     @abstractmethod
#     def my_abstract_method(self):
#         pass
#
# class MySubClass(MyBaseClass):
#     def my_concrete_method(self):
#         pass
#
# MySubClass()  # raises TypeError: Can't instantiate abstract class MySubClass with abstract methods my_abstract_method
# In this example, we define a metaclass MyMeta that inherits from the type metaclass. The __new__ method of the metaclass is overridden to call the update_abstractmethods method on any newly created class.
#
# We then define an abstract base class MyBaseClass that has one abstract method my_abstract_method. This class is defined with the @abstractmethod decorator, which indicates that any subclass must implement this method.
#
# Finally, we define a subclass MySubClass of MyBaseClass that defines a concrete method my_concrete_method. When we try to instantiate MySubClass, we get a TypeError because we haven't implemented the abstract method my_abstract_method.
#
# To fix this, we can add an implementation for my_abstract_method in MySubClass:
#
# python
# Copy code
# class MySubClass(MyBaseClass):
#     def my_concrete_method(self):
#         pass
#
#     def my_abstract_method(self):
#         pass
#
# MySubClass()  # no longer raises TypeError
# Now that we have implemented my_abstract_method in MySubClass, we can instantiate the class without any errors.
#
#
#
#
# koka vamsikrishna
# update_abstractmethods use of the python
# The update_abstractmethods method is a method in Python's built-in abc module that is used to update the abstract methods of a class. It is typically used in the metaclass of an abstract base class to ensure that any subclass that inherits from it implements all of its abstract methods.
#
# Here's an example of how update_abstractmethods can be used in Python:
#
# python
# Copy code
# import abc
#
# class MyBaseClass(abc.ABC):
#     @abc.abstractmethod
#     def my_abstract_method(self):
#         pass
#
# class MySubClass(MyBaseClass):
#     def my_concrete_method(self):
#         pass
#
# MySubClass()  # raises TypeError: Can't instantiate abstract class MySubClass with abstract methods my_abstract_method
# In this example, we define an abstract base class MyBaseClass using Python's built-in abc module. This class has one abstract method my_abstract_method, which is declared with the @abc.abstractmethod decorator.
#
# We then define a subclass MySubClass of MyBaseClass that defines a concrete method my_concrete_method. When we try to instantiate MySubClass, we get a TypeError because we haven't implemented the abstract method my_abstract_method.
#
# To fix this, we can add an implementation for my_abstract_method in MySubClass:
#
# python
# Copy code
# class MySubClass(MyBaseClass):
#     def my_concrete_method(self):
#         pass
#
#     def my_abstract_method(self):
#         pass
#
# MySubClass()  # no longer raises TypeError
# Now that we have implemented my_abstract_method in MySubClass, we can instantiate the class without any errors.
#
# If we want to ensure that any new abstract methods added to MyBaseClass are also added to its subclasses, we can use the update_abstractmethods method. Here's an example:
#
# python
# Copy code
# class MyMeta(abc.ABCMeta):
#     def __new__(cls, name, bases, attrs):
#         new_class = super().__new__(cls, name, bases, attrs)
#         abc.ABCMeta.__init__(new_class)
#         return new_class
#
# class MyBaseClass(metaclass=MyMeta):
#     @abc.abstractmethod
#     def my_abstract_method(self):
#         pass
#
# class MySubClass(MyBaseClass):
#     def my_concrete_method(self):
#         pass
#
# MyBaseClass.register(AnotherSubClass)
#
# class AnotherSubClass(MyBaseClass):
#     def another_abstract_method(self):
#         pass
#
# MySubClass()  # raises TypeError: Can't instantiate abstract class MySubClass with abstract methods my_abstract_method
# AnotherSubClass()  # raises TypeError: Can't instantiate abstract class AnotherSubClass with abstract methods my_abstract_method
# In this example, we define a metaclass MyMeta that inherits from abc.ABCMeta. The __new__ method of the metaclass is overridden to call the abc.ABCMeta.__init__ method on any newly created class. This ensures that the class is registered with the abc.ABCMeta metaclass and that its abstract methods are tracked.
#
# We then define an abstract base class MyBaseClass that has one abstract method my_abstract_method. This class is defined with the @abc.abstractmethod decorator, which indicates that any subclass must implement this method.
#
# We define two subclasses MySubClass and AnotherSubClass of MyBaseClass. MySubClass only implements the my_concrete_method method, while AnotherSubClass implements an additional abstract method another_abstract_method.
#
# We then use the registerister method to register AnotherSubClass with MyBaseClass.
