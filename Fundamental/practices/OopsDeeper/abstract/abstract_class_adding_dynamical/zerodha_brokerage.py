import abc


class ZerodhaBrokerage(abc.ABC):
    @abc.abstractmethod
    def equality_trading(self):
        pass
