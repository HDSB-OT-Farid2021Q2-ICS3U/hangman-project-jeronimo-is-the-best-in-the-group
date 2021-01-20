empty = [' ', ' ', ' ', ' ', ' ', ' ']
breakfast = ['c','a', 'n', 'a', 'd', 'a']
guess = ['a', 'c']
emptyview = [x if x in guess else ' ' for x in breakfast]

print(emptyview)
