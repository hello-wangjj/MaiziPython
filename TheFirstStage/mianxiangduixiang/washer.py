#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2017021313:51'
__doc__='''
属性包装
'''

class washer():

    def __init__(self, water=10, scour=2):
        self._water = water
        self.scour = scour
        self.year = 2010

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, water):
        if 0 < water < 500:
            self._water = water
        else:
            print('set failure!')

    @property
    def total_year(self):
        return 2016 - self.year

if __name__ == '__main__':
    w = washer()
    print(w.water)
    w.water = 200
    print(w.water)
    w.water = 600
    print(w.total_year)
