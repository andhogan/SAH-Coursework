# Exercise 1
# Create a GoldenRetriever class that inherits from the Dog class. 
# Give the sound argument of the GoldenRetriever.speak() method a default value of "Bark". 
# Use the following code for your parent Dog class:

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
#Check work:
fido = GoldenRetriever("Fido", 5)
fido.speak()