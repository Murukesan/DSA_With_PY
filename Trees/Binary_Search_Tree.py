class BST_node:
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None
    def Add_node(self,Node):
        if self.node>Node:
            if self.left:
                self.left.Add_node(Node)
            else:
                self.left=BST_node(Node)
        elif self.node<Node:
            if self.right:
                self.right.Add_node(Node)
            else:
                self.right = BST_node(Node)
        else:
            print("Data already exists in Binary serach tree")

    def remove(self, value):
        if value < self.node:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.node:
            if self.right:
                self.right = self.right.remove(value)
        else:
            # Case 1: No children
            if self.left is None and self.right is None:
                return None
            # Case 2: Only right child
            elif self.left is None:
                return self.right
            # Case 3: Only left child
            elif self.right is None:
                return self.left
            # Case 4: Two children
            else:
                min_larger = self.right.find_min()
                self.node = min_larger.node
                self.right = self.right.remove(min_larger.node)
        return self

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.node,end=',')
        if self.right:
            self.right.inorder()
    def search(self,nts):
        if self.node>nts:
            if self.left:
                return self.left.search(nts)
            else:
                return False
        elif self.node<nts:
            if self.right:
                return self.right.search(nts)
            else:
                return False
        else:
            # Found the node
            return True

    def find_min(self):
        current = self
        while current.left:  # stop when there is no more left child
            current = current.left
        return current.node


if __name__=='__main__':
    root=None
    while True:
        print("1. Insert node")
        print("2. Remove node")
        print('3. Inorder Traversal')
        print("4. Search a node")
        print("5. Find minimum")
        print('6. Exit')

        try:
            option = int(input("Enter option: "))
        except ValueError:
            print("Enter valid number")
            continue
        if option==1:
            Node=int(input("Please enter the node to insert"))
            if root is None:
                root=BST_node(Node)
            else:
                root.Add_node(Node)
        elif option==2:
            if root is None:
                print("Tree is empty")
                continue
            else:
                Node = int(input("Please enter the node to remove"))
                root.remove(Node)
        elif option==3:
            if root is None:
                print("Tree is Empty")
            else:
                root.inorder()
                print()
        elif option==4:
            try:
                nts=int(input("Enter the node to search:"))
                if root is None:
                    print("Tree is Empty")
                else:
                    if root.node==nts:
                        print('Element found at root node')
                    else:
                        if root.search(nts):
                            print("Element found")
                            continue
                        else:
                            print("Element not found")
                            continue
            except ValueError:
                print("Please Enter the correct value")
                continue
        elif option==5:
            if root is None:
                print("Tree is Empty")
            else:
                print(root.find_min())
        elif option==6:
            break

