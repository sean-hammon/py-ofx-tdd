from app.import_file.ofx_parser import OfxParser

class ImportOfx:

    def __init__(self, filename):
        self.filename = filename

    def import_ofx(self):
        contents = self.read_ofx_file()
        parser = OfxParser(contents)
        parsed_data = parser.parse()

        return parsed_data

    def read_ofx_file(self):
        with open(self.filename) as f:
            file_contents = [line.strip() for line in f.readlines()]

        return file_contents
