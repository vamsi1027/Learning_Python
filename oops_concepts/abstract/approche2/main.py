from practices.OopsDeeper.abstract.approche2.hdfc_bank_info import HDFCBankAccountInfo
from practices.OopsDeeper.abstract.approche2.icici_bank_info import ICICIBankAccountInfo

if __name__ == '__main__':
    rbi_bank_update = HDFCBankAccountInfo()
    rbi_bank_update.bank_audit_statement()

    rbi_bank_update = ICICIBankAccountInfo()
    rbi_bank_update.bank_audit_statement()
