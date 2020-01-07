import ficWriter

ctrtab = []
vartab = []
domtab = []
nomscen = "scen01"
with open('../CELAR/'+ nomscen+ '/ctr.txt', "r") as f:
    for line in f.readlines():
        # Traiter la ligne et ainsi de suite ...
        ctrtab.append(line.split())

with open('../CELAR/'+ nomscen +'/var.txt', "r") as f:
    for line in f.readlines():
        # Traiter la ligne et ainsi de suite ...
        vartab.append(line.split())

with open('../CELAR/'+ nomscen +'/dom.txt', "r") as f:
    for line in f.readlines():
        # Traiter la ligne et ainsi de suite ...
        domtab.append(line.split())

ficWriter.createFile(nomscen, vartab, ctrtab, domtab)