#1.	Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
# (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
#{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  

c = list()
n = list()
i = 0
dados = dict()
for c in (1,4,5,6,7,9):
    c = int(c**2)
    n.append(c)

if dados.get(1) == None:
   dados.setdefault(1, 1)
   dados.setdefault(2,4)
   dados.setdefault(4,16)
   dados.setdefault(5,25)
   dados.setdefault(6,36)
   dados.setdefault(7,49)
   dados.setdefault(9,81)
   
    
print(dados)


             
   
        

    