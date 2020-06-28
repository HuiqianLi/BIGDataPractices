#二叉树
class Node(object):
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data #节点的数据域
        self.lchild = lchild #左孩子
        self.rchild = rchild #右孩子

#树类
class Tree(object):
    def __init__(self,root=Node(-1,None,None)):
        self.root=root
        self.height=0
        self.MyQueue=[]
    
    #按层次添加节点到树中
    def add(self,data):
        node=Node(data)
        
        if self.root.data==-1:
            self.root=node
            if not node.data==None:
                self.height+=1
                
            self.MyQueue.append(self.root)
        else:
            treeNode=self.MyQueue[0]
            if treeNode.lchild==None:
                treeNode.lchild=node
                if not node.data==None:
                    self.height+=1
                    
                self.MyQueue.append(treeNode.lchild)
            else:
                treeNode.rchild=node
                
                self.MyQueue.append(treeNode.rchild)
                self.MyQueue.pop(0)
            
    #层次遍历
    def level_order(self):
        if self.root==None:
            return
        MQ=[]
        node=self.root
        MQ.append(node)
        while MQ:
            node=MQ.pop(0)
            print(node.data)
            if node.lchild:
                MQ.append(node.lchild)
            if node.rchild:
                MQ.append(node.rchild)
                
    #前序遍历
    def pro__order(self,root):
        if root==None:
            return
        print(root.data)
        self.pro__order(root.lchild)
        self.pro__order(root.rchild)
    
    #中序遍历
    def mid_order(self,root):
        if root==None:
            return
        self.mid_order(root.lchild)
        print(root.data)
        self.mid_order(root.rchild)
        
      #后序遍历
    def post_order(self,root):
        if root==None:
            return
        self.post_order(root.lchild)
        self.post_order(root.rchild)   
        print(root.data)

    #二叉树中的最大深度
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.lchild),self.maxDepth(root.rchild)+1)
    
    #二叉树中的最大路径和
    def maxPathSum(self, root):   
        self.curr_max = float('-inf')
        def getMax(root):
            if root == None:
                return 0
            lchild = max(0,getMax(root.lchild))
            rchild = max(0,getMax(root.rchild))
            self.curr_max = max(self.curr_max , lchild + rchild + root.val)
            return max(lchild,rchild)+root.val
        getMax(root)
        return self.curr_max