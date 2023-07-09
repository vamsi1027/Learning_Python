from practices.OopsDeeper.inheritance.center_government import CentralGovernment
from practices.OopsDeeper.inheritance.andhra_pradesh_state_budget import AndhraPradeshStateBudget

if __name__ == "__main__":
    center_government = CentralGovernment('Modi Government')
    center_government.state_budget()
    center_government.details_reports_state_budget()

    andrea_state_budget = AndhraPradeshStateBudget('Jagan CM', True)
    andrea_state_budget.state_budget()
    andrea_state_budget.details_reports_state_budget()
