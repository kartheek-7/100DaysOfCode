
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        
    def add_child(self,child):
        self.children.append(child)
        child.parent=self
        
    def get_level(self):
        level=0
        while self.parent :
            level+=1
            self=self.parent
        return level
        
    def print_tree(self):
        print(" "*(2*self.get_level())+"|"+ self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
            
count=0   
one=TreeNode("India")
t1=TreeNode("Telangana")
t2=TreeNode("Andhra Pradesh")
t3=TreeNode("Tamilnadu")
t4=TreeNode("karnataka")
t5=TreeNode("Hyderabad")
t6=TreeNode("Nalagonda")
t7=TreeNode("Warangal")
t8=TreeNode("Miryalaguda")
t9=TreeNode("Guntur")
t10=TreeNode("Visaka")
t11=TreeNode("chennai")
t12=TreeNode("Banglore")

one.add_child(t1)
one.add_child(t2)
one.add_child(t3)
one.add_child(t4)

t1.add_child(t5)
t1.add_child(t6)
t1.add_child(t7)

t2.add_child(t9)
t2.add_child(t10)

t3.add_child(t11)

t4.add_child(t12)

t6.add_child(t8)

one.print_tree()
#print(t8.get_level())   