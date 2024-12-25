# Escrever em uma planilha
# Adicionar dados
from openpyxl import Workbook


def create_workbook(path):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "13ª geração Intel® Core™ i7-13650HX"
    sheet["A2"] = "Windows 11 Home Single Language"
    sheet["A3"] = "NVIDIA® GeForce® RTX™ 4050, 6GB GDDR6"
    sheet["A4"] = "16GB DDR5 (2x8GB) 4800MT/s"
    sheet["A5"] = "SSD de 512GB PCIe NVMe M.2"
    sheet["A6"] = "Full HD de 15.6 (1920 x 1080), 120Hz, 250 nits"
    sheet["A7"] = "Dark Shadow Gray - Grafite"
    sheet["A8"] = "Teclado retroiluminado na cor laranja, numérico e em português"
    workbook.save(path)
    print("\nDados inseridos com sucesso!")


if __name__ == "__main__":
    create_workbook("spreadsheets/planilhas/notebooks.xlsx")
