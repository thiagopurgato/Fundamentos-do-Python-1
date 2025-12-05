ano = int(input("digite um ano: "))

if ano < 1582:
 print("Fora do periodo do calendario")
 
else:
    if ano % 4 != 0:
     print("ano comum")
    elif ano % 100 != 0:
     print("Ano bissexto")
    elif ano % 400 != 0:
     print("é ano comum")
    else:
     print("não é bissexto") 