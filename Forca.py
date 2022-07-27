import random
import time
from unicodedata import normalize

def palavraAleatoria():
    palavras = []
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = random.choice(palavras)
    palavra_secreta = normalize('NFKD', palavra_secreta).encode('ASCII','ignore').decode('ASCII')
    return palavra_secreta.replace('"', "")

game = ""
stop = False
acertou = False
palavrasDigitadas = []
palavraOriginal = palavraAleatoria()
palavraEscolhida = palavraOriginal.upper()
letrasDaPalavra = []
erros = i = j = 0
newErros = 0
boneco = [" ", "O", "|", "/", "\\", "|", "/", "\\"]
forca = [
    ["_", "_", "_", "_", "_", "_", "_", "_", " "],
    ["|", " ", "/", " ", " ", " ", " ", "|", " "],
    ["|", "/", " ", " ", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " ", " ", " ", " "],
    ["|", " "]
    ]

for i in range(len(palavraEscolhida)):
    letrasDaPalavra.append("-")
    forca[7].append("- ")

def MostrarForca():
    for l in range(0, 8):
        if(len(forca[7]) > len(forca[l])):
            for i in range(len(forca[7]) - len(forca[l])):
                forca[l].append(" ")

        if(len(forca[7]) < len(forca[0])):
            for i in range(len(forca[0]) - len(forca[7])):
                forca[7].append(" ")

        for c in range(0, len(forca[0])):
            print(f"{forca[l][c]}", end='')
        print()

def ComeçarJogo():
    print("=" * 60)
    print("*" * 15, "Bem vindo ao jogo da Forca!", "*" * 15)
    print("=" * 60)

    time.sleep(2)

def GanhouJogo():
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
    time.sleep(2)

def PerdeuJogo(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era:", palavra)
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
    time.sleep(2)

def PartesBoneco():
    if(erros == 1):
        i = 2
        j = 7

    if(erros == 2):
        i = 3
        j = 7

    if(erros == 3):
        i = 3
        j = 6

    if(erros == 4):
        i = 3
        j = 8

    if(erros == 5):
        i = 4
        j = 7

    if(erros == 6):
        i = 5
        j = 6

    if(erros == 7):
        i = 5
        j = 8

    forca[i][j] = boneco[erros]

ComeçarJogo()
MostrarForca()

while(stop == False):
    time.sleep(1)

    letraEscolhida = input("Tente uma letra: ").upper()
    palavrasDigitadas.append(letraEscolhida)

    if(letraEscolhida not in palavraEscolhida):
            erros += 1
            acertou = False
    else:
        for letra in palavraEscolhida:
            posicaoLetraPalavra = 0

            if(letraEscolhida == letra):
                acertou = True
                posicaoLetraPalavra = palavraEscolhida.find(letraEscolhida)

                letrasDaPalavra[posicaoLetraPalavra] = letraEscolhida
                forca[7][posicaoLetraPalavra+2] = letraEscolhida + " "
                palavraEscolhida = palavraEscolhida.replace(palavraEscolhida[posicaoLetraPalavra], " ", 1)

    print("=" * 60)

    if(erros != newErros):
        PartesBoneco()
        newErros += 1
    if(acertou):
        print("Você digitou uma letra que pertence a palavra!!")
        MostrarForca()
        print(f"Palavras digitadas:", ", ".join(palavrasDigitadas))
    else:
        print("Você digitou uma letra que não pertence a palavra!!")
        MostrarForca()
        print(f"Palavras digitadas:", ", ".join(palavrasDigitadas))

    if(newErros == 7):
        game = "lose"
        stop = True

    if("".join(letrasDaPalavra) == palavraOriginal.upper()):
        game = "win"
        stop = True

if(game == "win"):
    time.sleep(1)
    GanhouJogo()

if(game == "lose"):
    time.sleep(1)
    PerdeuJogo(palavraOriginal)

