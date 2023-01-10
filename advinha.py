from random import randint

def advinha ():
    num = randint (1 ,10)
  
  
    while True:
      numero = int(input("digite um numero de 1 a 10: "))
      if numero < 1 or numero > 10 :
        print("opção invalida numero tem que ser maior que 1 e menor que 10 ")
        break

      if numero == num :
        print("PARABÊNS ! você acertou o numero sorteado ")
        break

      elif numero < num :
        print("voce errou o numero era maior ")
      
      elif numero > num :
        print("você errou o numero era menor ")

      #if tentativas == 0 :
       # print("você atingiu o numero maximo /nde tentativas o numero seria " , num )
      
      pergunta = input("deseja jogar novamente s /n: ")
        
      if pergunta == "n" :
        break
      elif pergunta == "s":
        return advinha()      
       
advinha()