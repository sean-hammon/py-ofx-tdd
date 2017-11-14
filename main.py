from app.import_file.import_ofx import ImportOfx


def main():
    ofx_data = ImportOfx("sample.ofx")
    ofx_data.import_ofx()


if __name__ == "__main__":
    main()