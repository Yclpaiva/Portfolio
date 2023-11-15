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