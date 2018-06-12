size_small = (2.8, 2.1)
size_medium = (4.0, 3.0)

preamble = [
    r'''\newcommand{\mevcc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c^2}}''',
    r'''\newcommand{\mevc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c}}''',
    r'''\newcommand{\gevcc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c^2}}''',
    r'''\newcommand{\gevc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c}}''',
    r'''\newcommand{\MagUp}{\ensuremath{\mathrm{\textit{Mag\kern -0.05em Up}}}}''',
    r'''\newcommand{\MagDown}{\ensuremath{\mathrm{\textit{MagDown}}}}''',
]

def prepend_preamble(cmd):
    return [cmd, ] + preamble

def append_preamble(cmd):
    return preamble + [cmd, ]

def create(filename, code, size = size_small, preamble=preamble):
    basename = filename.split('.')[0]
    gpfilename = '{}.{}'.format(basename, 'gp')
    texfilename = '{}.{}'.format(basename, 'tex')

    with open(gpfilename, 'w') as f:
        f.write('set terminal epslatex size {}, {} color standalone "" 9 header \'{}\'\n'
                .format(*size, ' '.join(preamble)))

        f.write('set output \'{}\'\n'.format(texfilename))
        f.write('load \'parula.pal\'\n')
        f.write('set datafile separator \',\'\n\n')
        f.write(code.strip())

    return './gp2png.sh {} {}'.format(gpfilename, texfilename)
