import unittest
from app.import_file.import_ofx import ImportOfx
from app.import_file.ofx_parser import OfxParser


class TestImportFile(unittest.TestCase):

    def test_file_open(self):
        importer = ImportOfx('sample.ofx')
        contents = importer.import_ofx()
        self.assertIsNotNone(contents)

    def test_get_first_token(self):
        text = '<OFX><SIGNONMSGSRSV1><SONRS><STATUS>'
        parser = OfxParser([])
        index, token = parser.get_token(text, 0)
        self.assertEqual(token, '<OFX>')

    def test_get_second_token(self):
        text = '<OFX><SIGNONMSGSRSV1><SONRS><STATUS>'
        parser = OfxParser([])
        start = 0
        start, token = parser.get_token(text, start)
        start, token = parser.get_token(text, start)
        self.assertEqual(token, '<SIGNONMSGSRSV1>')

    def test_get_bank_info(self):
        importer = ImportOfx('sample.ofx')
        data = importer.import_ofx()
        self.assertIsNotNone(data.bank_info.routing_number)
        self.assertIsNotNone(data.bank_info.account_number)
        self.assertIsNotNone(data.bank_info.account_type)
