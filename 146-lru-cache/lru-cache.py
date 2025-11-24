class Node:
    def __init__(self, key, val):
        # each node will be having a (key, val), prev pointer, next pointer
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # LEFT(LRU) <=> (LRU)node1 <=> node2(MRU) <=> RIGHT(MRU)
    def __init__(self, capacity: int):
        self.cap = capacity     # capacity of the cache
        self.cache = {} # map key to nodes

        # left pointer node keeps track of LRU and 
        # right pointer node keeps track of MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left        # doubly L.L.

    # helper function 1
    # remove node from list
    def remove(self, node):
        # connect prev of the node with next of node
        # two pointers prev and nxt
        prev, nxt = node.prev, node.next       
        prev.next, nxt.prev = nxt, prev

    # helper function 2
    # insert node at right
    def insert(self, node):
        # inserting in the prev of right(MRU)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])        # remove from cache
            self.insert(self.cache[key])        # and insert at right (MRU)
            return self.cache[key].val          # return the val of the key since key is a node          
        return -1      # return -1 if key does not exist in the cache

    def put(self, key: int, value: int) -> None:
        # check if the same key already exists in the cache
        if key in self.cache:
            self.remove(self.cache[key])        # remove from cache
        self.cache[key] = Node(key, value)      # assign a new node of the key to be inserted
        self.insert(self.cache[key])            # insert to the right
        
        # after inserting, need to check if the len of cache is not exceeding the capacity
        # if exceeding then remove LRU (node next to Left)
        if len(self.cache) > self.cap:          
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]     # delete from the cache as well

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)