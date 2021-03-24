class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spaces=' '*self.get_level()*3
        prefix=spaces+"!___" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
def build_product_tree():
    root = TreeNode("Nilupul")
    Chinmay = TreeNode("Chinmay")
    Chinmay.add_child(TreeNode("Vishwa"))
    Vishwa=TreeNode("Vishwa")
    Vishwa.add_child(TreeNode("Dhaval"))
    Vishwa.add_child(TreeNode("Abhijit"))
    Chinmay.add_child(Vishwa)
    Chinmay.add_child(TreeNode("Aamir"))
    Gels = TreeNode("Gels")
    Gels.add_child(TreeNode("Peter"))
    Gels.add_child(TreeNode("Waqas"))
    root.add_child(Chinmay)
    root.add_child(Gels)
    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
