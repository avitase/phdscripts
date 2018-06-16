import config as configFile

import os

if os.path.isfile('options.py'):
    os.remove('options.py')

infile = file('options.py.template', 'r')
outfile = file('options.py', 'w')

print 'replacing \'configFile.line\'   -> \'%s\'' %configFile.line
print 'replacing \'configFile.stream\' -> \'%s\'' %configFile.stream
print 'replacing \'configFile.name\'   -> \'%s\'' %configFile.name
print 'replacing \'configFile.year\'   -> \'%s\'' %configFile.year
print 'replacing \'configFile.evtMax\' -> \'%s\'' %configFile.evtMax
print 'replacing \'configFile.debug\'  -> \'%s\'' %configFile.debug

import time
currentTime = time.strftime('%c')
outfile.write('# --- ATTENTION ---\n')
outfile.write('# This file is auto-generated.\n')
outfile.write('# Date: %s\n\n' %currentTime)

for line in infile:
    newLine = line
    newLine = newLine.replace('configFile.line', '\'' + configFile.line + '\'')
    newLine = newLine.replace('configFile.stream', '\'' + configFile.stream + '\'')
    newLine = newLine.replace('configFile.name', '\'' + configFile.name + '\'')
    newLine = newLine.replace('configFile.year', '\'' + configFile.year + '\'')
    newLine = newLine.replace('configFile.evtMax', str(configFile.evtMax))
    newLine = newLine.replace('configFile.debug', 'True' if configFile.debug else 'False')

    outfile.write(newLine)

infile.close()
outfile.close()

os.chmod('options.py', 0444)
