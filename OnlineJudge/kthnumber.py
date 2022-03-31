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


def getKthNumber(head, k):
    '''
    Please complete this function below, and return a value as answer.
    '''

    p = head
    i = 1
    while i < k:
        p = p.next
        i += 1
    return p.value

    ''' Please complete this function above.'''

# Don't modify code below.

# Evaluate result returned from your function
k = int(input())
result = getKthNumber(head, k)
print(result)