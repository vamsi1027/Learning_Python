import abc


class UpStockBrokerage(abc.ABC):
    @abc.abstractmethod
    def equality_trading(self):
        pass
