#!/usr/bin/env python3

from typing import Any


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
    def __init__(self, name = 'dog', breed = None):
        if(type(name) == str and len(name) > 0 and len(name) < 26):
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            return
        if breed in APPROVED_BREEDS:
                self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

            