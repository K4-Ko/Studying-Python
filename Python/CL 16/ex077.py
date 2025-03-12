# Create a program that has a tuple with several words.  
# Then, for each word, display which vowels it contains.

l = ('mouse', 'lamp', 'stone', 'chair', 'door',)
print('\nThe following words has the following vowels: ')
for p in l:
    print(f'\n{p}: ', end=' ')
    for v in p:
        if v in 'aeiou':
            print(v, end=' ')