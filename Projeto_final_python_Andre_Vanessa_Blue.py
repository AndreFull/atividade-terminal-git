from os import system
from tempo import Tempo
from personagem import Personagem


if __name__ == "__main__": 
    tempo = Tempo()
    personagem = Personagem()

    # MENU PRINCIPAL
    while True:
        system('cls')
        print(tempo)
        print('\nBem-vindo a um dia normal de quarentena em 2021!')
        print('\nO que sugere fazermos hoje:')
        print('[ 1 ] Estudar;')
        print('[ 2 ] Limpeza e higiene pessoal;')
        print('[ 3 ] Estimular a produção dos hormônios da felicidade para combatermos a depressão e a ansiedade;')
        print('[ 0 ] Dormir.')

        opcao = int(input('Escolha uma opção: '))
    
        # LAÇO DE REPETIÇÃO 
        while True:
            # [ 1 ] ESTUDAR
            if opcao == 1:
                system('cls')
                print('O que você quer estudar?\n\n[ 1 ] Estudar programação na Blue Edtech\n[ 2 ] Estudar para Concurso Público\n[ 0 ] Menu principal\n')
                escolha = int(input('Escolha uma opção: '))
                
                # [ 1 ] Estudar programação na Blue Edtech
                if escolha == 1:
                    system('cls')
                    if tempo.horas < 21:
                        tempo.avancarTempo(60*3)
                        print(tempo)
                        personagem.estudarBlue()
                    else:
                        print(f'São {tempo.horas}:{tempo.minutos} horas.\n')
                        print('\nAcabou de estudar? Você precisa descansar. Amanhã tem mais!')
                        input('\nPressione ENTER para continuar ...')
                        break
                    input('\nPressione ENTER para continuar ...')

                # [ 2 ] Estudar para concurso público
                elif escolha == 2:
                    system('cls')
                    if tempo.horas < 21:
                        personagem.estudarConcurso()
                        tempo.avancarTempo(60*3)
                        print(tempo)
                    else:
                        print(f'São {tempo.horas}:{tempo.minutos} horas.\n')
                        print('\nEstá cansadx? Vamos dar um tempo, ok?')
                        input('\nPressione ENTER para continuar ...')
                        break
                    input('\nPressione ENTER para continuar ...')
                elif escolha == 0:
                    system('cls')
                    break
                else:
                    print('** Escolha apenas entre as opções disponíveis **')
                    input('\nAperte ENTER para continuar...')
                    

            # [ 2 ] LIMPEZA E HIGIENE PESSOAL
            elif opcao == 2:
                system('cls')
                if tempo.horas < 16:
                    tempo.avancarTempo(60*8)
                    print(tempo)
               
                else:
                    print(f'São {tempo.horas}:{tempo.minutos} horas.\n\nJá chega de limpar! Não exagere, também, né? Você precisa ir dormir.')
                    input('\nPressione ENTER para continuar ...')
                    break
                input('\nPressione ENTER para continuar ... ')
                break
            
            # AUMENTAR SAÚDE
            elif opcao == 3:
                system('cls')
                print('Escolha uma opção:\n')
                print('[ 1 ] Comer alimentos saudáveis;')
                print('[ 2 ] Assistir Netiflix')
                print('[ 3 ] Corrida ao ar livre')
                print('[ 0 ] Menu Principal')

                escolha = int(input('Escolha uma opção acima: '))
                
                # COMIDA SAUDÁVEL
                if escolha == 1:
                    personagem.comidaSaudavel()
                    tempo.avancarTempo(30)
                    print(tempo)
                    print(personagem)
                    input('\nDigite ENTER para continuar...')
                
                # "ASSISTIR NETFLIX"
                elif escolha == 2:
                    personagem.assistir()
                    tempo.avancarTempo(60*2)
                    print(tempo)
                    print(personagem)
                    input('\nDigite ENTER para continuar...')
                
                # CORRIDA AO AR LIVRE
                elif escolha == 3:
                    personagem.corrida()
                    tempo.avancarTempo(60*2)
                    print(tempo)
                    print(personagem)
                    input('\nDigite ENTER para continuar...')
                # MENU PRINCIPAL
                elif escolha == 0:
                    break
                else:
                    system('cls')
                    print('\n** Escolha apenas entre as opções disponíveis! **')
                    input('\nDigite ENTER para continuar...')
            
            # IR DORMIR
            elif opcao == 0:
                tempo.dormir()
                print('')
                print(personagem)
                input('\nPressione ENTER para ACORDAR...')
                break
                
            else:
                system('cls')
                print('Digite apenas números das opções.')
                input('\nDigite ENTER para continuar...')
                break
            


                    







        
    

    


