'''
An Even Shorter Version

    - List comprehension creates a dynamic list.
    - In this case, we make a list of reversed tuples and then sort it.
    - More information at http://wiki.python.org/moin/HowTo/Sorting
'''
c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )