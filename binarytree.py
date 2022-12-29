class BSTree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def add_element(self,child):
        if self.data==child:
            return
        if self.data>child:
            if self.left:
                self.left.add_element(child)
            else:
                self.left=BSTree(child)
        
        else:
            if self.right:
                self.right.add_element(child)
            else:
                self.right=BSTree(child)

    def get_level(self,ele):
        count=0
        if self.data==ele:
            return 0
        while self:
            count+=1
            if self.left==ele:
                pass
    
    def inorder_BST(self):
        ele=[]
<<<<<<< HEAD
        if self.left:
            ele+=self.left.inorder_BST()
=======
        if root.left:
            ele+=root.left.inorder_BST()
>>>>>>> 22f18fc2cca5fbfc818ac3fb61020a6f545498f7
            
        ele.append(self.data)
        
<<<<<<< HEAD
        if self.right:
            ele+=self.right.inorder_BST()
=======
        if root.right:
            ele+=root.right.inorder_BST()
>>>>>>> 22f18fc2cca5fbfc818ac3fb61020a6f545498f7
            
        return ele
    
    def search_ele(self,val):
        
        if self.data==val:
            return True
        if self.data>val:
            if self.left:
                return self.left.search_ele(val)
            else:
                return False
            
        else:
            if self.right:
                return self.right.search_ele(val)
            else:
                return False
        
            

def construct_BST(mat):
    root=BSTree(mat[0])
    n=len(mat)
    for i in range(1,n):
        root.add_element(mat[i])
    return root


        
    
    
if __name__=='__main__':
    ele=[17,4,20,1,9,18,23,34]
    root=construct_BST(ele)
    print(root.inorder_BST())
    print(root.search_ele(23))
    
        
