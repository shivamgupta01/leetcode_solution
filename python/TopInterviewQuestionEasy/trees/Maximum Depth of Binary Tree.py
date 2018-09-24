import node

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         return self.in_order_traversal(root)[-1]
#     def in_order_traversal(self,root):
#         if root:
#             return self.in_order(root,0,[])
    
#     def in_order(self,pntr,count,temp):
#         if pntr.leftNode:
#             count = count + 1
#             self.in_order(pntr.leftNode,count,temp)
            
#         else:
#             temp.append(count)
            
#         if pntr.rightNode:
#             count = count + 1
#             self.in_order(pntr.rightNode,count,temp)
            
#         else:
#             temp.append(count)
#         return temp
        
        

        

# if __name__ == '__main__':
#     s = Solution()
#     tree = node.binarySearchTree()
#     tree.insert(15)
#     tree.insert(14)
#     tree.insert(20)
#     tree.insert(None)
#     tree.insert(None)
#     tree.insert(16)
#     tree.insert(17)
#     print(s.maxDepth(tree.root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.



class Solution:
    def maxDepth(self, root):
        # if root == None: return 0
        # q = [root]
        # depth = 0
        # while q:
        #     depth += 1
        #     new = []
        #     for r in q:
        #         if r.left: new.append(r.left)
        #         if r.right: new.append(r.right)
        #     q = new
        # hieght =  depth

        return self.height(root)
    def height(self,pntr):
        if pntr == None:
            return 0
        return max(self.height(pntr.left),self.height(pntr.right)) + 1
        
    
