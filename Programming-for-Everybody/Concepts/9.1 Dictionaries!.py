'''
Dictionaries!

    - Lists index their entries based on the position in the list
    - Dictionaries are like bags - no order
    - So we index the things we put in the dictionary with a 'lookup tag'
'''
# For reference, we're putting 12 in the purse, tagging it with money. 
# The key is money and the 12 is the value in the key/value pair.
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)