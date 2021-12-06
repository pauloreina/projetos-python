import os


def cls():
    os.system('cls')
    return


def palavra():
    global secreto, digitadas, tentativa
    tentativa = ''
    for le in secreto:
        if le in digitadas:
            print(le, end='')
            tentativa += le
        else:
            print('*', end='')


def forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


digitadas = list()
tentativa = ''
erro = 0

while True:
    print('*' * 30)
    print(f'{"Jogo da Forca":^30}')
    print('*' * 30)
    while True:
        secreto = input('Digite uma palavra: ').strip().lower()
        if secreto == '':
            print('Digite alguma palavra!')
        else:
            break
    cls()
    while True:
        letra = input('Digite uma letra: ').strip().lower()
        if len(letra) > 1:
            print('Isso não vale! Digite apenas uma letra.')
        elif letra in digitadas:
            print('Essa letra já foi digitada anteriormente!')
        else:
            digitadas.append(letra)
            if letra in secreto:
                print(f'\033[0;32mA letra "{letra}" existe na palavra secreta.\033[m')
            else:
                print(f'\033[0;31mA letra "{letra}" não existe na palavra secreta.\033[m')
                erro += 1
            digitadas.sort()
            print('='*20)
            forca(erro)
            palavra()
            print(f'\nLetras Digitadas: ', end='')
            for i in digitadas:
                print(i, end=' ')
            print(f'\nErros: {erro}')
            if erro == 7:
                print(f'Você perdeu! A palavra era "{secreto}"')
                break
            if tentativa == secreto:
                print('Parabéns, você acertou a palavra!')
                print('=' * 20)
                break
            print('=' * 20)
    continuar = input('Deseja continuar? [S/N]')
    while continuar not in 'sSnN':
        continuar = input('Opção inválida: ')
    if continuar in 'Nn':
        break
    digitadas.clear()
    erro = 0
