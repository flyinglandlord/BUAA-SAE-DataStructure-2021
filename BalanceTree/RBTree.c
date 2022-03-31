#include <stdio.h>
#include <stdlib.h>

#define INF 2147483647
#define Red 0
#define Black 1

//#define LOCAL_TEST
//#define MORE_FEATURE

typedef struct Node {
    struct Node *lson;
    struct Node *rson;
    struct Node *parent;
    int val;
    int cnt;
    int size;
    int color;      // 1 - Black    0 - Red
}Node;

Node *root;
Node *NIL;

Node *get_grandparent(Node *o) {return o->parent->parent;}
Node *get_parent(Node *o) {return o->parent;}
Node *get_uncle(Node *o) {
    if(o->parent == NIL || get_grandparent(o) == NIL) return NIL;
    if(o->parent == get_grandparent(o)->lson) return get_grandparent(o)->rson;
    else if(o->parent == get_grandparent(o)->rson) return get_grandparent(o)->lson;
    return NIL;
}
void set_black(Node *o) {if(o) o->color = Black;}
void set_red(Node *o) {if(o) o->color = Red;}

int _max(int a, int b) {return a>b?a:b;}
int size(Node *o) {return o==NULL?0:o->size;}
int cnt(Node *o) {return o==NULL?0:o->cnt;}
void pushup(Node *o) {o->size = cnt(o) + size(o->lson) + size(o->rson);}

void init() {
    NIL = (Node *)calloc(1, sizeof(Node));
    NIL->lson = NIL->rson = NIL->parent = NULL;
    NIL->size = NIL->cnt = 0;
    NIL->color = Black;
    root = NIL;
    //root->parent = NIL;
}

// 红黑树的旋转与AVL树的不同指出在于，旋转的节点没有变，指针仍然指向原来的位置
// 例如本来指针指向的是父亲，旋转之后变成了儿子，指针仍然是指向原来的父亲，现在的儿子，即不需要修改形参的值
void lrotate(Node *o) {
    Node *tmp = o->rson; 
    o->rson = tmp->lson; 
    if(tmp->lson != NIL) tmp->lson->parent = o;
    tmp->parent = o->parent;
    if(o->parent == NIL) root = tmp;
    else {
        if(o->parent->lson == o) o->parent->lson = tmp;
        else o->parent->rson = tmp;
    }
    tmp->lson = o;
    o->parent = tmp;
    pushup(o); pushup(tmp);
}
void rrotate(Node *o) {
    Node *tmp = o->lson;
    o->lson = tmp->rson;
    if(tmp->rson != NIL) tmp->rson->parent = o;
    tmp->parent = o->parent;
    if(o->parent == NIL) root = tmp;
    else {
        if(o->parent->lson == o) o->parent->lson = tmp;
        else o->parent->rson = tmp;
    }
    tmp->rson = o;
    o->parent = tmp;
    pushup(o); pushup(tmp);
}

void insert_fixup(Node *o) {
    Node *i = o;
    Node *f = get_parent(i);
    Node *g = get_grandparent(i);
    while(f->color == Red) {
        Node *u = get_uncle(i);
        if(f == g->lson) {
            // 情况1：叔叔节点也是红色
            // 解决方法：叔叔和父亲设为黑色，祖父设为红色，继续从祖父向上修正
            if(u->color == Red) {
                set_black(u);
                set_black(f);
                set_red(g);
                i = g;

                f = get_parent(i);
                g = get_grandparent(i);
                continue;
            }

            // 情况2：叔叔节点也是黑色， 当前节点是右孩子
            // 解决方法：左旋一次，转化为情况3
            if(f->rson == i) {
                lrotate(f);
                Node *tmp = f;
                f = i;
                i = tmp;
            }

            // 情况3：叔叔节点也是黑色， 当前节点是左孩子
            // 解决方法：父亲设为黑色，祖父设为红色，右旋一次
            set_black(f);
            set_red(g);
            rrotate(g); 
        } else {    //对称的再来一遍
            // 情况1：叔叔节点也是红色
            // 解决方法：叔叔和父亲设为黑色，祖父设为红色，继续从祖父向上修正
            if(u->color == Red) {
                set_black(u);
                set_black(f);
                set_red(g);
                i = g;

                f = get_parent(i);
                g = get_grandparent(i);
                continue;
            }

            // 情况2：叔叔节点也是黑色/叔叔节点不存在， 当前节点是左孩子
            // 解决方法：左旋一次，转化为情况3
            if(f->lson == i) {
                rrotate(f);
                Node *tmp = f;
                f = i;
                i = tmp;
            }

            // 情况3：叔叔节点也是黑色/叔叔节点不存在， 当前节点是右孩子
            // 解决方法：父亲设为黑色，祖父设为红色，右旋一次
            set_black(f);
            set_red(g);
            //printf("%d %d\n", grandparent->val, grandparent->color);
            lrotate(g);
            //printf("%d\n", root->val);
        }
        f = get_parent(i);
        g = get_grandparent(i);
    }
    set_black(root);
}

