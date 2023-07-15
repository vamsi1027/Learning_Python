from practices.OopsDeeper.inheritance.center_government import CentralGovernment


class AndhraPradeshStateBudget(CentralGovernment):

    def __init__(self, name, satisfied):
        super().__init__(name)
        print("AP State budget")
        self.name = name
        self.satisfied = satisfied

    def state_budget(self, accepted) -> object:
        print(f"State budget been accepting the {self.name, self.satisfied}")

    @classmethod
    def details_reports_state_budget(cls) -> object:
        print("Details reports AndhraPradeshStateBudget should be initialized")
