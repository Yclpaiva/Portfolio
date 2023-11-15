import csv
from alumni import Alumni
from datamanagment import DataManagement
from pessoa import Pessoa

    

class Professor:
    def __init__(self):
        pass

def getGradesInput():
    for i in range(4):
        notas = int(input('Type the Alumni grades: '))


# Exemplo de uso
numero_linha = 3
novo_texto = 'Nova linha alterada'



            

def main():
    while True:
        print('\n\nBem-Vindo ao sistema de consulta academica!')
        opcao = int(input('Escolha uma das opções:\n\n1-Consulta Banco de dados  |  2-Cadastro Banco de dados\n\n3- Substituir dados  |  4- Add grade\n\n    :'))
        if opcao == 1:
            accessdata = DataManagement.read_database()
            #return Alumni(accessdata[0],accessdata[1],accessdata[2],accessdata[3],accessdata[4])
        elif opcao == 2:
            DataManagement.inputdatapessoa()
        elif opcao == 3:
            DataManagement.subdata()
        elif opcao == 4:
            DataManagement.addgrade()
        else:
            pass
main()