class ListNode
def __init __(self, val=0, next=None);
self.val=val
self.next=next
def remove_duplicates(head);
current=head
while current and current.next;
if current.val==current.next.val:
  current.next=current.next.next
else:
  current = current.next
  return head;
