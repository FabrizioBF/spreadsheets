# Apagar dados
from openpyxl import Workbook


def deleting_cols_rows(path):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Brasil"
    sheet["B1"] = "Argentina"
    sheet["C1"] = "Chile"
    sheet["A2"] = "linha 2"
    sheet["A3"] = "linha 3"
    sheet["A4"] = "linha 4"
    # Apgar coluna A
    sheet.delete_cols(idx=1)
    # Apagar 2 linhas iniciando na segunda linha
    sheet.delete_rows(idx=2, amount=2)
    workbook.save(path)


if __name__ == "__main__":
    deleting_cols_rows("planilha_apagando_dados.xlsx")
    print("Operação realizada com sucesso!")
