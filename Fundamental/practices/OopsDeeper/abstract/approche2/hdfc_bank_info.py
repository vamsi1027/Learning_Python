from dataclasses import dataclass, fields
from typing import Optional
from practices.OopsDeeper.abstract.approche2.rbi_bank_info import IRBIBankInformation


@dataclass
class HDFCBankAccountInfo(IRBIBankInformation):
    banch_name = Optional[str] = None
    toke: str = fields(repr=False, default=None)

    def bank_audit_statement(self):
        print("HDFC Audit Statement is initialized on oct 22nd 2023")
