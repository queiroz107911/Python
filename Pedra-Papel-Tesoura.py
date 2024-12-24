contador_jogador1 = 0
contador_jogador2 = 0

while True:
    print('Pedra/Papel/Tesoura')
    print('''\n escolha sua opção:
    [1]Preda
    [2]Papel
    [3]Tesora''')
    print('\n')
    jogador1= int(input("escolha uma opção"))
    jogador2= int(input('escolha uma opção'))

    if jogador1== 1:
        if jogador2== 1: 
            print('Empate')
        elif jogador2== 2:
            print('jogador2 VENCEU')
            contador_jogador2 +=1
        elif jogador2== 3:
            print('jogador1 VENCEU')  
            contador_jogador1 +=1

    if jogador1== 2:
        if jogador2== 1:
            print('jogador1 VENCEU')
            contador_jogador1 +=1
        elif jogador2== 2:
            print('Empate')
        elif jogador2== 3:
            print('jogador2 VNCEU')  
            contador_jogador2 +=1

    if jogador1== 3:
        if jogador2== 1:
            print('jogador1 VENCEU')
            contador_jogador1 +=1
        elif jogador2== 2:
            print('jogador1 VENCEU')
            contador_jogador1 +=1
        elif jogador2== 3:
            print('Empate')

    print(f'Pontuação do jogador1: {contador_jogador1}')
    print(f'Pontuação do jogador2: {contador_jogador2}')

    if contador_jogador1== 2:
        print('jogador1 VENCEU')
        break
    elif contador_jogador2== 2:
        print('jogador2 VENCEU')
        break


    













