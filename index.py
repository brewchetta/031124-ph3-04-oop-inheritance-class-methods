from classes.bird import Bird
from classes.cat import Cat
from classes.dog import Dog
from classes.fish import Fish
from classes.mammal import Mammal

def something(something, **kwargs):
    for arg in kwargs:
        print(arg)