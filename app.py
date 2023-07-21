import random

def jogar():
    
    abertura_mensagem()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = substitui_por_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

      chute = pede_chute()

      if(chute in palavra_secreta):
        
        marca_chute_correto(chute, letras_acertadas, palavra_secreta)

      else:
          print("Nenhuma letra encontrada")
          desenha_forca(erros)
          erros += 1

      print(letras_acertadas)
      
      enforcou = erros == 8
      acertou = "_" not in letras_acertadas

    if(enforcou):
        imprime_perdedor(palavra_secreta)
        continuar()
    if(acertou):
        imprime_vencedor()
        continuar()
    
def abertura_mensagem():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    
    arquivo = open("palavra.txt", "r")
    palavra = []

    for linha in arquivo:
       linha = linha.strip()
       palavra.append(linha)    

    arquivo.close()
    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].lower()

    return palavra_secreta

def substitui_por_letras_acertadas(palavra_secreta):
   letras_acertadas = ["_" for letra in palavra_secreta]
   return letras_acertadas
   
def pede_chute():
    chute =  input("Digite uma letra: ").strip().lower()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Fim de jogo")

def imprime_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("Fim de jogo")

def continuar():
    print("\n1- Nova rodada")
    print("2- Sair")
    resp = int(input())

    if resp == 1:
        jogar()
    else:
        print("Até a próxima")

if(__name__ == "__main__"):
    jogar()
