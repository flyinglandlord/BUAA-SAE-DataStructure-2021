#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#define LOCAL_TEST

int KEY_MAX;
int KEY_MIN;
int MID;

typedef struct Node{
    int size;
    int *key;
    struct Node **child;
    struct Node *parent; 
} Node;
Node *newNode() {
    Node *node = NULL;
    node = (Node *)calloc(1, sizeof(Node));
    if(node == NULL) return NULL;
    node->size = 0;
    node->key = (int *)calloc((KEY_MAX + 1), sizeof(int));
    if(node->key == NULL) return NULL;
    node->child = (Node **)calloc((KEY_MAX + 2), sizeof(Node *));
    if(node->child == NULL) return NULL;
    return node;
}
Node *root;

Node *search(Node *o, int x);
void init(int M);
void _split(Node *o);
void _merge(Node *o);
void do_merge(Node *l, Node *r, int id);
void insert(int key);
void btree_delete(int key);
void _delete(Node *o, int id);

void init(int M) {
    KEY_MAX = M-1;
    KEY_MIN = (M%2) ? M/2+1 : M/2;
    MID = M/2;
    root = NULL;
}

void _split(Node *o) {
    Node *parent = NULL, *new_left = NULL;
    while(o->size > KEY_MAX) {
        int len = o->size;
        new_left = newNode();
        if(!new_left) return;
        memcpy(new_left->key, o->key + MID + 1, (len-MID-1) * sizeof(int));
        memcpy(new_left->child, o->child + MID + 1, (len-MID) * sizeof(Node *));
        new_left->size = (len-MID-1);
        o->size = MID;
        new_left->parent = o->parent;

        parent = o->parent;
        if(!parent){
            parent = newNode();
            if(!parent) return;
            root = parent;
            parent->child[0] = o;
            parent->child[1] = new_left;
            o->parent = parent;
            new_left->parent = parent;
            parent->key[0] = o->key[MID];
            parent->size = 1;
        } else {
            int i;
            for(i = parent->size; i > 0; i--) {
                if(o->key[MID] < parent->key[i-1]) {
                    parent->key[i] = parent->key[i-1];
                    parent->child[i+1] = parent->child[i];
                } else break;
            }
            parent->key[i] = o->key[MID];
            parent->child[i+1] = new_left;
            new_left->parent = parent;
            parent->size++;
        }
        memset(o->key + MID, 0, (len - MID) * sizeof(int));
        memset(o->child + MID + 1, 0, (len - MID) * sizeof(Node *));
        for(int i = 0; i <= new_left->size; i++) if(new_left->child[i]) new_left->child[i]->parent = new_left;
        o = parent;
    }
}

void btree_insert(int key) {
    if(root == NULL) {
        Node *node = newNode();
        if(!node) return;
        node->size = 1;
        node->key[0] = key;
        node->parent = NULL;
        root = node;
        return;
    }
    Node *o = root;
    int i;
    while(o) {
        for(i = 0; i < o->size; i++) {
            if(key == o->key[i]) {
                //printf("Element Existed...\n");
                return;
            } else if(key < o->key[i]) break;
        }
        //printf("%d\n", i);
        if(o->child[i]) o = o->child[i];
        else break;
    }
    for(int j = o->size; j > i; j--) o->key[j] = o->key[j-1];
    o->key[i] = key;
    o->size++;
    if(o->size > KEY_MAX) _split(o);
}

// 将l和r指向的两个节点合并，同时mid是父亲父亲节点中的编号
void do_merge(Node *l, Node *r, int mid) {
    Node *parent = l->parent;
    l->key[l->size++] = parent->key[mid];
    memcpy(l->key + l->size, r->key, r->size * sizeof(int));
    memcpy(l->child + l->size, r->child, (r->size+1) * sizeof(Node *));
    
    int i;
    for(i=0; i <= r->size; i++) if(r->child[i]) r->child[i]->parent = l;
    l->size += r->size;

    for(i=mid; i<parent->size-1; i++) {
        parent->key[i] = parent->key[i+1];
        parent->child[i+1] = parent->child[i+2];
    }

    parent->key[i] = 0;
    parent->child[i+1] = NULL;
    parent->size--; 
    free((void *)r->key);
    free((void *)r->child);
    free(r);

    if(parent->size < KEY_MIN) _merge(parent);
}

