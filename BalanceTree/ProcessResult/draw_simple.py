import matplotlib.pyplot as plt

d_file = open("rbtree_simple_format.txt", "r")
lines = d_file.readlines()
length = len(lines)
rb_x = []
rb_y_ins = []
rb_y_del = []
rb_y_sea = []

for i in range(0, length, 6):
    rb_x.append(int(lines[i]))
    t_ins = 0.0
    t_del = 0.0
    t_sea = 0.0
    for j in range(i+1, i+6):
        d_line = lines[j].strip().split()
        t_ins += float(d_line[0])
        t_sea += float(d_line[1])
        t_del += float(d_line[2])
    t_ins /= 5
    t_del /= 5
    t_sea /= 5
    rb_y_ins.append(t_ins)
    rb_y_del.append(t_del)
    rb_y_sea.append(t_sea)


d_file = open("btree_simple.txt", "r")
lines = d_file.readlines()
length = len(lines)
b_x = []
b_y_ins = []
b_y_del = []
b_y_sea = []

for i in range(0, length, 6):
    b_x.append(int(lines[i]))
    t_ins = 0.0
    t_del = 0.0
    t_sea = 0.0
    for j in range(i+1, i+6):
        d_line = lines[j].strip().split()
        t_ins += float(d_line[0])
        t_sea += float(d_line[1])
        t_del += float(d_line[2])
    t_ins /= 5
    t_del /= 5
    t_sea /= 5
    b_y_ins.append(t_ins)
    b_y_del.append(t_del)
    b_y_sea.append(t_sea)

d_file = open("avl_simple.txt", "r")
lines = d_file.readlines()
length = len(lines)
avl_x = []
avl_y_ins = []
avl_y_del = []
avl_y_sea = []

for i in range(0, length, 6):
    avl_x.append(int(lines[i]))
    t_ins = 0.0
    t_del = 0.0
    t_sea = 0.0
    for j in range(i+1, i+6):
        d_line = lines[j].strip().split()
        t_ins += float(d_line[0])
        t_sea += float(d_line[1])
        t_del += float(d_line[2])
    t_ins /= 5
    t_del /= 5
    t_sea /= 5
    avl_y_ins.append(t_ins)
    avl_y_del.append(t_del)
    avl_y_sea.append(t_sea)

plt.figure(figsize=(6, 4), dpi=300)
plt.plot(avl_x, avl_y_del, label='AVLTree', linewidth=2, marker='x',
         markerfacecolor='black', markersize=4)
plt.plot(avl_x, b_y_del, label='B-Tree', linewidth=2, marker='x',
         markerfacecolor='black', markersize=4)
plt.plot(avl_x, rb_y_del, label='Red-Black-Tree', linewidth=2, marker='x',
         markerfacecolor='black', markersize=4)
plt.xlabel('Dot Number')
plt.ylabel('Time')
plt.title('Delete Time Contrast')
plt.legend()
plt.savefig("delete_comparison.png", dpi=500)
plt.show()

