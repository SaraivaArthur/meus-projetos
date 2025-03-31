player = {"Nome": "Python", "x": 0, "y":0 }

def andar(direcao):
    if direcao =="d":
        player ['x'] += 1
    elif direcao == 'a':
        player ['x'] -= 1
    elif direcao == 'W':
        player ['y'] -= 1
    elif direcao == 's':
        player ['y'] += 1
        
while True:
  print("\n" * 100)
    
print("---------------------------")
for y in range(5):
    print ("\n")
    for x in range(10):
        if player ['x'] == x and player ['y'] == y:
            print ('😎', end="")
        else:
            print ("🟩", end="")
print("---------------------------")

direcao = input("Proxima direcao (w,s,d,a):")
andar(direcao)
direcao = input("Proxima direcao (w,s,d,a):")
andar(direcao)
            
            
    
