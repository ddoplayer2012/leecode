# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     二叉树
   Description :
   Author :       me
   date：          2019/8/5
-------------------------------------------------
   Change Activity:
                   2019/8/5:
-------------------------------------------------
"""
__author__ = 'me'

class Node(object):
    def __init__(self,item):
        self.item=item #表示对应的元素
        self.left=None #表示左节点
        self.right=None #表示右节点
    def __str__(self):
        return str(self.item)  #print 一个 Node 类时会打印 __str__ 的返回值
class Tree(object):
    def __init__(self):
        self.root=Node('root')  #根节点定义为 root 永不删除，作为哨兵使用。
    def add(self,item):
        node = Node(item)
        if self.root is None:  #如果二叉树为空，那么生成的二叉树最终为新插入树的点
            self.root = node
        else:
            q = [self.root] # 将q列表，添加二叉树的根节点
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None: #左子树为空则将点添加到左子树
                    pop_node.left = node
                    return
                elif pop_node.right is None: #右子树为空则将点添加到右子树
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    def get_parent(self, item):
        if self.root.item == item:
            return None  # 根节点没有父节点
        tmp = [self.root] # 将tmp列表，添加二叉树的根节点
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item: #某点的左子树为寻找的点
                return pop_node #返回某点，即为寻找点的父节点
            if pop_node.right and pop_node.right.item == item: #某点的右子树为寻找的点
                return pop_node #返回某点，即为寻找点的父节点
            if pop_node.left is not None: #添加tmp 元素
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None
    def delete(self, item):
        if self.root is None:  # 如果根为空，就什么也不做
            return False

        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.item == item else parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False