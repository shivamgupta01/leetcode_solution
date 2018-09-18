#   Back to Chapter
# Array
# Array type of questions were asked in interviews frequently. You will most likely encounter one during your interviews. We recommend: Single Number, Rotate Array, Intersection of Two Arrays II and Two Sum.
# Strings
# String type of questions were asked in interviews frequently. You will most likely encounter one during your interviews. We recommend: Reverse String, First Unique Character in a String, String to Integer (atoi) and Implement strStr().
#   Reverse String
#   Reverse Integer
#   First Unique Character in a String
#   Valid Anagram
#   Valid Palindrome
#   String to Integer (atoi)
#   Implement strStr()
#   Count and Say
#   Longest Common Prefix
# Linked List
# Linked List problems are relatively easy to master. Do not forget the Two-pointer technique, which not only applicable to Array problems but also Linked List problems as well. Another technique to greatly simplify coding in linked list problems is the dummy node trick. We recommend: Reverse Linked List, Merge Two Sorted Lists and Linked List Cycle. For additional challenge, solve these problems recursively: Reverse Linked List, Palindrome Linked List and Merge Two Sorted Lists.
# Trees
# Tree is slightly more complex than linked list, because the latter is a linear data structure while the former is not. Tree problems can be solved either breadth-first or depth-first. We have one problem here which is great for practicing breadth-first traversal. We recommend: Maximum Depth of Binary Tree, Validate Binary Search Tree, Binary Tree Level Order Traversal and Convert Sorted Array to Binary Search Tree.
# Sorting and Searching
# These problems deal with sorting or searching in a sorted structure. We recommend First Bad Version as a great introduction to a very important algorithm.
# Dynamic Programming
# Here are some classic Dynamic Programming interview questions. We recommend: Climbing Stairs, Best Time to Buy and Sell Stock and Maximum Subarray.
# Design
# These problems may require you to implement a given interface of a class, and may involve using one or more data structures. These are great exercises to improve your data structure skills. We recommend: Shuffle an Array and Min Stack.
# Math
# Most of the math questions asked in interviews do not require math knowledge beyond middle school level. We recommend: Count Primes and Power of Three.
# Others
# Here are some other questions that do not fit in other categories. We recommend: Number of 1 Bits and Valid Parentheses.
#
#  PreviousNext
#   Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.




class Solution(object):
    def isPalindrome(self, s):
        temp = []

        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        i = 0
        j = len(temp)-1
        while(j>i):
            if temp[i]!=temp[j]:
                return False
            i +=1
            j-=1

        return True




if __name__ == '__main__':
    s = Solution()
    print "solutin : " + str(s.isPalindrome('00'))