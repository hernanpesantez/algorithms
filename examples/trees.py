from binarytree import tree, bst, heap, Node, build
# Generate a random binary tree and return its root node
my_tree = tree(height=3, is_perfect=False)
# Generate a random BST and return its root node

x =build ([2,4,5,6,7])
print(dir(bst))
my_bst = bst(2)
# Generate a random max heap and return its root node
my_heap = heap(height=3, is_max=True, is_perfect=False)

# Pretty-print the trees in stdout
print(my_tree)
#
#        _______1_____
#       /             \
#      4__          ___3
#     /   \        /    \
#    0     9      13     14
#         / \       \
#        7   10      2
#
print(my_bst)
#
#            ______7_______
#           /              \
#        __3__           ___11___
#       /     \         /        \
#      1       5       9         _13
#     / \     / \     / \       /   \
#    0   2   4   6   8   10    12    14
#
print(my_heap)
#
#              _____14__
#             /         \
#        ____13__        9
#       /        \      / \
#      12         7    3   8
#     /  \       /
#    0    10    6
#

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root)
#
#        __1
#       /   \
#      2     3
#     / \
#    4   5
#
root.inorder
print('inorder ',root.inorder)

print('preorder ',root.preorder)
# [Node(1), Node(2), Node(4), Node(5), Node(3)]

print('postorder ',root.postorder)
# [Node(4), Node(5), Node(2), Node(3), Node(1)]

print('levelorder ',root.levelorder)
# [Node(1), Node(2), Node(3), Node(4), Node(5)]

list(root)  # Equivalent to root.levelorder
# [Node(1), Node(2), Node(3), Node(4), Node(5)]