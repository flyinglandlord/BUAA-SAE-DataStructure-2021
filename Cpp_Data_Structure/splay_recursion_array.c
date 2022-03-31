#include <stdio.h>
#include <stdlib.h>
#define MAXN 100005
#define INF 2147483647
#define true 1
#define false 0
#define root ch[0][1]

int ch[MAXN][2];
int val[MAXN], size[MAXN], cnt[MAXN], fa[MAXN];
int tot=0;

void pushup(int id) {size[id] = size[ch[id][0]] + size[ch[id][1]] + cnt[id];}
int identify(int id) {       //左子树返回0，右子树返回1
    int f = fa[id]; return id == ch[f][0] ? 0 : 1;
}
void rotate(int id) {        //这里的旋转跟AVL树不同，是给出儿子节点，找父亲节点
    int f = fa[id], g =fa[fa[id]];
    int d = identify(id);
    ch[g][identify(f)] = id; fa[id] = g;
    ch[f][d] = ch[id][d^1]; fa[ch[id][d^1]] = f;
    ch[id][d^1] = f; fa[f] = id;
    pushup(f); pushup(id);
}
void splay(int id, int tar) {
    tar = fa[tar];
    while(fa[id] != tar) {
        if(fa[fa[id]] == tar) rotate(id);
        else if(identify(id) == identify(fa[id])) {
            rotate(fa[id]); rotate(id);
        } else {
            rotate(id); rotate(id);
        }
    }
}

void addPoint(int value) {
    if(!root) {
        root = ++tot;
        val[tot] = value;
        size[tot] = cnt[tot] = 1;
        ch[tot][0] = ch[tot][1] = 0;
        fa[tot] = 0;
        return;
    } else {
        int node = root;
        while(true) {
            size[node]++;
            if(value == val[node]) {
                cnt[node]++;
                splay(node, root);
                return;
            }
            int nxt = (value < val[node]) ? 0 : 1;
            if(!ch[node][nxt]) {
                //printf("$$$\n");
                ch[node][nxt] = ++tot;
                val[tot] = value;
                size[tot] = cnt[tot] = 1;
                ch[tot][0] = ch[tot][1] = 0;
                fa[tot] = node;
                splay(tot, root);
                return;
            }
            node = ch[node][nxt];
        }
    }
}

int searchPoint(int value) {
    int node = root;
    while(node) {
        if(value == val[node]) {
            splay(node, root);
            return node;
        }
        int nxt = (value < val[node]) ? 0 : 1;
        node = ch[node][nxt];
    }
    return 0;
}

void delPoint(int value) {
    int del = searchPoint(value);
    //printf("%d %d %d\n", root, val[ch[root][0]], val[ch[root][1]]);
    if(del) {
        if(cnt[del] > 1) {
            cnt[del]--;
            pushup(del);
            return;
        }
        if(!ch[del][0] && !ch[del][1]) {
            root = 0;
            return;
        } else if(!ch[del][0]) {
            root = ch[del][1];
            fa[root] = 0;
            fa[ch[del][1]] = 0;
        } else {
            int node = del;
            node = ch[node][0];
            while(ch[node][1]) node = ch[node][1];
            splay(node, ch[del][0]);
            //printf("%d %d %d\n", root, val[ch[root][0]], val[ch[root][1]]);
            fa[node] = 0;
            ch[node][1] = ch[del][1];
            fa[ch[del][1]] = node;
            root = node;
            pushup(node);
        }
    }
}

int rank(int value) {          //splay这个好写，直接把value旋转到根的位置，但是要求必须value在树中
    int pos = searchPoint(value);
    return size[ch[pos][0]] + 1;
}

int getRank(int value, int id) {
    int ans = 0;
    while(id) {
        if(id == 0) return ans+1;
        if(value < val[id]) id = ch[id][0];
        else if(value > val[id]) ans += size[ch[id][0]] + cnt[id], id = ch[id][1];
        else return ans + size[ch[id][0]] + 1;
    }
    return ans+1;
}

int kth(int k, int id, int rk) {
    if(rk + size[ch[id][0]] >= k) return kth(k, ch[id][0], rk);
    else if(rk + size[ch[id][0]] + cnt[id] >= k) return val[id];
    else return kth(k, ch[id][1], rk + size[ch[id][0]] + cnt[id]);
}

int searchPrev(int value, int id, int ans) {
    if(val[id] < value) {
        if(!ch[id][1]) return val[id];
        else return searchPrev(value, ch[id][1], val[id]);
    } else {
        if(!ch[id][0]) return ans;
        else return searchPrev(value, ch[id][0], ans);
    }
}

int searchNext(int value, int id, int ans) {
    if(val[id] > value) {
        if(!ch[id][0]) return val[id];
        else return searchNext(value, ch[id][0], val[id]);
    } else {
        if(!ch[id][1]) return ans;
        else return searchNext(value, ch[id][1], ans);
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
            printf("%d\n", rank(x));
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
            addPoint(x);
            break;
        case 2:
            delPoint(x);
            break;
        }
        //printf("%d %d %d\n", root, val[ch[root][0]], val[ch[root][1]]);
    }
    return 0;
}

