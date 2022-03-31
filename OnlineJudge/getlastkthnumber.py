# A simple definition of linked Node.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


head = None

# Read list of data and construct linked list
raw_values = input()
last = None
for value in [int(x) for x in raw_values.split()]:
    node = Node(value)
    if head is None:
        head = node
    else:
        last.next = node
    last = node

# Don't modify code above.

def getLastKthNumber(head, k):
    ''' Please complete this function below,
    and return a value as answer.'''

    p = head
    length = 1
    while p.next is not None:
        p = p.next
        length += 1

    i = 1
    p = head
    while i < length - k + 1:
        p = p.next
        i += 1
    return p.value


    ''' Please complete this function above.'''

# Don't modify code below.

# Evaluate result returned from your function
k = int(input())
result = getLastKthNumber(head, k)
print(result)