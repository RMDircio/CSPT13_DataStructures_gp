'''--------------Artem Lecture CSPT 8----------------------'''



# code from lecture that might be useful for the assignment
''' 
Wrap the given value in a ListNode and insert it after this node. 
Note that this node could already have a next node it is pointing to.
'''
def insert_after(self,value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
        current_next.prev = self.next

'''
Wrap the given value in a ListNode and insert it before this node.
Note that this node could already have a previous node it is pointing to
'''

def insert_before(self,value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
        current_prev.next = self.prev

'''
Rearranges this ListNode's pervious and next pointers accordingly,
effectively deleting this ListNode
'''

def delete(self):
    if self.prev:
        self.prev.next = self.next
    if self.next:
        self.next.prev = self.prev



