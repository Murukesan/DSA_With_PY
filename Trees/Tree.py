class Tree_node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def preorder(self,root): #root,left, right
        if root is None:
            return
        print(root.data,end=',')
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root): #left,right,root
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=',')


    def inorder(self,root): #left,root,right
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=',')
        self.inorder(root.right)

root=Tree_node('A')
node1=Tree_node('B')
node2=Tree_node('C')
node3=Tree_node('D')
node4=Tree_node('E')
node5=Tree_node('F')
node6=Tree_node('G')

root.left=node1
root.right=node2

node1.left=node3
node1.right=node4

node2.left=node5
node2.right=node6
#         A
#        / \
#       B   C
#      / \ / \
#     D  E F  G


print(root.left.left.data)
print("Preorder")
root.preorder(root)
print("\n")
print("Postorder")
root.postorder(root)
print("\n")
print("Inorder")
root.inorder(root)
