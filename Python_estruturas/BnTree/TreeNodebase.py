class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# in order 
# planifica a arvore e atravvessa em ordem
#esquerda, atual e depois direita

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end= " ")
    inorder(node.right)

inorder(root)
print(end="\n\n")

# pre order
#abre a atual, depois esquerda, depois direita
def preorder(node):
    if not node:
        return
    print(node.val, end= " ")
    preorder(node.left)
    preorder(node.right)

preorder(root)

print(end="\n\n")

# post order
#abre a esquerda, depois direita, depois atual
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end= " ")

postorder(root)