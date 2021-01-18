empty = [' ', ' ', ' ', ' ', ' ', ' ']
breakfast = ['c','a', 'n', 'a', 'd', 'a']
guess = ['a']
emptyview = [x if x in guess else ' ' for x in breakfast]

print(emptyview)
