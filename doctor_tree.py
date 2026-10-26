class DoctorNode:
    def __init__(self, doctorName):
            self.doctorName = doctorName #This is our value we're keeping track of.
            self.left = None
            self.right = None



class DoctorTree:
    def __init__(self):
        self.DoctorNode = None #This is our root node of the tree. It starts as None because the tree is empty.

    def insert(self, parent_name, employee_name, side, current_node=None):
        if self.DoctorNode is None: #Case 1: The Tree Is Empty.
             print("Tree is empty. Please insert a root node first.")
             return
        
        if current_node is None: #Starts from the root which is DoctorNode because there is no current node yet.
            current_node = self.DoctorNode

        #Case 2: We Found the Parent Node
        if current_node.doctorName == parent_name:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(employee_name) #Employee name is added because it is the new value of the node.
                print("Inserted", employee_name, "under ", parent_name, "on the left side.")
                return True

            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(employee_name)
                print("Inserted", employee_name, "under ", parent_name, "on the right side.")
                return True

            else:
                print(f"{parent_name} already has a {side} child.")
                return True

        #Case 3: We Haven't Found the Parent Node Yet So We Search the Subtrees
        found_left = False
        found_right = False

        if current_node.left:
             found_left = self.insert(parent_name, employee_name, side, current_node.left)

        if current_node.right and not found_left:
             found_right = self.insert(parent_name, employee_name, side, current_node.right)

        if not(found_left or found_right):
            if current_node == self.DoctorNode:
                print(f"Parent node {parent_name} is not found in the tree.")
                return False
            
        return found_left or found_right
    
    def preorder(self, DoctorNode): #Method where the root of the subtree is visited first, then the left, finally the right subtree.
          if DoctorNode is None:
               return []
          result = [DoctorNode.doctorName]
          result += self.preorder(DoctorNode.left)
          result += self.preorder(DoctorNode.right)

          return result

    def inorder(self, DoctorNode): #Method where the root of the subtree is visited first, then the left, finally the right subtree.
          if DoctorNode is None:
               return []
          result = []
          result += self.inorder(DoctorNode.left)
          result.append(DoctorNode.doctorName)
          result += self.inorder(DoctorNode.right)

          return result
    
    def postorder(self, DoctorNode): #Method where the root of the subtree is visited first, then the left, finally the right subtree.
         if DoctorNode is None:
              return []
         result = []
         result += self.postorder(DoctorNode.left)
         result += self.postorder(DoctorNode.right)
         result.append(DoctorNode.doctorName)

         return result

tree = DoctorTree()
tree.DoctorNode = DoctorNode("Dr. Wilson")

tree.insert("Dr. Wilson", "Dr. Smith", "right")
tree.insert("Dr. Wilson", "Dr. Johnson", "left")
tree.insert("Dr. Johnson", "Dr. Harris", "right")
tree.insert("Dr. Johnson", "Dr. Brown", "left")

result = tree.insert("Dr. Davis", "Dr.Taylor", "left") #This should print an error message because there is no Dr.Davis in the tree.
print(result)

print(tree.preorder(tree.DoctorNode))
print(tree.inorder(tree.DoctorNode))
print(tree.postorder(tree.DoctorNode))

#Use the online resources because they follow the same logic as a binary search tree. You can use the insert method to add new nodes to the tree, and you can use the left and right attributes to traverse the tree..