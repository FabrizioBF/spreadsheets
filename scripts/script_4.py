# Tarefa: ler células específicas
from openpyxl import load_workbook


def get_cell_info(path):
    workbook = load_workbook(filename=path)
    sheet = workbook.active
    print("\n", sheet)
    print(f'O título da planilha é: {sheet.title}')
    print(f'O valor de A2 é {sheet["A2"].value}')
    print(f'O valor de A3 é {sheet["A3"].value}')
    cell = sheet['B3']
    print(f'A variável "célula solicitada" é {cell.value}')


if __name__ == '__main__':
    get_cell_info('spreadsheets/planilhas/livros.xlsx')
