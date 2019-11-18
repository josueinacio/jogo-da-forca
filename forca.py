palavra_secreta = ["s","u","b","l","i","m","e"]
letras_descobertas = []


print('***Bem vindo ao jogo da forca!***')
print('*********************************')

for i in range(0, len(palavra_secreta)) :
    letras_descobertas.append("-") 
    acertou = False 

while acertou == False :
  letra =str(input("digite a letra: "))
for i in range(0, len (palavra_secreta)) :

    if letra == palavra_secreta[1] :
       letras_descobertas[i] = letra
    print(letras_descobertas[i])
acertou = True 

for x in range(0, len (letras_descobertas)) :
   if  letras_descobertas[x] == "-" :
       acertou = False
for x in range(0, len (letras_descobertas)) :
   if  letras_descobertas[x] == "-" :
       acertou = False
