# Editar planilha.py
from openpyxl import load_workbook


def edit(path, data):
    workbook = load_workbook(filename=path)
    sheet = workbook.active
    for cell in data:
        current_value = sheet[cell].value
        sheet[cell] = data[cell]
        print(f'Alterando {cell} de {current_value} para {data[cell]}')
        workbook.save(path)


if __name__ == "__main__":
    data = {"B1": "Hi", "B5": "Python"}
    edit("spreadsheets/planilhas/planilha_inserindo_dados.xlsx", data)
