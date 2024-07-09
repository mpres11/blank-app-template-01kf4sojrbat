import pandas as pd

class DataImport:
    """
    This is a docstring, man.
    """

    def __init__(self):
        pass


    def fetch_and_clean_data():
        df = pd.read_excel('national-register-listed-20240115.xlsx', engine='openpyxl')
        return df

