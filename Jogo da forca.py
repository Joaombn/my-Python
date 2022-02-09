import os

a = 0
b = 0
c = "-"
x = 0
y = 0
z = 0


palavra = input("digite uma palavra ")
Dica1 = input("digite a primeira dica ")
Dica2 = input("digite a segunda dica ")
Dica3 = input("digite a terceira dica ")
controle = []
acertos = []
tents=0
Tentativas=[]

def topo():
 print("\n", c * 30, "\n", "Jogo da forca 1.0".center(30), "\n", c * 30, "\nDica 1 -" + Dica1, "\nDica 2 -" + Dica2,"\nDica 3 -" + Dica3,"\n")

def tentar():
 
 global b
 global tents
 global Tentativas
 
 b = input("\nDigite uma letra: ")
 b = b.upper()
 Tentativas.extend(b)
 tents += 1
 

os.system('clear')

while (x < len(palavra)):
    controle.extend(palavra[x].upper())
    acertos.extend(c)
    x = x + 1

d = len(palavra)
full = 0

while (full != 1):

    topo()
    x = 0
    while (x < len(palavra)):
     print(acertos[x])
     x = x + 1
    print()

    print("Tentativas:",Tentativas,tents,"\n","A!=Ã")
    tentar()
    x = 0

    while (x < len(palavra)):

        if (b == controle[x]):
            acertos[x] = b

        x = x + 1
        os.system('clear')

    if (acertos == controle):
        full = 1
x = 0

topo()
while (x < len(palavra)):
    print(acertos[x])
    x = x + 1

print()
print("Parabéns Você venceu :)")
print("Tentativas:", tents)
print("Tentativas:", Tentativas)
print("Obrigado por jogar :)")





###
