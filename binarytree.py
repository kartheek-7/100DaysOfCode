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
    
    def inorder_BST(root):
        ele=[]
        if root.left:
            ele+=inorder_BST(root.left)
            
        ele.append(root.data)
        
        if root.right:
            ele+=inorder_BST(root.right)
            
        return ele     
            

def construct_BST(mat):
    root=BSTree(mat[0])
    n=len(mat)
    for i in range(1,n):
        root.add_element(mat[i])
    return root


        
    
    
if __name__=='__main__':
    ele=[17,4,20,1,9,18,23,34]
    root=construct_BST(ele)
    root.inorder_BST()
    
    
        