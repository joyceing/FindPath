# -*- coding:utf-8 -*-
import copy
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right =None
class Solution:
    def FindPath(self,root,expectNumber):
        if not root:
            return[]
        currentSum=0
        path=[]
        result=[]
        self.FindPathto(root,expectNumber,path,currentSum,result)
        return result
    def FindPathto(self,root,expectNumber,path,currentSum,result):
        currentSum += root.val
        path.append(root.val)
        #如果是叶节点，并且路径上的节点值等于输入值
        #则打印该路径
        isLeaf= (root.left==None and root.right==None)
        if (currentSum==expectNumber and isLeaf):
            # print("A path is found:")
            #print(path)
            # return path
            result.append(copy.deepcopy(path))
            # result.extend(path)
        #如果不是叶节点，则遍历它的子节点
        if root.left !=None:
            self.FindPathto(root.left,expectNumber,path,currentSum,result)
        if root.right !=None:
            self.FindPathto(root.right,expectNumber,path,currentSum,result)
        #返回父节点之前，在路径上删除当前节点
        path.pop()
        # return result

node1=TreeNode(10)
node2=TreeNode(5)
node3=TreeNode(12)
node4=TreeNode(4)
node5=TreeNode(7)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
S=Solution()
print(S.FindPath(node1,22))
