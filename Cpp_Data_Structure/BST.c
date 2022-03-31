#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAXN 100005
#define INF 2147483647
#define true 1
#define false 0
#define int long long

struct Node {
    int val;
    int cnt;
    struct Node *lson, *rson;
    int size;
};

struct Node *newTree() {
    struct Node *root = NULL;
    return root;
}

struct Node *addPoint(int val, struct Node **root) {
    struct Node *newpoint = (struct Node *)malloc(sizeof(struct Node));
    newpoint->val = val;
    newpoint->lson = newpoint->rson = NULL;
    newpoint->size = 1;
    newpoint->cnt = 1;
    if (*root == NULL) {
        *root = newpoint;
        return *root;
    }
    struct Node *iter = *root, *father = NULL;
    while (iter != NULL) {
        iter->size ++;
        if (iter->val == val) {
            iter->cnt ++;
            return iter;
        }
        father = iter;
        if (iter->val < val) iter = iter->rson;
        else iter = iter->lson;
    }
    if (father->val < val) father->rson = newpoint;
    else father->lson = newpoint;
    return newpoint;
}

struct Node *searchPoint(int val, struct Node *root) {
    struct Node *iter = root;
    while(iter != NULL) {
        if (iter->val == val) return iter;
        else if (iter->val < val) iter = iter->rson;
        else iter = iter->lson;
    }
    return INF;
}

int searchNext(int val, struct Node *root) {
    struct Node *iter = root;
    int ans = INF;
    while(true) {
        if(iter->val <= val) {
            if(iter->rson == NULL) return ans;
            else iter = iter->rson;
        } else {
            if(iter->lson == NULL) return iter->val;
            ans = iter->val;
            iter = iter->lson;
        }
    }
}

int searchPrev(int val, struct Node *root) {
    struct Node *iter = root;
    int ans = -INF;
    while(true) {
        if(iter->val >= val) {
            if(iter->lson != NULL) iter = iter->lson;
            else return ans;
        } else {
            if(iter->rson == NULL) return iter->val;
            ans = iter->val;
            iter = iter->rson;
        }
    }
}

struct Node *kth(int k, struct Node *root) {
    struct Node *iter = root;
    int step = 0;
    while(true) {
        if(iter == NULL) return INF;
        if(step + (iter->lson == NULL ? 0 : iter->lson->size) >= k) iter = iter->lson;
        else if(step + (iter->lson == NULL ? 0 : iter->lson->size) + iter->cnt >= k) return iter;
        else {step += (iter->lson == NULL ? 0 : iter->lson->size) + iter->cnt, iter = iter->rson;}
    }
}

int rank(int val, struct Node *root) {
    struct Node *iter = root;
    int rk = 0;
    while(true) {
        if(iter == NULL) return rk + 1;
        if(iter->val == val) return rk + (iter->lson == NULL ? 0 : iter->lson->size) + 1;
        else if(iter->val < val) {
            rk += (iter->lson == NULL ? 0 : iter->lson->size) + iter->cnt;
            iter = iter->rson;
        } else {
            iter = iter->lson;
        }
    }
}

int main() {
    struct Node *root = newTree();
    int n;
    scanf("%lld", &n);
    while(n--) {
        int op, x;
        scanf("%lld%lld", &op, &x);
        switch(op) {
        case 1:
            printf("%lld\n", rank(x, root));
            break;
        case 2:
            printf("%lld\n", kth(x, root)->val);
            break;
        case 3:
            printf("%lld\n", searchPrev(x, root));
            break;
        case 4:
            printf("%lld\n", searchNext(x, root));
            break;
        case 5:
            addPoint(x, &root);
            break;
        }
    }
    return 0;
}
/*
13
5 44
5 17
5 8
5 32
5 29
5 88
5 65
5 97
5 54
5 82
5 76
5 93
3 44
*/
