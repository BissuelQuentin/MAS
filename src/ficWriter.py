
def createFile(nbAgent, vartab, ctrtab, domtab):
    file = open("scen01.xml", "w")


    file.write('<instance>\n')
    file.write('    <presentation name="sampleProblem" maxConstraintArity="2"\n')
    file.write('                   maximize="false" format="XCSP 2.1_FRODO" />\n\n')

    file.write('    <agents nbAgents="'+ str(nbAgent) + '">\n')
    for i in range(nbAgent) :
        file.write('        <agent name="agent' + str(i+1) + '" />\n')
    file.write('    </agents>\n\n')


    file.write('    <domains nbDomains="'+ str(domtab.length()) +'">\n')
    file.write('        <agent name="agentX" />\n')
    file.write('        <agent name="agentY" />\n')
    file.write('        <agent name="agentZ" />\n')
    file.write('    </agents>\n\n')

    file.close()


createFile(1, )