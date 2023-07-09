from abc import ABCMeta, abstractmethod


class ObserverABC(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        # print("==================="+subject)
        """should implement update() method"""
