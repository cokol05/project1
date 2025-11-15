import os
import sys
from datetime import datetime


sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../taskmanager'))

project = 'Console task manager'
copyright = f'{datetime.now().year}, Anton'
author = 'Anton'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'special-members': '__init__',
    'show-inheritance': True,
}

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

html_static_path = ['_static']

html_show_sourcelink = True
html_show_sphinx = False