void _merge(Node *o) {
    int id, mid;
    Node *parent = o->parent;
    Node *right_bro = NULL, *left_bro = NULL;

    // 如果是根节点，则直接处理
    if(!parent) {
        if(o->size == 0) {
            if(o->child[0]) {
                root = o->child[0];
                o->child[0]->parent = NULL;
            } else root = NULL;
            free((void *)o->key);
            free((void *)o->child);
            free(o);
        }
        return;
    }

    // 找到需要合并的节点在数组中的编号
    for(id = 0; id <= parent->size; id++) if(parent->child[id] == o) break;
    if(id > parent->size) {
        //printf("Element Not Found!\n");
        return;
    }

    // 如果是最右边的节点，就和左边的合并（把右侧节点o合并到左侧left_bro）
    if(id == parent->size) {
        mid = id-1;
        left_bro = parent->child[mid];
        
        // 如果可以合并就合并
        if(o->size + left_bro->size + 1 <= KEY_MAX) {
            return do_merge(left_bro, o, mid);
        }

        // 否则就不合并
        if(left_bro->size == 1) return;

        // 把左边的最大的那个元素拿出来当作根，根节点跟右侧合并
        for(int i = o->size; i > 0; i--) {
            o->key[i] = o->key[i-1];
            o->child[i+1] = o->child[i];
        }
        o->child[1] = o->child[0];

        o->key[0] = parent->key[mid];
        o->size++;
        o->child[0] = left_bro->child[left_bro->size];
        if(left_bro->child[left_bro->size]){
            left_bro->child[left_bro->size]->parent = o;
        }

        parent->key[mid] = left_bro->key[left_bro->size - 1];
        left_bro->key[left_bro->size - 1] = 0;
        left_bro->child[left_bro->size] = NULL;
        left_bro->size--;
        return;
    }

    // 否则就和右边的节点合并（把右侧right_bro合并到左侧o），下面同理
    mid = id;
    right_bro = parent->child[mid+1];
    if(o->size + right_bro->size + 1 <= KEY_MAX) {
        return do_merge(o, right_bro, mid);
    }

    if(right_bro->size == 1) return;

    o->size++;
    o->key[o->size-1] = parent->key[mid];
    o->child[o->size] = right_bro->child[0];
    if(right_bro->child[0]) {
        right_bro->child[0]->parent = o;
    }

    parent->key[mid] = right_bro->key[0];
    for(int i = 0; i < right_bro->size; i++) {
        right_bro->key[i] = right_bro->key[i+1];
        right_bro->child[i] = right_bro->child[i+1];
    }
    right_bro->child[right_bro->size] = NULL;
    right_bro->size--;
}

void _delete(Node *node, int id) {
    Node *o = node;
    Node *child = o->child[id];
    while(child) {
        node = child;
        child = node->child[child->size];
    }
    if(o != node) o->key[id] = node->key[node->size - 1];
    else for(int j = id; j < o->size; j++) o->key[j] = o->key[j+1];
    node->key[node->size-1] = 0;
    node->size--;

    if(node->size < KEY_MIN) _merge(node);
    
}

void btree_delete(int key) {
    Node *o = root;
    int i;
    while(o) {
        for(i=0; i<o->size; i++) {
            if(key == o->key[i]) {
                _delete(o, i);
                return;
            }
            else if(key < o->key[i]) break;
        }
        o = o->child[i];
    }
    //printf("Element Not Found!\n");
    return;
}

Node *btree_search(Node *o, int x) {
    if(!o) return NULL;
    if(x < o->key[0]) return btree_search(o->child[0], x);
    for(int i = 0; i < o->size; i++) {
        if(o->key[i] == x) return o;
        else if(o->key[i+1] > x) return btree_search(o->child[i+1], x);
    }
    return btree_search(o->child[o->size], x);
}

#ifdef LOCAL_TEST

    void _PreOrderTravel(Node *o) {
        if(o == NULL) return;
        printf("(");
        printf("%d", o->key[0]);
        for(int i = 1; i < o->size; i++) printf(",%d", o->key[i]);
        printf(")");
        for(int i = 0; i <= o->size; i++) _PreOrderTravel(o->child[i]);
    }



int main() {
    init(3);
    int n;
    scanf("%d", &n);
    while(n--) {
        int op, x;
        Node *q;
        scanf("%d%d", &op, &x);
        switch(op) {
            case 0:
                q = search(root, x);
                if(!q) printf("Not Found!\n");
                else {
                    for(int i = 0; i < q->size; i++) if(x == q->key[i]) {
                        printf("%d:%d\n", q->size, i);
                        break;
                    }
                }
                break;
            case 1:
                insert(x);
                break;
            case 2:
                delete(x);
                break;
        }

#ifdef LOCAL_TEST

        _PreOrderTravel(root);
        printf("\n");

#endif
        
    }
}

#endif