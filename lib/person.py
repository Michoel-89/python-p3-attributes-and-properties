#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = 'Brian', job = None):
        
        if(type(name) == str and len(name) > 0 and len(name) < 26):
            self.name = name.title()
        else:
            return print("Name must be string between 1 and 25 characters.")
            
        if job in APPROVED_JOBS:
                self.job = job
        else:
            return print( "Job must be in list of approved jobs.")
            
