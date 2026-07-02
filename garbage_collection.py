import gc
import sys

class Node:
    def __init__(self, name):
        self.value = name
        self.next = None



#create nodes

a = Node("A")
b = Node("B")
print(f"Initial reference count of a: {sys.getrefcount(a)}")
print(f"Initial reference count of b: {sys.getrefcount(b)}")


#create circular reference
a.next = b
b.next = a
print(f"Reference count of a after circular reference: {sys.getrefcount(a)}")
print(f"Reference count of b after circular reference: {sys.getrefcount(b)}")


#delete references
print("Deleting references to a and b...")
del a
del b

#Note: At this point, the reference counts of the objects are still greater than zero due to the circular reference, so they won't be collected by the garbage collector yet.   
collected = gc.collect()
print(f"Garbage collector: collected {collected} objects.")
