import time
import os
from IPython.display import display, HTML

def show_fig(filename, directory='img', width=400, fool_caching=True):
    html_template = '<img src="{0}" alt="{0}" width="{2}">'
    rnd = str(time.time()) if fool_caching else ''
    fullname = os.path.join(directory, filename)
    display(HTML(html_template.format(fullname, '?' + rnd, width)))

