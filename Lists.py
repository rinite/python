inventory = {'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Here the dictionary access expression takes the place of a list name 

# Your code here
inventory['pocket'] = ('seashell', 'strange berry', 'lint')


print inventory['gold']
inventory['gold'] = inventory['gold'] + 50
print inventory['gold']

inventory['backpack'].sort()
inventory['backpack'].remove('dagger')

print inventory['backpack']
