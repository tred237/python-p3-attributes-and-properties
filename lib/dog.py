#!/usr/bin/env python3
import ipdb

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = '', breed = ''):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        # ipdb.set_trace()
        if ((type(name) == str) and (1 <= len(name) <= 25)):
            self._name = name
        else:
            print('Name must be string between 1 and 25 characters.')

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        # ipdb.set_trace()
        # if not hasattr(self, 'name'):
        #     return

        if (breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print('Breed must be in list of approved breeds.')

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


d = Dog(name = "")