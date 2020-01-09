import ficWriter

def ficParsing(nomscen, nbvar):
    ctrtab = []
    vartab = []
    domtab = []
    i = 0

    with open('../CELAR/'+ nomscen+ '/ctr.txt', "r") as f:
        line = f.read().splitlines()
        while i < nbvar:
            if(i<len(line)):
                # Traiter la ligne et ainsi de suite ...
                ctrtab.append(line[i].split())
            i = i+1

    i = 0

    with open('../CELAR/'+ nomscen +'/var.txt', "r") as f:
        line = f.read().splitlines()
        while i < len(line):
            if (i < len(line)):
                # Traiter la ligne et ainsi de suite ...
                vartab.append(line[i].split())
            i = i+1
    i = 0

    with open('../CELAR/'+ nomscen +'/dom.txt', "r") as f:
        line = f.readlines()
        while i < len(line):
            if (i < len(line)):
                # Traiter la ligne et ainsi de suite ...
                domtab.append(line[i].split())
            i = i+1

    ficWriter.createFile(nomscen, vartab, ctrtab, domtab)