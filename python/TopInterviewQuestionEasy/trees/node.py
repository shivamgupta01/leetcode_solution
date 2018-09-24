class Node:

    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

class binarySearchTree:

    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            ## Insertion without Recursion
            # pntr = self.root
            # while data != pntr.data:
            #     if data > pntr.data: 
            #         if pntr.rightNode == None:
            #             pntr.rightNode = newNode
            #             break
            #         pntr = pntr.rightNode
                    
            #     elif data < pntr.data:
            #         if  pntr.leftNode == None:
            #             pntr.leftNode = newNode
            #             break
            #         pntr = pntr.leftNode

            ## Insertion with recursion
            self.insert_node(self.root,data)

    def insert_node(self,pntr,data):
        if data < pntr.data:
            if pntr.leftNode == None:
                pntr.leftNode = Node(data)
            else:
                self.insert_node(pntr.leftNode,data)
        elif data > pntr.data:
            if pntr.rightNode == None:
                pntr.rightNode = Node(data)
            else:
                self.insert_node(pntr.rightNode,data)    

    def get_minimum(self):
        if self.root:
            return self.minimum(self.root)
        else:
            return "No node in tree"
    
    def minimum(self,pntr):
        if pntr.leftNode:
            return self.minimum(pntr.leftNode)
        return pntr.data
            
    def get_maximum(self):
        if self.root:
            return self.maximum(self.root)
        else:
            return "No node in tree"
    
    def maximum(self,pntr):
        if pntr.rightNode != None:
            return self.maximum(pntr.rightNode)
        return pntr.data
    def in_order_traversal(self):
        if self.root:
            self.in_order(self.root)
    
    def in_order(self,pntr):
        if pntr.leftNode:
            self.in_order(pntr.leftNode)
        print(pntr.data)
        if pntr.rightNode:
            self.in_order(pntr.rightNode)

    def pre_order_traversal(self):
        if self.root:
            self.pre_order(self.root)
    
    def pre_order(self,pntr):
        print(pntr.data)
        if pntr.leftNode:
            self.pre_order(pntr.leftNode)
        if pntr.rightNode:
            self.pre_order(pntr.rightNode)

        # [32,10,1,19,16,23]
            
    def post_order_traversal(self):
        if self.root:
            self.post_order(self.root)
    
    def post_order(self,pntr):
        if pntr.leftNode:
            self.post_order(pntr.leftNode)
        if pntr.rightNode:
            self.post_order(pntr.rightNode)
        print(pntr.data)


if __name__ == '__main__':
    s = binarySearchTree()
    s.insert(32)
    s.insert(10)
    s.insert(1)
    s.insert(19)
    s.insert(16)
    s.insert(23)
    s.insert(55)
    s.insert(79)
    # print(s.get_minimum())
    # print(s.get_maximum())
    # s.in_order_traversal()
    # s.pre_order_traversal()
    s.post_order_traversal()