# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Parallel.GAMIT'
copyright = '2024, Demián D. Gómez'
author = 'Demián D. Gómez'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os
import sys
from unittest.mock import MagicMock # for mock importing for autodoc and argparse
sys.path.insert(0, os.path.abspath(".."))

extensions = ['sphinx.ext.viewcode','sphinx.ext.autodoc', 'sphinx_argparse_cli', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Mocking -----------------------------------------------------------------

# mock modules 
MOCK_MODULES = ['psycopg2', 'psycopg2.extras', 'psycopg2.extensions', 'pg','pgdb']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = MagicMock(return_value = "")

# Mock file operations during documentation build
original_open = open
def mock_file_open(path, mode='r', **kwargs):
    path = str(path)
    if path.endswith('.cfg'):
        filename = os.path.basename(path)
        path = os.path.join('../configuration_files', filename) # assume current dir is docs
    return original_open(path, mode, **kwargs)

# Apply the mock during documentation build
import builtins
builtins.open = mock_file_open

# -- LaTeX Unicode Fix -------------------------------------------------------
latex_elements = {
    'preamble': r'''
    \usepackage[utf8]{inputenc}
    \DeclareUnicodeCharacter{202F}{ }
    ''',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_static_path = ['_static']
