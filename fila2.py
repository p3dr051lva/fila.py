comum = []
idosos = []
prog = []
aux = 2
while aux > 0:
    c = str(input("digite uma senha para entrar na fila idosos, se quiser: "))
    i = str(input("digite uma senha para entrar na fila dos gestantes, se quiser: "))
    p = str(input("digite uma senha para entrar na fila dos comuns, se quiser: "))

    if c != '' and i != '' and p == '':
        comum.append(c)
        idosos.append(i)
    elif c != '' and i == '' and p != '':
        comum.append(c)
        prog.append(p)
    elif c == '' and i != '' and p != '':
        idosos.append(i)
        prog.append(p)
    elif c != '' and i != '' and p != '':
        comum.append(c)
        idosos.append(i)
        prog.append(p)
    elif c == '' and i == '' and p == '':
        comum = comum
        idosos = idosos
        prog = prog
    elif c == '' and i == '' and p != '':
        prog.append(p)
    elif c == '' and i != '' and p == '':
        idosos.append(i)
    elif c != '' and i == '' and p == '':
        comum.append(c)
        
    print (comum,"idosos")
    print (idosos,"gestantes")
    print (prog,"comuns")

    sc = str(input("quer que a fila dos idosos ande? responda com sim ou nao:"))
    si = str(input("quer que a fila dos gestantes ande? responda com sim ou nao:"))
    sp = str(input("quer que a fila das comuns ande ande? responda com sim ou nao:"))

    if sc == 'sim' and si == 'nao' and sp == 'nao':
        del comum[0]
    elif sc == 'nao' and si == 'sim' and sp == 'nao':
        del idosos[0]
    elif sc == 'nao' and si == 'nao' and sp == 'sim':
        del prog[0]
    elif sc == 'sim' and si == 'sim' and sp == 'sim':
        del comum[0]
        del idosos[0]
        del prog[0]
    elif sc == 'sim' and si == 'sim' and sp == 'nao':
        del comum[0]
        del idosos[0]
    elif sc == 'sim' and si == 'nao' and sp == 'sim':
        del comum[0]
        del prog[0]
    elif sc == 'nao' and si == 'sim' and sp == 'sim':
        del idosos[0]
        del prog[0]

    print (comum,"idosos")
    print (idosos,"gestantes")
    print (prog,"comuns")

    
    
    
