#coding=utf-8
import study_05.烤地瓜
import pygame
class Dog:
    def __new__(cls):

        if cls ==None:
            return object.__new__(cls)
        else:
            return  cls

a=Dog()
print(id(a))

b=Dog()
print(id(b))
c=Dog();
print(id(c))
