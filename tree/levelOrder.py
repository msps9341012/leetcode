def levelOrder(self, root):
        """
        設一個變數depth去紀錄深度
        考慮等於或不等於(child)
        """	
        if not root:
		    return []
        res=[]
        queue=[[root,0]]
        depth=-1
        while queue:
            node=queue.pop(0)
            if node[1]==depth:
                res[-1].append(node[0].val)
            else:
                res.append([node[0].val])
                depth=node[1]
            if node[0].left:
                queue.append([node[0].left,depth+1])
            if node[0].right:
                queue.append([node[0].right,depth+1])
        return res

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    ret = []
    
    if not root: 
        return ret
    
    def helper(node, level):
        
        if len(ret) < level:
            ret.append([node.val])
        else:
            ret[level-1].append(node.val)
            
        if node.left : helper(node.left, level+1)
        if node.right : helper(node.right, level+1)
            
    helper(root,1)
    return ret