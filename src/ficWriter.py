
def createFile(nomscen, vartab, ctrtab, domtab):
    file = open(nomscen + ".xml", "w")


    file.write('<instance>\n')
    file.write('    <presentation name="sampleProblem" maxConstraintArity="2"\n')
    file.write('                   maximize="false" format="XCSP 2.1_FRODO" />\n\n')

    file.write('    <agents nbAgents="'+ str(len(vartab)) + '">\n')
    for i in range(len(vartab)) :
        file.write('        <agent name="agent' + str(i+1) + '" />\n')
    file.write('    </agents>\n\n')


    file.write('    <domains nbDomains="'+ str(len(domtab)) +'">\n')
    for i in range(len(domtab)):
        file.write('        <domain name="' + str(i + 1) + '" nbValues="' + str(domtab[i][1]) + '">')
        for j in range(int(domtab[i][1])-1):
            file.write(str(domtab[i][j+2]) + " ")
        file.write(str(domtab[i][int(domtab[i][1])+1]))
        file.write('</domain>\n')
    file.write('    </domains>\n\n')

    file.write('    <variables nbVariables="'+ str(len(vartab)) +'">\n')
    for i in range(len(vartab)) :
        file.write('        <variable name="'+ str(i+1) + '" domain="'+ str(vartab[i][1]) + '" agent="agent'+ str(i+1) +'" />\n')
    file.write('    </variables>\n\n')

    file.write('    <predicates nbPredicates="2">\n')
    file.write('        <predicate name="NEQ">\n')
    file.write('            <parameters> int X1 int X2 int K2 </parameters>\n')
    file.write('            <expression>\n')
    file.write('                <functional> gt(abs(sub(X1,X2)),K2) </functional>\n')
    file.write('            </expression>\n')
    file.write('        </predicate>\n')
    file.write('        <predicate name="EQ">\n')
    file.write('            <parameters> int X1 int X2 int K2</parameters>\n')
    file.write('            <expression>\n')
    file.write('                <functional> eq(abs(sub(X1,X2)),K2) </functional>\n')
    file.write('            </expression>\n')
    file.write('        </predicate>\n')
    file.write('    </predicates>\n\n')

    file.write('    <constraints nbConstraints="'+ str(len(ctrtab)) +'">\n')
    for i in range(len(ctrtab)):
        if (ctrtab[i][3] == '>'):
            file.write('        <constraint name="'+ str(ctrtab[i][0]) +'_and_'+ str(ctrtab[i][1]) +'_have_different_value" arity="2" scope="'+ str(ctrtab[i][0]) + ' '+ str(ctrtab[i][1])+ '" reference="NEQ">\n')
        else:
            file.write('       <constraint name="' + str(ctrtab[i][0]) + '_and_' + str(ctrtab[i][1]) + '_have_same_value" arity="2" scope="' + str(ctrtab[i][0]) + ' ' + str(ctrtab[i][1]) + '" reference="EQ">\n')
        file.write('            <parameters>' + str(ctrtab[i][0]) + ' ' + str(ctrtab[i][1]) + ' ' + str(ctrtab[i][4]) + '</parameters>\n')
        file.write('        </constraint>\n')
    file.write('    </constraints>\n\n')
    file.write('</instance>\n')


    file.close()
