PLY (Python Lex-Yacc) - Mini-Lisp Implementation

Introduction
============

PLY is a 100% Python implementation of the common parsing tools lex
and yacc. Here are a few highlights:

 -  PLY is very closely modeled after traditional lex/yacc.
    If you know how to use these tools in C, you will find PLY
    to be similar.

 -  PLY provides *very* extensive error reporting and diagnostic 
    information to assist in parser construction.  The original
    implementation was developed for instructional purposes.  As
    a result, the system tries to identify the most common types
    of errors made by novice users.  

 -  PLY provides full support for empty productions, error recovery,
    precedence specifiers, and moderately ambiguous grammars.

 -  Parsing is based on LR-parsing which is fast, memory efficient, 
    better suited to large grammars, and which has a number of nice
    properties when dealing with syntax errors and other parsing problems.
    Currently, PLY builds its parsing tables using the LALR(1)
    algorithm used in yacc.

 -  PLY uses Python introspection features to build lexers and parsers.  
    This greatly simplifies the task of parser construction since it reduces 
    the number of files and eliminates the need to run a separate lex/yacc 
    tool before running your program.

 -  PLY can be used to build parsers for "real" programming languages.
    Although it is not ultra-fast due to its Python implementation,
    PLY can be used to parse grammars consisting of several hundred
    rules (as might be found for a language like C).  The lexer and LR 
    parser are also reasonably efficient when parsing typically
    sized programs.  People have used PLY to build parsers for
    C, C++, ADA, and other real programming languages.

How to Use
==========

PLY consists of two files : lex.py and yacc.py.  These are contained
within the 'ply' directory which may also be used as a Python package.
To use PLY, simply copy the 'ply' directory to your project and import
lex and yacc from the associated 'ply' package.  For example:

     import ply.lex as lex
     import ply.yacc as yacc

Alternatively, you can copy just the files lex.py and yacc.py
individually and use them as modules.  For example:

     import lex
     import yacc

The file setup.py can be used to install ply using distutils.

The file doc/ply.html contains complete documentation on how to use
the system.

The example directory contains several different examples including a
PLY specification for ANSI C as given in K&R 2nd Ed.   

A simple example is found at the end of this document

Requirements
============
PLY requires the use of Python 2.2 or greater.  However, you should
use the latest Python release if possible.  It should work on just
about any platform.  PLY has been tested with both CPython and Jython.
It also seems to work with IronPython.
