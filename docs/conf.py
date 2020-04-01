# -*- coding: utf-8 -*-

import sys
import toml
from pathlib import Path
from pygments.lexers.python import CythonLexer
from sphinx.highlighting import lexers

pyproject = toml.load(Path(__file__).parents[1].joinpath('pyproject.toml'))
# -- Path setup --------------------------------------------------------------

sys.path.append(Path(__file__).parents[1])
# -- Project information -----------------------------------------------------

project = pyproject['tool']['poetry']['name']
copyright = '2019, dxfeed'
author = 'dxfeed'

# The short X.Y version
version = pyproject['tool']['poetry']['version']
# The full version, including alpha/beta/rc tags
release = pyproject['tool']['poetry']['version']


# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',  # numpy style docstrings
    'sphinx.ext.intersphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# The theme to use for HTML and HTML Help pages.
html_theme = 'alabaster'
html_theme_options = {
    'body_max_width': '80%',
    'show_powered_by': False,
    'sidebar_collapse': True
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'dxfeeddoc'

# remove view source link
html_show_sourcelink = False

# highlight cython
lexers['cython'] = CythonLexer()
