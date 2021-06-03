#2.	Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e 
# cada valor associado é o número ao quadrado.
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} 

c = []
i = []
for c in range(1,10+1):
    print(c)

for i in range(1,10+1):
    i = i**2
    print(i)

key_list = c
value_list = i

dados = dict()
dados = (c : i)


print(dados)


        





