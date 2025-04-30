
tree_height = int(input())
cii = 1
for i in range(tree_height):
    print(' ' * (tree_height - (i+1)) + '*' * (i+cii) + ' ' * (tree_height - (i+1)))
    cii += 1