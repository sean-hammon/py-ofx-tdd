from app.import_file.ofx_file import OfxFile
from app.import_file.ofx_transaction import OfxTransaction


class OfxParser:

    def __init__(self, contents):
        self.lines = contents
        self.file_object = OfxFile()
        self.current_tx = None

    def parse(self):
        #   Discard file header data
        lines = self.lines[10:]

        for line in lines:

            #   Assuming a line will always start with a tag.
            if line[0] != '<':
                raise ValueError('We appear to have encountered invalid data: ' + line)

            start = 0
            stop = len(line)

            while start >= 0 and start != stop:
                start, token = self.get_token(line, start)
                if token[0:2] == "</":
                    if token == "</STMTTRN>":
                        self.file_object.transactions.append(self.current_tx)
                    continue

                start, value = self.get_token(line, start)

                if value[0:2] == "</":
                    continue

                while start > 0 and value[0] == "<":
                    self.token_identify(token)
                    token = value
                    start, value = self.get_token(line, start)

                self.token_identify(token, value)

        return self.file_object

    def get_token(self, line, start):
        if line[start] == '<':

            #   We're looking at a tag, we need to find the end
            #   of the tag.

            end = line.find('>', start) + 1
        else:

            #   We're looking at a value, we need to find
            #   the beginning of the next tag.

            end = line.find('<', start)

        token = line[start:end]
        return [end, token]

    def token_identify(self, token, value=None):
        if token == '<DTSERVER>':
            self.file_object.date_generated = value
        elif token == '<LANGUAGE>':
            self.file_object.language = value
        elif token == '<CURDEF>':
            self.file_object.currency = value
        elif token == '<BANKID>':
            self.file_object.bank_info.routing_number = value
        elif token == '<ACCTID>':
            self.file_object.bank_info.account_number = value
        elif token == '<ACCTTYPE>':
            self.file_object.bank_info.account_type = value
        elif token == '<DTSTART>':
            self.file_object.lower_bound_date = value
        elif token == '<DTEND>':
            self.file_object.upper_bound_date = value
        elif token == '<STMTTRN>':
            self.current_tx = OfxTransaction()
        elif token == '<TRNTYPE>':
            self.current_tx.type = value
        elif token == '<DTPOSTED>':
            self.current_tx.date_posted = value
        elif token == '<TRNAMT>':
            self.current_tx.amount = float(value)
        elif token == '<FITID>':
            self.current_tx.fitid = value
        elif token == '<NAME>':
            self.current_tx.name = value
        elif token == '<CHECKNUM>':
            self.current_tx.check_number = value
        elif token == '<MEMO>':
            self.current_tx.memo = value
