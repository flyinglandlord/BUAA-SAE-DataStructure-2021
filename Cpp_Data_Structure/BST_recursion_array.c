#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 10005
#define INF 2147483647

int val[MAXN], cnt[MAXN], size[MAXN];
int ch[MAXN][2];        //0是左孩子,1是右孩子
int tot = 0, root = 0;

void pushup(int id) {
    size[id] = size[ch[id][0]] + size[ch[id][1]] + cnt[id];
}

void rotate(int* id, int d) {           //d为0是左旋,1为右旋
    int temp = ch[*id][d^1];            //左旋找右儿子，右旋找左儿子
    ch[*id][d^1] = ch[temp][d];         //左旋id连接右儿子的左子树，右旋id连接左儿子的右子树
    ch[temp][d] = *id;                  //父亲变成儿子（辈分乱了qwq）
    *id = temp;                         //儿子转成父亲(qwq)
    pushup(ch[*id][d]), pushup(*id);
}

void addPoint(int value, int* id) {
    if(*id == 0) {
        (*id) = ++tot;
        val[tot] = value;
        cnt[tot] = 1;
        size[tot] = 1;
        return;
    }
    if(value < val[*id]) addPoint(value, &ch[*id][0]);
    else if(value == val[*id]) cnt[*id]++, size[*id]++;
    else addPoint(value, &ch[*id][1]);
    pushup(*id);
}

int getNext(int value, int id, int ans) {
    if(val[id] <= value) {
        if(!ch[id][1]) return ans;
        else getNext(value, ch[id][1], ans);
    } else {
        if(!ch[id][0]) return val[id];
        else getNext(value, ch[id][0], val[id]);
    }
}

int getPrev(int value, int id, int ans) {
    if(val[id] >= value) {
        if(!ch[id][0]) return ans;
        else getPrev(value, ch[id][0], ans);
    } else {
        if(!ch[id][1]) return val[id];
        else getPrev(value, ch[id][1], val[id]);
    }
}

int kth(int k, int id, int rk) {
    if(!id) return;
    if(rk + cnt[id] + size[ch[id][0]] >= k && rk + size[ch[id][0]] < k) return val[id];
    else if(rk + cnt[id] + size[ch[id][0]] < k) return kth(k, ch[id][1], rk + cnt[id] + size[ch[id][0]]);
    else return kth(k, ch[id][0], rk);
}

int getRank(int value, int id) {
    int ans = 0;
    while(id) {
        if(value < val[id]) id = ch[id][0];
        else if(value == val[id]) return ans + size[ch[id][0]] + 1;
        else ans += cnt[id] + size[ch[id][0]], id = ch[id][1];
    }
    return ans+1;
}

void delPoint(int value, int* id) {
    if(*id == 0) return;
    if(value == val[*id]) {
        if(cnt[*id] > 1) {
            cnt[*id]--;
            pushup(*id);
            return;
        }
        if(ch[*id][0] || ch[*id][1]) {
            if(ch[*id][1] || ch[*id][0]) {
                if(!ch[*id][1]) {
                    rotate(id, 1);
                    delPoint(value, &ch[*id][1]);
                } else {
                    rotate(id, 0);
                    delPoint(value, &ch[*id][0]);
                }
            }
            pushup(*id);
        }
        else *id = 0;
        return;
    }
    if(value < val[*id]) delPoint(value, &ch[*id][0]);
    else delPoint(value, &ch[*id][1]);
    pushup(*id);
}

int main() {
    int n;
    scanf("%d", &n);
    while(n--) {
        int op, x;
        scanf("%d%d", &op, &x);
        switch(op) {
        case 1:
            printf("%d\n", getRank(x, root));
            break;
        case 2:
            printf("%d\n", kth(x, root, 0));
            break;
        case 3:
            printf("%d\n", getPrev(x, root, -INF));
            break;
        case 4:
            printf("%d\n", getNext(x, root, INF));
            break;
        case 5:
            addPoint(x, &root);
            break;
        case 6:
            delPoint(x, &root);
            break;
        }
        //printf("%d %d %d %d\n", root, val[root], val[ch[root][0]], val[ch[root][1]]);
    }
    return 0;
}
