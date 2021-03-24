class binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_root(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_root(data)
            else:
                self.left=binarytree(data)
        if data>self.data:
            if self.right:
                self.right.add_root(data)
            else:
                self.right=binarytree(data)
    def preorder(self):
        el=[]
        el.append(self.data)
        if self.left:
            el+=self.left.preorder()
        if self.right:
            el+=self.right.preorder()
        return el
def build_tree(el):
    print(el)
    root=binarytree(el[0])
    for i in range(1,len(el)):
        root.add_root(el[i])
    return root
if __name__=='__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbers_tree.add_root(86))
    print(numbers_tree.preorder())
    

    
    
