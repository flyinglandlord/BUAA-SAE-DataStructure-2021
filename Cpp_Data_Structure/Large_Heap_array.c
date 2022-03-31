#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 100005
#define INF 2147483647
#define true 1
#define false 0
#define lson(x) (2*(x)+1)
#define rson(x) (2*(x)+2)
#define parent(x) (((x)-1)/2)

struct Pair {
    int k, v;
}data[MAXN];
int cnt;

void swap(struct Pair *a, struct Pair *b) {struct Pair temp = *a; *a = *b; *b = temp;}
void upHeap(int i) {
    if(i == 0) return;
    if(data[i].k > data[parent(i)].k) {
        swap(&data[i], &data[parent(i)]);
        upHeap(parent(i));
    }
}
void downHeap(int i) {
    int pos;
    if(lson(i) < cnt) {
        pos = lson(i);
        if(rson(i) < cnt) pos = (data[lson(i)].k > data[rson(i)].k) ? lson(i) : rson(i);
        if(data[pos].k > data[i].k) {
            swap(&data[pos], &data[i]);
            downHeap(pos);
        }
    }
}
void heapify() {
    for(int i = parent(cnt-1); i >= 0; i--) downHeap(i);
}
void addval(int k, int v) {
    data[cnt].k = k, data[cnt].v = v;
    cnt++;
    upHeap(cnt-1);
}
int max() {
    if(!cnt) return -1;
    return data[0].v;
}
int remove_max() {
    if(!cnt) return -1;
    int ans = data[0].v;
    data[0] = data[cnt-1];
    cnt--;
    downHeap(0);
    return ans;
}
void init(struct Pair *arr, int n) {
    for(int i = 0; i < n; i++) data[i].k = arr[i].k, data[i].v = arr[i].v;
    cnt = n+1;
    heapify();
}

int main() {
    for(int i = 1; i <= 10; i++) addval(i, i);
    for(int i = 1; i <= 11; i++) printf("%d\n", remove_max());
}
