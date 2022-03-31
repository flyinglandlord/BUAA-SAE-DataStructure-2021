from abc import ABCMeta, abstractmethod

'''
通过这个例子可以看出，Python中的abstractmethod类似于Java中的接口interface
'''


class Progression(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        '''Constructure'''

    @abstractmethod
    def _advanced(self):
        '''next number'''

    @abstractmethod
    def __next__(self):  # 返回想要的下一个数字
        '''iter_related'''

    @abstractmethod
    def __iter__(self):  # 返回self即可
        '''iter_related'''

    @abstractmethod
    def print_progression(self, n):
        '''print the progression'''
