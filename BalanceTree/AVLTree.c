#include <stdio.h>
#include <stdlib.h>

#define INF 2147483647

//#define LOCAL_TEST
#define MORE_FEATURE

struct node {
    struct node *lson;
    struct node *rson;
    int val;
    int cnt;
    int size;
    int height;
};

struct node *root;

int _max(int a, int b) {return a>b?a:b;}
int size(struct node *o) {return o==NULL?0:o->size;}
int cnt(struct node *o) {return o==NULL?0:o->cnt;}
int height(struct node *o) {return o==NULL?0:o->height;}
void pushup(struct node **o) {
    (*o)->height = _max(height((*o)->lson), height((*o)->rson)) + 1;
    (*o)->size = cnt(*o) + size((*o)->lson) + size((*o)->rson);
}

void lrotate(struct node **o) {
    struct node *tmp = (*o)->rson;
    (*o)->rson = tmp->lson;
    tmp->lson = (*o);
    pushup(o); pushup(&tmp);
    (*o) = tmp;
}
void rrotate(struct node **o) {
    struct node *tmp = (*o)->lson;
    (*o)->lson = tmp->rson;
    tmp->rson = (*o);
    pushup(o); pushup(&tmp);
    (*o) = tmp;
}

void LL(struct node **o) {rrotate(o);}
void LR(struct node **o) {lrotate(&((*o)->lson)); rrotate(o);}
void RL(struct node **o) {rrotate(&((*o)->rson)); lrotate(o);}
void RR(struct node **o) {lrotate(o);}

struct node *avltree_insert(struct node *o, int key) {
    if(o == NULL) {
        o = (struct node *)malloc(sizeof(struct node));
        o->lson = o->rson = NULL;
        o->height = o->size = o->cnt = 1;
        o->val = key;
        return o;
    }
    if(key == o->val) {
        o->cnt++;
        pushup(&o);
        return o;
    } else if(key < o->val) {
        o->lson = avltree_insert(o->lson, key);
        if(height(o->lson) - height(o->rson) == 2) {
            if(key <= o->lson->val) LL(&o);
            else LR(&o);
        }
        pushup(&o);
        return o;
    } else {
        o->rson = avltree_insert(o->rson, key);
        if(height(o->rson) - height(o->lson) == 2) {
            if(key >= o->rson->val) RR(&o);
            else RL(&o);
        }
        pushup(&o);
        return o;
    }
}

struct node *avltree_delete(struct node *o, int key) {
    if(o == NULL) return NULL;
    if(key < o->val) {
        o->lson = avltree_delete(o->lson, key);
        if(height(o->rson) - height(o->lson) == 2) {
            if(height(o->rson->rson) >= height(o->rson->lson)) RR(&o);
            else RL(&o);
        }
        pushup(&o);
        return o;
    } else if(key > o->val) {
        o->rson = avltree_delete(o->rson, key);
        if(height(o->lson) - height(o->rson) == 2) {
            if(height(o->lson->lson) >= height(o->lson->rson)) LL(&o);
            else LR(&o);
        }
        pushup(&o);
        return o;
    } else if(key == o->val) {
        if(o->cnt > 1) {
            o->cnt--;
            pushup(&o);
            return o;
        }
        if(o->lson && o->rson) {
            if(height(o->lson) >= height(o->rson)) {
                struct node *p = o->lson;
                while(p->rson) p = p->rson;
                o->val = p->val; o->cnt = p->cnt;
                p->cnt = 1;
                o->lson = avltree_delete(o->lson, p->val);
                pushup(&o);
                return o;
            } else {
                struct node *p = o->rson;
                while(p->lson) p = p->lson;
                o->val = p->val; o->cnt = p->cnt;
                p->cnt = 1;
                o->rson = avltree_delete(o->rson, p->val);
                pushup(&o);
                return o;                
            }
        } else {
            struct node *tmp = o;
            if(o->lson) o = o->lson;
            else if(o->rson) o = o->rson;
            else o = NULL;
            free(tmp);
            return o;
        }
    }
    return NULL;
}

struct node *avltree_search(struct node *o, int key) {
    if(o == NULL) return NULL;
    if(o->val == key) return o;
    else if(key < o->val) return avltree_search(o->lson, key);
    else return avltree_search(o->rson, key);
}

#ifdef MORE_FEATURE

    int _searchNext(int key, struct node *o, int ans) {
        if(o->val <= key) {
            if(o->rson == NULL) return ans;
            else return _searchNext(key, o->rson, ans);
        } else {
            if(o->lson == NULL) return o->val;
            else return _searchNext(key, o->lson, o->val);
        }
    }

    int _searchPrev(int key, struct node *o, int ans) {
        if(o->val >= key) {
            if(o->lson == NULL) return ans;
            else return _searchPrev(key, o->lson, ans);
        } else {
            if(o->rson == NULL) return o->val;
            else return _searchPrev(key, o->rson, o->val);
        }
    }

    int _kth(int k, struct node *o, int rk) {
        if(!o) return -1;
        if(rk + size(o->lson) + cnt(o) >= k && rk + size(o->lson) < k) return o->val;
        else if(rk + size(o->lson) + cnt(o) < k) return _kth(k, o->rson, rk + size(o->lson) + cnt(o));
        else return _kth(k, o->lson, rk);
    }

    int _rank(int key, struct node *o) {
        struct node *i = o;
        int rk = 0;
        while(1) {
            if(!i) return rk + 1;
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

    void _PreOrderTravel(struct node *o) {
        if(!o) return;
        printf("%d ", o->val);
        _PreOrderTravel(o->lson);
        _PreOrderTravel(o->rson);
    }



int main() {
    int n;
    scanf("%d", &n);
    while(n--) {
        int op, x;
        struct node *q;
        scanf("%d%d", &op, &x);
        switch(op) {
            case 0:
                q = _search(root, x);
                if(!q) printf("Not Found!\n");
                else printf("%d%d%d%d\n", q->cnt, q->val, q->size, q->height);
                break;
            case 1:
                root = _Insert(root, x);
                break;
            case 2:
                root = _Delete(root, x);
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