from dataclasses import dataclass


@dataclass
class MyOwnService:
    name: str
    location: str
    account: {}


my_account = MyOwnService("vamsi", "USA", {"bank ": 1234})
print(my_account.account)
