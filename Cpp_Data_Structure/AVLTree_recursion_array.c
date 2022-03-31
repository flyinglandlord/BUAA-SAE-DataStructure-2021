#include <stdio.h>
#include <stdlib.h>
#define INF 2147483647
#define MAXN 100005
#define true 1
#define false 0

int ch[MAXN][2];
int size[MAXN], cnt[MAXN], height[MAXN];
int val[MAXN];
int tot, root=0;

int max(int a, int b) {return a>b?a:b;}
void pushup(int id) {
    size[id] = size[ch[id][0]] + size[ch[id][1]] + cnt[id];
    height[id] = max(height[ch[id][0]], height[ch[id][1]]) + 1;
}
void rotate(int* id, int d) {
    int temp = ch[*id][d^1];
    ch[*id][d^1] = ch[temp][d];
    ch[temp][d] = *id;
    pushup(*id); pushup(temp);
    *id = temp;
}
void LL(int *id) {rotate(id, 1);}
void RR(int *id) {rotate(id, 0);}
void LR(int *id) {rotate(&ch[*id][0], 0); rotate(id, 1);}
void RL(int *id) {rotate(&ch[*id][1], 1); rotate(id, 0);}

void addPoint(int value, int* id) {
    if(*id == 0) {
        *id = ++tot;
        size[*id] = cnt[*id] = 1;
        ch[*id][0] = ch[*id][1] = 0;
        height[*id] = 1;
        val[*id] = value;
        return;
    }
    if(value < val[*id]) {
        addPoint(value, &ch[*id][0]);
        pushup(*id);
        if(height[ch[*id][0]] - height[ch[*id][1]] == 2) {
            if(value < val[ch[*id][0]]) LL(id);
            else LR(id);
        }
    } else if(value > val[*id]) {
        addPoint(value, &ch[*id][1]);
        pushup(*id);
        if(height[ch[*id][1]] - height[ch[*id][0]] == 2) {
            if(value > val[ch[*id][1]]) RR(id);
            else RL(id);
        }
    } else {
        cnt[*id]++;
        pushup(*id);
        return;
    }
    pushup(*id);
}

void delPoint(int value, int* id) {
    if(*id == 0) return;
    if(value < val[*id]) {
        delPoint(value, &ch[*id][0]);
        pushup(*id);
        if(height[ch[*id][1]] - height[ch[*id][0]] == 2) {
            int p = ch[*id][1];
            if(height[ch[p][1]] >= height[ch[p][0]]) RR(id);
            else RL(id);
        }
        pushup(*id);
        return;
    } else if(value > val[*id]) {
        delPoint(value, &ch[*id][1]);
        pushup(*id);
        if(height[ch[*id][0]] - height[ch[*id][1]] == 2) {
            int p = ch[*id][0];
            if(height[ch[p][0]] >= height[ch[p][1]]) LL(id);
            else LR(id);
        }
        pushup(*id);
        return;
    } else {
        if(cnt[*id] > 1) {
            cnt[*id]--;
            pushup(*id);
            return;
        }
        if(ch[*id][0] && ch[*id][1]) {
            if(height[ch[*id][0]] >= height[ch[*id][1]]) {
                int p = ch[*id][0];
                while(ch[p][1] != 0) p = ch[p][1];
                val[*id] = val[p];
                cnt[*id] = cnt[p];
                cnt[p] = 1;
                delPoint(val[p], &ch[*id][0]);
                pushup(*id);
            } else {
                int p = ch[*id][1];
                while(ch[p][0] != 0) p = ch[p][0];
                val[*id] = val[p];
                cnt[*id] = cnt[p];
                cnt[p] = 1;
                delPoint(val[p], &ch[*id][1]);
                pushup(*id);
            }
        } else {
            size[*id] = cnt[*id] = val[*id] = 0;
            *id = (ch[*id][0] != 0) ? ch[*id][0] : ch[*id][1];
            /*pushup(*id);*/
            /*这里没有pushup, 在这里调了两个小时，Graveyard Here...*/
            /*考虑左右儿子均为空的情况，这时pushup会使得树的高度乱掉*/
            return;
        }
    }
}

int searchNext(int value, int id, int ans) {
    if(!id) return ans;
    if(value < val[id]) {
        if(!ch[id][0]) return val[id];
        else return searchNext(value, ch[id][0], val[id]);
    } else {
        if(!ch[id][1]) return ans;
        else return searchNext(value, ch[id][1], ans);
    }
}

int searchPrev(int value, int id, int ans) {
    if(!id) return ans;
    if(value > val[id]) {
        if(!ch[id][1]) return val[id];
        else return searchPrev(value, ch[id][1], val[id]);
    } else {
        if(!ch[id][0]) return ans;
        else return searchPrev(value, ch[id][0], ans);
    }
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
    if(!id) return 0;
    if(rk + size[ch[id][0]] >= k) return kth(k, ch[id][0], rk);
    else if(rk + size[ch[id][0]] + cnt[id] >= k) return val[id];
    else return kth(k, ch[id][1], rk + size[ch[id][0]] + cnt[id]);
}

int main() {
    int n;
    //int t = 0;
    //freopen("test.out", "w", stdout);
    scanf("%d", &n);
    while(n--) {
        int op, x;
        scanf("%d%d", &op, &x);
        switch(op) {
        case 1:
            addPoint(x, &root);
            break;
        case 2:
            delPoint(x, &root);
            break;
        case 3:
            printf("%d\n", getRank(x, root));
            break;
        case 4:
            //printf("-*-*-*%%%");
            printf("%d\n", kth(x, root, 0));
            break;
        case 5:
            printf("%d\n", searchPrev(x, root, -INF));
            break;
        case 6:
            printf("%d\n", searchNext(x, root, INF));
            break;
        }
        //printf("%d %d %d %d\n", root, val[root], val[ch[root][0]], val[ch[root][1]]);
    }
    return 0;
}

/*
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
*/
