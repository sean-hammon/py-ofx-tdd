import unittest


class TestImportFile(unittest.TestCase):

    def test_file_open(self):
        importer = ImportOfx('sample.ofx')
        contents = importer.import_ofx()
        self.assertIsNotNone(contents)