void rbtree_insert(Node *o, int key) {
    Node *i = o;
    Node *f = NIL;
    while (i != NIL) {
        f = i;
        i->size += 1;
        if (i->val == key) {
            i->cnt += 1;
            return;
        }
        else if(key < i->val) i = i->lson;
        else i = i->rson;
    }
    i = (Node *)malloc(sizeof(Node));
    i->parent = f; i->val = key;
    i->lson = i->rson = NIL; i->size = i->cnt = 1;
    i->color = Red;
    if(f != NIL) {
        if(i->val < f->val) f->lson = i;
        else f->rson = i;
    } else {
        root = i;
    }
    insert_fixup(i);
}

Node *rbtree_search(Node *o, int key) {
    if(o == NIL) return NULL;
    if(o->val == key) {return o;}
    Node *ans;
    if(key < o->val) ans = rbtree_search(o->lson, key);
    else ans = rbtree_search(o->rson, key);
    return ans;
}

void delete_fixup(Node *o, Node *f) {
    Node *other;

    while((o->color == Black) && o != root) {
        if(f->lson == o) {
            other = f->rson;

            // 情况1：黑+黑 & 兄弟为红色
            // 解决方法：染色+左旋，转化成情况2
            if(other->color == Red) {
                other->color = Black;
                f->color = Red;
                lrotate(f);
                other = f->rson;
            }

            // 情况2：黑+黑 & 兄弟为黑色，兄弟的两个孩子也是黑色
            // 解决方法：染色，当前节点变成父亲节点，继续循环
            if((other->lson->color == Black) && (other->rson->color == Black)) {
                other->color = Red;
                o = f;

                f = get_parent(o);
                continue;
            }

            // 情况3：黑+黑 & 兄弟为黑色，兄弟的右孩子为红，左孩子为黑
            // 解决方法：染色+左旋，转化成情况4
            if(other->rson->color == Black) {
                other->lson->color = Black;
                other->color = Red;
                rrotate(other);
                other = f->rson;
            }

            // 情况4：黑+黑 & 兄弟为黑色，兄弟的右孩子为红色
            // 解决方法：兄弟染成父亲的颜色，父亲染成黑色，左旋，调整完毕
            other->color = f->color;
            f->color = Black;
            other->rson->color = Black;
            lrotate(f);
            o = root;
            break;
        } else {    //对称地再来一遍
            other = f->lson;

            // 情况1：黑+黑 & 兄弟为红色
            // 解决方法：染色+右旋，转化成情况2
            if(other->color == Red) {
                other->color = Black;
                f->color = Red;
                rrotate(f);
                other = f->lson;
            }

            // 情况2：黑+黑 & 兄弟为黑色，兄弟的两个孩子也是黑色
            // 解决方法：染色，当前节点变成父亲节点，继续循环
            if((other->lson->color == Black) && (other->rson->color == Black)) {
                other->color = Red;
                o = f;

                f = get_parent(o);
                continue;
            }

            // 情况3：黑+黑 & 兄弟为黑色，兄弟的左孩子为红，右孩子为黑
            // 解决方法：染色+右旋，转化成情况4
            if(other->lson->color == Black) {
                other->rson->color = Black;
                other->color = Red;
                lrotate(other);
                other = f->lson;
            }

            // 情况4：黑+黑 & 兄弟为黑色，兄弟的右孩子为红色
            // 解决方法：兄弟染成父亲的颜色，父亲染成黑色，右旋，调整完毕
            other->color = f->color;
            f->color = Black;
            other->lson->color = Black;
            rrotate(f);
            o = root;
            break;
        }
    }

    // 处理的最后根节点一定是黑+红，即情况0
    // 解决方法：直接染成黑色即可
    if(o != NIL) o->color = Black;
}

