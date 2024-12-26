# Adicionar linhas de dados
from openpyxl import Workbook


def create_workbook(path):
    workbook = Workbook()
    sheet = workbook.active
    data = [["Nome", "Idade", "Email"],
            ["Bill Gates", 55, "billgates@gmail.com"],
            ["Sam Altman", 45, "samaltman@gmail.com"],
            ["Jeff Bezos", 55, "jeffbezos@gmail.com"]]
    for row in data:
        sheet.append(row)
        workbook.save(path)


if __name__ == "__main__":
    create_workbook("dados.xlsx")
