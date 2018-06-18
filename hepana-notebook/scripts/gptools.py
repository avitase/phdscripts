import os

size_small = (2.8, 2.1)
size_medium = (4.0, 3.0)

preamble = [
    r'''\newcommand{\mevcc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c^2}}''',
    r'''\newcommand{\mevc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c}}''',
    r'''\newcommand{\gevcc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c^2}}''',
    r'''\newcommand{\gevc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c}}''',
    r'''\newcommand{\MagUp}{\ensuremath{\mathrm{\textit{Mag\kern -0.05em Up}}}}''',
    r'''\newcommand{\MagDown}{\ensuremath{\mathrm{\textit{MagDown}}}}''',
    r'''\newcommand{\Lb}{\ensuremath{\Lambda_b^0}}''',
    r'''\newcommand{\Lz}{\ensuremath{\Lambda}}''',
    r'''\newcommand{\Dz}{\ensuremath{D^0}}''',
    r'''\newcommand{\Ks}{\ensuremath{K_s}}''',
    r'''\newcommand{\jpsi}{\ensuremath{J\mskip -3mu/\mskip -2mu\psi\mskip 2mu}}''',
]

def prepend_preamble(cmd):
    return [cmd, ] + preamble

def append_preamble(cmd):
    return preamble + [cmd, ]

def create(filename, code, size=size_small, preamble=preamble, monochrome=True):
    basename = filename.split('.')[0]
    gpfilename = '{}.{}'.format(basename, 'gp')
    texfilename = '{}.{}'.format(basename, 'tex')

    with open(os.path.join('img', gpfilename), 'w') as f:
        color_type = 'monochrome' if monochrome else 'color'
        f.write('set terminal epslatex size {}, {} {} standalone "" 9 header \'{}\'\n'
                .format(*size, color_type, ' '.join(preamble)))

        f.write('set output \'{}\'\n'.format(texfilename))
        f.write('load \'/home/jovyan/scripts/parula.pal\'\n')
        f.write('set datafile separator \',\'\n\n')

        macros = '/home/jovyan/scripts'
        f.write('set macros\nset loadpath \'{}\'\n\n'.format(macros))

        f.write(code.strip())

    return 'gp2png.sh {} {} {}'.format(gpfilename, texfilename, color_type)
