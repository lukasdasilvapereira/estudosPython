def retornarMedia(numero):
    if len(numero) == 0:
        return 0
    else:
        return sum(numero) / len(numero)
    
print(retornarMedia([10, 20 , 30]))
    

