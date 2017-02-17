#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2017021613:31'


def deco(a_class):
    class NewClass:

        def __init__(self, age, color):
            self.wrapped = a_class(age)
            self.color = color

        def display(self):
            print('deco')
            print(self.wrapped.age)
            print(self.color)
    return NewClass


@deco
class Cat:

    def __init__(self, age):
        self.age = age

    def display(self):
        print('display')
        print(self.age)

if __name__ == '__main__':
    c = Cat(12, 'red')
    c.display()
