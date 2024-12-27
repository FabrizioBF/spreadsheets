# Inserindo dados
from openpyxl import Workbook


def inserting_cols_rows(path):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Brasil"
    sheet["A2"] = "Argentina"
    sheet["A3"] = "Chile"
    sheet.insert_cols(idx=1)
    sheet.insert_rows(idx=2, amount=2)
    workbook.save(path)


if __name__ == "__main__":
    inserting_cols_rows("planilha_inserindo_dados.xlsx")
