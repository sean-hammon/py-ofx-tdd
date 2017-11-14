from app.import_file.ofx_bank import OfxBank


class OfxFile:

    def __init__(self):
        self.date_generated = None
        self.language = None
        self.currency = None
        self.bank_info = OfxBank()
        self.lower_bound_date = None
        self.upper_bound_date = None
        self.transactions = []
