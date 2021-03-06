# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
from recommonmark.transform import AutoStructify
project = 'Java-Cookbook'
copyright = '2020, Frenude'
author = 'Frenude'

# The full version, including alpha/beta/rc tags
release = '0.1.1'


# -- General configuration ---------------------------------------------------
# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.autosectionlabel',
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'java-cookbookdoc'


# -- Options for LaTeX output ---------------------------------------------
latex_elements = {  # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',  # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt', 'classoptions': ',oneside', 'babel': '',  # 必須
    'inputenc': '',  # 必須
    'utf8extra': '',  # 必須
    # Additional stuff for the LaTeX preamble.
    # use fc-list :lang=zh to see available fonts
    # \usepackage{indentfirst}
    # \setlength{\parindent}{2em}
    'preamble': r"""
\usepackage{xeCJK}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
"""}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'java-cookbook.tex', u'java-cookbook Documentation',
     u'Frenude', 'howto'),
]

# open for create pdf
# latex_engine = 'xelatex'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'java-cookbook', u'java-cookbook Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'java-cookbook', u'java-cookbook Documentation',
     author, 'java-cookbook', 'One line description of project.',
     'Miscellaneous'),
]

github_doc_root = "https://github.com/frenude/java-cookbook"
# At the bottom of conf.py


# def setup(app):
#     app.add_config_value('recommonmark_config', {
#         'url_resolver': lambda url: github_doc_root + url,
#         'auto_toc_tree_section': 'Contents',
#     }, True)
#     app.add_transform(AutoStructify)
