#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define INF 2147483647
#define true 1
#define false 0

struct Node {
    int val;
    int cnt;
    int size;
    int height;
    struct Node *lson, *rson;
};

struct Node *root;

int max(int a, int b) {return a>b?a:b;}
int size(struct Node *node) {return node==NULL?0:node->size;}
int height(struct Node *node) {return node==NULL?0:node->height;}
int cnt(struct Node *node) {return node==NULL?0:node->cnt;}
void pushup(struct Node **node) {
    (*node)->size = size((*node)->lson) + size((*node)->rson) + cnt((*node));
    (*node)->height = 1 + max(height((*node)->rson), height((*node)->lson));
}
void rotate(struct Node **node, int d) {         //d=0×óÐý, d=1ÓÒÐý
    if(d == 0) {
        struct Node *temp = (*node)->rson;
        (*node)->rson = temp->lson;
        temp->lson = (*node);
        pushup(node);pushup(&temp);
        (*node) = temp;
    } else if(d == 1) {
        struct Node *temp = (*node)->lson;
        (*node)->lson = temp->rson;
        temp->rson = (*node);
        pushup(node);pushup(&temp);
        (*node) = temp;
    }
    pushup(node);
}
void LL(struct Node **node) {rotate(node, 1);}
void RR(struct Node **node) {rotate(node, 0);}
void LR(struct Node **node) {rotate(&((*node)->lson), 0); rotate(node, 1);}
void RL(struct Node **node) {rotate(&((*node)->rson), 1); rotate(node, 0);}

void addPoint(int value, struct Node **node) {
    if(*node == NULL) {
        *node = (struct Node *)malloc(sizeof(struct Node));
        (*node)->lson = (*node)->rson = NULL;
        (*node)->val = value;
        (*node)->cnt = (*node)->size = 1;
        (*node)->height = 1;
        return;
    }
    if((*node)->val == value) {
        (*node)->cnt++;
        pushup(&(*node));
        return;
    }
    else if((*node)->val < value) {
        addPoint(value, &((*node)->rson));
        pushup(&(*node));
        if(height((*node)->rson) - height((*node)->lson) == 2) {
            if(value > (*node)->rson->val) RR(node);
            else RL(node);
        }
    }
    else {
        addPoint(value, &((*node)->lson));
        pushup(&(*node));
        if(height((*node)->lson) - height((*node)->rson) == 2) {
            if(value < (*node)->lson->val) LL(node);
            else LR(node);
        }
    }
    pushup(&(*node));
}

void delPoint(int value, struct Node **node) {
    if(*node == NULL) return;
    if((*node)->val < value) {
        delPoint(value, &((*node)->rson));
        pushup(&(*node));
        if(height((*node)->lson) - height((*node)->rson) == 2)
            if(height((*node)->lson->lson) >= height((*node)->lson->rson)) LL(node);
            else LR(node);
    } else if((*node)->val > value) {
        delPoint(value, &((*node)->lson));
        pushup(&(*node));
        if(height((*node)->rson) - height((*node)->lson) == 2)
            if(height((*node)->rson->lson) > height((*node)->rson->rson)) RL(node);
            else RR(node);
    } else {
        if((*node)->cnt > 1) {
            (*node)->cnt--;
            pushup(&(*node));
            return;
        }
        if((*node)->lson && (*node)->rson) {
            if(height((*node)->lson) > height((*node)->rson)) {
                struct Node *p = (*node)->lson;
                while(p->rson != NULL) p = p->rson;
                (*node)->cnt = p->cnt;
                (*node)->val = p->val;
                p->cnt = 1;
                delPoint(p->val, &((*node)->lson));
                pushup(&(*node));
                return;
            } else {
                struct Node *p = (*node)->rson;
                while(p->lson != NULL) p = p->lson;
                (*node)->cnt = p->cnt;
                (*node)->val = p->val;
                p->cnt = 1;
                delPoint(p->val, &((*node)->rson));
                pushup(&(*node));
                return;
            }
        } else {
            struct Node *p = *node;
            if((*node)->lson) *node = (*node)->lson;
            else if((*node)->rson) *node = (*node)->rson;
            else *node = NULL;
            free(p);
            return;
        }
    }
}

struct Node *searchPoint(int value, struct Node *node) {
    if(node->val == value) return node;
    else if(node->val < value) return searchPoint(value, node->rson);
    else return searchPoint(value, node->lson);
    return NULL;
}

int searchNext(int value, struct Node *node, int ans) {
    if(node->val <= value) {
        if(node->rson == NULL) return ans;
        else return searchNext(value, node->rson, ans);
    } else {
        if(node->lson == NULL) return node->val;
        else return searchNext(value, node->lson, node->val);
    }
}

int searchPrev(int value, struct Node *node, int ans) {
    if(node->val >= value) {
        if(node->lson == NULL) return ans;
        else return searchPrev(value, node->lson, ans);
    } else {
        if(node->rson == NULL) return node->val;
        else return searchPrev(value, node->rson, node->val);
    }
}

int kth(int k, struct Node *node, int rk) {
    if(!node) return NULL;
    if(rk + size(node->lson) + cnt(node) >= k && rk + size(node->lson) < k) return node->val;
    else if(rk + size(node->lson) + cnt(node) < k) return kth(k, node->rson, rk + size(node->lson) + cnt(node));
    else return kth(k, node->lson, rk);
}

int rank(int value, struct Node *node) {
    struct Node *iter = node;
    int rk = 0;
    while(true) {
        if(iter == NULL) return rk + 1;
        if(iter->val == value) return rk + size(iter->lson) + 1;
        else if(iter->val < value) {
            rk += size(iter->lson) + cnt(iter);
            iter = iter->rson;
        } else {
            iter = iter->lson;
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    while(n--) {
        int op, x;
        scanf("%d%d", &op, &x);
        switch(op) {
        case 3:
            printf("%d\n", rank(x, root));
            break;
        case 4:
            printf("%d\n", kth(x, root, 0));
            break;
        case 5:
            printf("%d\n", searchPrev(x, root, -INF));
            break;
        case 6:
            printf("%d\n", searchNext(x, root, INF));
            break;
        case 1:
            addPoint(x, &root);
            break;
        case 2:
            delPoint(x, &root);
            break;
        }
        //printf("%d %d %d\n", root->val, size(root->lson), size(root->rson));
    }
    return 0;
}

/*
1000
1 44
1 17
1 8
1 32
1 29
1 88
1 65
1 97
1 54
1 82
1 76
1 93
3 44
*/
