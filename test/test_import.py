from app.import_file.import_ofx import ImportOfx
from app.import_file.ofx_parser import OfxParser


def test_file_open():
    importer = ImportOfx('sample.ofx')
    contents = importer.import_ofx()
    assert contents is not None


def test_get_first_token():
    text = '<OFX><SIGNONMSGSRSV1><SONRS><STATUS>'
    parser = OfxParser([])
    index, token = parser.get_token(text, 0)
    assert token == '<OFX>'


def test_get_second_token():
    text = '<OFX><SIGNONMSGSRSV1><SONRS><STATUS>'
    parser = OfxParser([])
    start = 0
    start, token = parser.get_token(text, start)
    start, token = parser.get_token(text, start)
    assert token == '<SIGNONMSGSRSV1>'


def test_get_bank_info():
    importer = ImportOfx('sample.ofx')
    data = importer.import_ofx()
    assert data.bank_info is not None
    assert data.bank_info.routing_number is not None
    assert data.bank_info.account_number is not None
    assert data.bank_info.account_type is not None
