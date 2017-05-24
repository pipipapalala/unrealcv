#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, glob, shutil, subprocess
doc_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(doc_dir)
sys.path.insert(0, doc_dir)

# If runs on ReadTheDocs environment
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Hack for lacking git-lfs support ReadTheDocs
if on_rtd:
    print('Fetching files with git_lfs for %s' % project_dir)
    from git_lfs import fetch
    fetch(project_dir)

    subprocess.call('doxygen Doxyfile', shell=True)
    # Generate xml from doxygen

import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx_gallery.gen_gallery',
    'breathe',
]

sphinx_gallery_conf = {
    'examples_dirs': ['tutorials_source'],
    'gallery_dirs': ['tutorials'],
    'filename_pattern': 'tutorial.py',
    'backreferences_dir': False,
}

for i in range(len(sphinx_gallery_conf['examples_dirs'])):
    gallery_dir = sphinx_gallery_conf['gallery_dirs'][i]
    source_dir = sphinx_gallery_conf['examples_dirs'][i]
    # Create gallery dirs if it doesn't exist
    if not os.path.isdir(gallery_dir):
        os.mkdir(gallery_dir)

    # Copy rst files from source dir to gallery dir
    for f in glob.glob(os.path.join(source_dir, '*.rst')):
        shutil.copy(f, gallery_dir)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'UnrealCV'
copyright = '2017, UnrealCV team'
author = 'UnrealCV contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
exclude_patterns += sphinx_gallery_conf['examples_dirs']
exclude_patterns += ['*/index.rst']
print(exclude_patterns)

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'logo_only': False,
}


# Output file base name for HTML help builder.
htmlhelp_basename = 'UnrealCVDoc'

breathe_projects = {
    "unrealcv": "./doxygen/xml/",
}
breathe_default_project = 'unrealcv'
