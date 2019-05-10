#!/usr/bin/env python
""" This example demonstrates that you need to run
'pip install .' in the main directory, before you
can do 'import spyce' in a Python program"""

try:
    import spyce
    print("Succesfully imported spyce!")
except ImportError:
    print("Could not import spyce! Maybe you forgot to run 'pip install'")
