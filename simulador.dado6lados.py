import random

def jogar_dado():
   return random.randint(1,6)

while True:
    input("Pressione o enter para jogar um dado...")
    resultado = jogar_dado()
    print (f"🎲 você tirou: {resultado}\n")
    
    jogar_novamente = input("Quer jogar de novo? (s/n):").lower()
    if jogar_novamente != 's':
        print ("Até a próxima!")
        break