void rbtree_delete(Node *o, int key) {
    if(o == NIL || o == NULL) return;
    Node *ch, *f;
    Node *i = o;
    int color;

    while(i != NIL) {
        f = i;
        i->size--;
        if(i->val == key) break;
        if(key < i->val) i = i->lson;
        else i = i->rson;
    }
    
    if(i == NIL) {
        while(f != NIL && f != NULL) f->size++, f = f->parent;
        return;
    }
    if(i->cnt > 1) {
        i->cnt--;
        return;
    }

    if(i->lson != NIL && i->rson != NIL) {
        Node *min = i->rson;
        while(min->lson != NIL) min = min->lson;

        f = get_parent(i);
        if(f != NIL) {
            if(f->lson == i) f->lson = min;
            else f->rson = min;
        } else root = min;

        f = get_parent(min);
        ch = min->rson;
        color = min->color;

        if(f == i) f = min;
        else {
            Node *tmp = min;
            while(tmp != i) {
                tmp->size -= min->cnt;
                tmp = tmp->parent;
            }

            if(ch != NIL) ch->parent = f;
            f->lson = ch;

            min->rson = i->rson;
            i->rson->parent = min;
        }

        min->parent = i->parent;
        min->lson = i->lson;
        i->lson->parent = min;
        min->color = i->color;
        pushup(min);

        if(color == Black) delete_fixup(ch, f);
        free(i);
        return;
    }

    if(i->lson != NIL) ch = i->lson;
    else ch = i->rson;

    f = get_parent(i);
    color = i->color;

    if(ch != NIL) ch->parent = f;

    if(f != NIL) {
        if(f->lson == i) f->lson = ch;
        else f->rson = ch;
    } else root = ch;

    if(color == Black) delete_fixup(ch, f);
    free(i);
}

#ifdef MORE_FEATURE

    int _searchNext(int key, Node *o, int ans) {
        if(o->val <= key) {
            if(o->rson == NIL) return ans;
            else return _searchNext(key, o->rson, ans);
        } else {
            if(o->lson == NIL) return o->val;
            else return _searchNext(key, o->lson, o->val);
        }
    }

    int _searchPrev(int key, Node *o, int ans) {
        if(o->val >= key) {
            if(o->lson == NIL) return ans;
            else return _searchPrev(key, o->lson, ans);
        } else {
            if(o->rson == NIL) return o->val;
            else return _searchPrev(key, o->rson, o->val);
        }
    }

    int _kth(int k, Node *o, int rk) {
        if(o == NIL) return -1;
        if(rk + size(o->lson) + cnt(o) >= k && rk + size(o->lson) < k) return o->val;
        else if(rk + size(o->lson) + cnt(o) < k) return _kth(k, o->rson, rk + size(o->lson) + cnt(o));
        else return _kth(k, o->lson, rk);
    }

    int _rank(int key, Node *o) {
        Node *i = o;
        int rk = 0;
        while(1) {
            if(i == NIL) return rk + 1;
            if(i->val == key) return rk + size(i->lson) + 1;
            else if(i->val < key) {
                rk += size(i->lson) + cnt(i);
                i = i->rson;
            } else {
                i = i->lson;
            }
        }
    }

#endif

#ifdef LOCAL_TEST

    void _PreOrderTravel(Node *o) {
        if(o == NIL) return;
        printf("(%d,%d,%d,%s)\n", o->val, o->size, o->cnt, o->color == 1 ? "Black" : "Red");
        _PreOrderTravel(o->lson);
        _PreOrderTravel(o->rson);
    }

int main() {

    NIL = (Node *)calloc(1, sizeof(Node));
    NIL->lson = NIL->rson = NIL->parent = NULL;
    NIL->size = NIL->cnt = 0;
    NIL->color = Black;
    root = NIL;

    int n;
    scanf("%d", &n);
    while(n--) {
        int op, x;
        Node *q;
        scanf("%d%d", &op, &x);
        switch(op) {
            case 0:
                q = rbtree_search(root, x);
                if(!q) printf("Not Found!\n");
                else printf("(%d,%d,%d,%s)\n", q->val, q->size, q->cnt, q->color == 1 ? "Black" : "Red");
                break;
            case 1:
                rbtree_insert(root, x);
                break;
            case 2:
                rbtree_delete(root, x);
                break;

#ifdef MORE_FEATURE

            case 3:
                printf("%d\n", _rank(x, root));
                break;
            case 4:
                printf("%d\n", _kth(x, root, 0));
                break;
            case 5:
                printf("%d\n", _searchPrev(x, root, -INF));
                break;
            case 6:
                printf("%d\n", _searchNext(x, root, INF));
                break;
#endif
        }

#ifdef LOCAL_TEST

        _PreOrderTravel(root);
        printf("\n");

#endif
        
    }
}

#endif