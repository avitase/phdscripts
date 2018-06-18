import time
import os
from IPython.display import display, HTML

def show_fig(file_name, directory='img', width=400, fool_caching=True):
    html_template = '<img src="{0}" alt="{1}" width="{2}">'
    full_name = os.path.join(directory, file_name)
    if fool_caching:
        rnd = str(time.time())
        full_name += '?' + rnd
    display(HTML(html_template.format(full_name, file_name, width)))

