'''Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate_BST(root)
        
    def validate_BST(self,root):
        if root == None:
            return True
        else:
            return self.validate_tree(root,[],True)
                    
                
        
    def validate_tree(self,pntr,temp,res):
        if pntr.left:
            res = self.validate_tree(pntr.left,temp,res)
        
        if len(temp) >= 1 and pntr.val <= temp[-1]:
            return False
        else:
            temp.append(pntr.val)
        if pntr.right:
            res = self.validate_tree(pntr.right,temp,res)
        return res
        
        