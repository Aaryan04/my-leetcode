"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        # start with this node's info
        parts = [str(root.val), str(len(root.children))]

        # recursively add all the children and its child list length
        for child in root.children:
            parts.append(self.serialize(child))

        return ",".join(parts)


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """

        if not data:
            return None
        
        data_q = deque(data.split(','))
        
        def build_tree():
            val = int(data_q.popleft())
            num_of_child = int(data_q.popleft())
            
            node = Node(val, [])

            for _ in range(num_of_child):
                child = build_tree()
                node.children.append(child)
            return node

        return build_tree()



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))