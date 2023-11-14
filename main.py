import csv

class Pessoa:
    def __init__(self,name,birthday,contact):
        self.name = name
        self.birthday = birthday
        self.contact = contact
    
    def get_name(self):
        return self.name
    def get_birthday(self):
        return self.birthday
    def get_contact(self):
        return self.contact
class Alumni:
    def __init__(self,pessoa,birthday,contact,parents,grades):
        
        self.dadospessoa = pessoa
        self.dadosbirthday = birthday
        self.dadoscontact = contact
        self.dadosparentes = parents
        self.dadosgrades = grades
        
    def get_pessoa(self):
        return self.dadospessoa.get_name()
    def get_birthday(self):
        return self.dadosbirthday.get_birthday()
    def get_contact(self):
        return self.dadoscontact.get_contact()
    def get_parents(self):
        return self.dadosparentes
    def get_grades(self):
        return self.dadosgrades
    def grades_alumni(self):
        grade = sum(self.dadosgrades)/4
        return grade        
class Professor:
    def __init__(self):
        pass

def opendatabase():
    pessoa = []
    with open('pessoa.csv') as file:
        for line in file:
            name,birthday,contact = line.rstrip().split(',')
            pessoalista = {'name':name,'birthday':birthday,'contact':contact }
            pessoa.append(pessoalista)

def getGradesInput():
    for i in range(4):
        notas = int(input('Type the Alumni grades: '))

class DataManagement:
    def __init__(self,add_database):
        self.add_database = add_database
        
    def add_database(entry):
        file = open('pessoa.csv', 'a')
        file.write(entry + '\n')
        
    def inputdatapessoa():
        inputnamepessoa = str(input('digite o nome da pessoa: '))
        inputbirthday = str(input('digite a data de nascimento: '))
        inputcontact = str(input('digite o número de contato: '))
        
        itsalumni = (input('é aluno? (Sim ou não)  ')).lower().strip()
        if itsalumni == 'sim':
            inputparents = str(input('digite o nome da mãe: '))
            inputparents2 = str(input('digite o nome do pai: '))
            resultado = (f'{inputnamepessoa},{inputbirthday}, {inputcontact},{inputparents} & {inputparents2},grades:{0}/{0}/{0}/{0}')
        else:
            resultado = (f'{inputnamepessoa},{inputbirthday},{inputcontact}')
        print('pessoa adicionada:', resultado)
        DataManagement.add_database(resultado)
        
        return resultado
    def read_database():
        while True:
            line_number = int(input('Read which line? '))  # Get the line number from the user
            with open('pessoa.csv', 'r') as file:
                lines = file.readlines()
            if line_number >= len(lines):
                with open('pessoa.csv', 'r') as file:
                    current_line = 0
                    for line in file:
                        current_line += 1
                        if current_line == line_number:
                            values = line.strip().split(',')
                            if len(values) == 5:
                                name, birthday, contact , parents, grades = values
                                print(name, birthday, contact, parents, grades)
                                return name, birthday, contact, parents, grades # Returning the values from the specific line
                            if len(values) == 3:
                                name, birthday, contact = values
                                print(name, birthday, contact)
                                return name, birthday, contact, None, None
                            else:
                                print("Invalid format in the selected line.")
                                return None
                print("Line not found.")
                return None
            else:
                print('Número informado inválido!')
        
        
    def pessoatoalumni():
        numero_linha = int(input('Qual a linha que você deseja alterar? '))
        with open('pessoa.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
        if 1 <= numero_linha <= len(linhas):
            print(linhas[numero_linha-1])
            novo_texto = str(input('Qual o valor a ser adicionado? '))
            linhas[numero_linha - 1] = novo_texto + '\n'
            with open('pessoa.csv', 'w') as arquivo:
                arquivo.writelines(linhas)
            print(f'Linha {numero_linha} alterada com sucesso.')
        else:
            print(f'Linha {numero_linha} não encontrada.')

# Exemplo de uso
numero_linha = 3
novo_texto = 'Nova linha alterada'



            

def main():
    while True:
        print('\n\nBem-Vindo ao sistema de consulta academica!')
        opcao = int(input('Escolha uma das opções:\n\n1-Consulta Banco de dados  |  2-Cadastro Banco de dados\n\n3- Pessoa to alumni    :'))
        if opcao == 1:
            accessdata = DataManagement.read_database()
            #return Alumni(accessdata[0],accessdata[1],accessdata[2],accessdata[3],accessdata[4])
        elif opcao == 2:
            DataManagement.inputdatapessoa()
        elif opcao == 3:
            DataManagement.pessoatoalumni()
        else:
            pass
main()