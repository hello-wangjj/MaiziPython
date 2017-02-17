#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2017021611:57'


class MoveAble:

    def move(self):
        print('Move...')


class MoveOnFeet(MoveAble):

    def move(self):
        print('move on feet...')


class MoveOnWheel(MoveAble):

    def move(self):
        print('move on wheel...')


class MoveObj:

    def set_move(self, move_albe):
        self.move_able = move_albe()

    def move(self):
        self.move_able.move()


if __name__ == '__main__':
    m = MoveObj()
    m.set_move(MoveAble)
    m.move()
    m.set_move(MoveOnFeet)
    m.move()
    m.set_move(MoveOnWheel)
    m.move()
