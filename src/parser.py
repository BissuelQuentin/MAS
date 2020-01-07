
ctrtab = []
vartab = []
domtab = []

with open("../CELAR/scen01/ctr.txt", "r") as f:
    for line in f.readlines():
        # Traiter la ligne et ainsi de suite ...
        ctrtab.append(line.split())

print(ctrtab)

with open("../CELAR/scen01/var.txt", "r") as f:
    for line in f.readlines():
        # Traiter la ligne et ainsi de suite ...
        vartab.append(line.split())

print(vartab)

with open("../CELAR/scen01/dom.txt", "r") as f:
    for line in f.readlines():
        # Traiter la ligne et ainsi de suite ...
        domtab.append(line.split())

print(domtab)

ficWriter.createFile(1, vartab, ctrtab, domtab)