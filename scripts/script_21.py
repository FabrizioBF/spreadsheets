# Congelar linhas e colunas.py
from openpyxl import Workbook


def freeze(path, row_to_freeze):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Freeze"
    sheet.freeze_panes = row_to_freeze
    headers = ["Nome", "Endereço", "Estado", "Cep", "Profissão"]
    sheet["A1"] = headers[0]
    sheet["B1"] = headers[1]
    sheet["C1"] = headers[2]
    sheet["D1"] = headers[3]

    data = [dict(zip(headers, ("Mike", "098 Red Street", "CA", "50000", "Data Analyst"))), dict(
        zip(headers, ("Bill", "555 Blue Street", "NY", "80000", "Data Engineering"))), dict(
        zip(headers, ("Beatrice", "222 Orange Street", "TX", "70000", "Software Developer")))]
    row = 2
    for d in data:
        sheet[f'A{row}'] = d["Nome"]
        sheet[f'B{row}'] = d["Endereço"]
        sheet[f'C{row}'] = d["Estado"]
        sheet[f'D{row}'] = d["Cep"]
        sheet[f'D{row}'] = d["Profissão"]

        row += 1
        workbook.save(path)


if __name__ == "__main__":
    freeze("freeze.xlsx", row_to_freeze="A2")
