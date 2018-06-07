import time
import os
from IPython.display import display, HTML

size_small = (2.8, 2.1)
size_medium = (4.0, 3.0)

texmacros = [
    r'''\newcommand{\mevcc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c^2}}''',
    r'''\newcommand{\mevc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c}}''',
    r'''\newcommand{\gevcc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c^2}}''',
    r'''\newcommand{\gevc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c}}''',
    r'''\newcommand{\MagUp}{\ensuremath{\mathrm{\textit{Mag\kern -0.05em Up}}}}''',
    r'''\newcommand{\MagDown}{\ensuremath{\mathrm{\textit{MagDown}}}}''',
]

def create(filename, code, size = size_small):
    basename = filename.split('.')[0]
    gpfilename = '{}.{}'.format(basename, 'gp')
    texfilename = '{}.{}'.format(basename, 'tex')

    with open(gpfilename, 'w') as f:
        f.write('set terminal epslatex size {}, {} color standalone "" 9 header \'{}\'\n'
                .format(*size, ' '.join(texmacros)))

        f.write('set output \'{}\'\n'.format(texfilename))
        f.write('load \'parula.pal\'\n')
        f.write('set datafile separator \',\'\n\n')
        f.write(code.strip())

    return './gp2png.sh {} {}'.format(gpfilename, texfilename)

def show_fig(filename, directory = 'img', width = 400):
    html_template = '<img src="{0}?{1}" alt="{0}" width="{2}">'
    rnd = time.time() # fool caching
    fullname = os.path.join(directory, filename)
    display(HTML(html_template.format(fullname, rnd, width)))
