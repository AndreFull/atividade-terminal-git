from os import system
from time import sleep


class Personagem:
    def __init__(self):
        self.dinheiro = 1100 # R$ 1.100,00 é valor do salário mínimo atual. 
        
        self.blue = 0
        self.expConc = 0
        self.nivel = "Sem experiência"
        self.trabalho = False
        
    def __str__(self):
        return f'Status do personagem:\n=-=-=-=-=-=-=\nExperiência em programação: {self.blue}\nExperiência em Concursos: {self.expConc}\nNível: {self.nivel}'

    # LIMPAR E SE LIMPAR
    def limpar(self):
        print(f'Você limpou bem as coisas e fez sua higiene pessoal adequada.')
        print('Parabéns! Isso só ajuda a aumentar a sua saúde.')
        
    
    # ESTUDAR NA BLUE EDTECH
    def estudarBlue(self):
        self.blue += 1.0
        
        if self.expConc >= 10 and self.blue >= 10:
            self.nivel = "Futuro Programador Senior FullStack!"
            self.salario = 1000

        elif self.blue >= 10:
            self.nivel = "Futuro Programador Senior!"
            self.salario = 700

        elif self.blue >= 5:
            self.nivel = "Futuro Programador Pleno!"
            self.salario = 400

        elif self.blue >= 2:
            self.nivel = "Futuro Programador Junior!"
            self.salario = 250

        print(f'Você estudou programação e sua experiência atual é estimada em {self.blue}.\n')
        

    # ESTUDAR PARA CONCURSO (sabe-se lá quando vamos ter mais...)
    def estudarConcurso(self):
        self.expConc += 0.5
       
        if self.expConc >= 10 and self.blue >= 10:
            self.nivel = "Concurseiro inciante..."
            self.salario = 1000

        elif self.expConc >= 10:
            self.nivel = "Concurseiro 'nutella'..."
            self.salario = 650

        elif self.expConc >= 5:
            self.nivel = "Concurseiro experiente..."
            self.salario = 250

        elif self.expConc >= 2:
            self.nivel = "Concurseiro raiz... Boto fé!"
            self.salario = 130
        print(f'Você estudou bem para o concurso público.\nSua experiência atual é estimada em {self.expConc}')
        print('\n. Parabéns! Continue assim que logo conseguirá!')
        

    # AUMENTAR A PRODUÇÃO DE HORMÔNIOS DA FELICIDADE
    def comidaSaudavel(self):
        system('cls')
       
        self.dinheiro -= 50
        print('Hum... que delícia! Vamos pedir mais um desses?\n')
        sleep(5)
        print(f'Comida saudável também pode ser a nossa caseira, feita com muito amor!\n')
    
    def assistir(self):
        system('cls')
        
        self.dinheiro -= 35
        print('Que gostoso assistir Netiflix na sua companhia... ;)\n')
        sleep(5)
        print(f'Você não acha que está bom de você levantar um pouco? \nJá assitiu muita coisa hoje.')
        print('Sei que estamos felizes, mas a mente também cansa, sabia?\n')
    
    def corrida(self):
        system('cls')
        
        print('Que bom podermos correr um pouco ao ar livre e nessa praça linda! \n')
        sleep(5)
        print(f'Fiquei tão feliz com a sua companhia! A corrida foi muito boa! Obrigada\n')

