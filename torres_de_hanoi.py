def torres_de_hanoi(discos, primera_torre, segunda_torre, torre_extra):
    '''Resuelve el problema de las torres de hanoi'''
    
    if discos == 1:
        # Caso base hay un solo disco en la primera torre, se mueve directamente
        print(f"Mover disco 1 desde {primera_torre} hasta {segunda_torre}")
    else:
        
        # Mover n-1 discos desde primera_torre a torre_extra
        torres_de_hanoi(discos-1, primera_torre, torre_extra, segunda_torre)
        
        # Mover el disco n desde primera_torre a segunda_torre
        print(f"Mover disco {discos} desde {primera_torre} hasta {segunda_torre}")
        
        # 3. Mover n-1 discos desde torre_extra a segunda_torre
        torres_de_hanoi(discos-1, torre_extra, segunda_torre, primera_torre)


torres_de_hanoi(3, 'A', 'C', 'B')
