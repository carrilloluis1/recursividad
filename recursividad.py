def calcular_potencia(base: int = 2, exponente: int = 2):
    
    '''Calcula la potencia de un numero'''
    
    if exponente == 0:
    #Caso base cuando sea 0 el exponente el resultado es 1
        return 1
    
    else:
        return base * calcular_potencia(base, exponente - 1)

print (calcular_potencia(2, 4))