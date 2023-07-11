def comeco():
    notas = pega_nota()
    print("Sua média é:", notas)

def pega_nota():
    nota1 = int(input("Digite a 1 nota: "))
    nota2 = int(input("Digite a 2 nota: "))
    nota3 = int(input("Digite a 3 nota: "))
    nota4 = int(input("Digite a 4 nota: "))

    media = (nota1 + nota2 + nota3 + nota4)/4

    return media


if(__name__ == "__main__"):
    comeco()
