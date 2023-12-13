class DataManagement:
    def __init__(self,add_database):
        self.add_database = add_database
        
    def add_database(entry):
        file = open('data.csv', 'a')
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
            with open('data.csv', 'r') as file:
                lines = file.readlines()
            if line_number >= len(lines):
                with open('data.csv', 'r') as file:
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
        
        
    def subdata():
        numero_linha = int(input('Qual a linha que você deseja alterar? '))
        with open('data.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
        if 1 <= numero_linha <= len(linhas):
            print(linhas[numero_linha-1])
            novo_texto = str(input('Qual o valor a ser adicionado? '))
            linhas[numero_linha - 1] = novo_texto + '\n'
            with open('data.csv', 'w') as arquivo:
                arquivo.writelines(linhas)
            print(f'Linha {numero_linha} alterada com sucesso.')
        else:
            print(f'Linha {numero_linha} não encontrada.')

    def addgrade():
        while True:
            line_number = int(input('Read which line? '))  # Get the line number from the user
            with open('data.csv', 'r') as file:
                lines = file.readlines()
                print(len(lines))
            if line_number <= len(lines):
                with open('data.csv', 'r') as file:
                    current_line = 0
                    for line in file:
                        current_line += 1
                        if current_line == line_number:
                            values = line.strip().split(',')
                            if len(values) == 5:
                                name, birthday, contact , parents, grades = values
                                grade1 = 0
                                grade2 = 0
                                grade3 = 0 
                                grade4 = 0
                                grade1 = input('Input grade 1: ')
                                yesorno = str(input('Tem mais notas para adicionar? ')).lower().strip()
                                if yesorno == 'sim':
                                    grade2 = input('Input grade 2: ')
                                    yesorno = str(input('Tem mais notas para adicionar? ')).lower().strip()
                                    if yesorno == 'sim':
                                        grade3 = input('Input grade 3: ')
                                        yesorno = str(input('Tem mais notas para adicionar? ')).lower().strip()
                                        if yesorno == 'sim':
                                            grade4 = input('Input grade 4: ')
                                        else:pass
                                    else:pass
                                else:pass
                                grades = f'grades:{grade1}/{grade2}/{grade3}/{grade4}'                      
                                print(name, birthday, contact, parents, grades)
                                novo_texto = str(f'{name},{birthday},{contact},{parents},{grades}') # Returning the values from the specific line
                                lines[line_number - 1] = novo_texto + '\n'
                                with open('data.csv', 'w') as arquivo:
                                    arquivo.writelines(lines)
                                print(f'Linha {line_number} alterada com sucesso.')
                            if len(values) == 3:
                                print("Invalid format in the selected line.")
                                return None
            else:
                print('Número informado inválido!')
                print("Line not found.")
                return None