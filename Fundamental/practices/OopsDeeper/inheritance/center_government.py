class CentralGovernment:
    def __init__(self, name):
        print('Central Government Budget: %s')
        self.name = name

    def state_budget(self) -> object:
        print(f"State budget been initialized soon from {self.name}")

    @classmethod
    def details_reports_state_budget(cls) -> object:
        print("Notice: Details reports state budget should be initialized from from Central Government")
