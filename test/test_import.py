import unittest
from app.import_file.import_ofx import ImportOfx


class TestImportFile(unittest.TestCase):

    def test_file_open(self):
        importer = ImportOfx('sample.ofx')
        contents = importer.import_ofx()
        self.assertIsNotNone(contents)

