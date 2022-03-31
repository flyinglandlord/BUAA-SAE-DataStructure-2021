class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_in(node_list):
    list_in = input().split()
    l = len(list_in)
    node_list.append(Node(list_in[0]))
    for i in range(1, l):
        if list_in[i] == "None":
            node_list.append(None)
        else:
            new_node = Node(list_in[i])
            node_list.append(new_node)
            if(i % 2 == 1):
                k = (i-1)//2
                while(node_list[k] == None):
                    k += 1
                node_list[k].left = new_node
            else:
                k = (i-2)//2
                while (node_list[k] == None):
                    k += 1
                node_list[k].right = new_node


node_list = []
tree_in(node_list)
ans = 0
for i in node_list:
    if(i == None):
        pass
    elif(i.left == None):
        pass
    else:
        ans += int(i.left.data)
print(ans)