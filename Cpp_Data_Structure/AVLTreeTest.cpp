#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int MAXN = 100005;

int ch[MAXN][2];
int siz[MAXN], val[MAXN], cnt[MAXN], hei[MAXN];
int rt = 0, tot = 0;

void pushup(int o) {
    siz[o] = siz[ch[o][0]] + siz[ch[o][1]] + cnt[o];
    hei[o] = max(hei[ch[o][0]], hei[ch[o][1]]) + 1;
}
void rotate(int& o, int d) {
    int tmp = ch[o][d^1];
    ch[o][d^1] = ch[tmp][d];
    ch[tmp][d] = o;
    pushup(o);
    pushup(o=tmp);
}
void RR(int& o) {rotate(o, 1);}
void RL(int& o) {rotate(ch[o][0], 0); rotate(o, 1);}
void LL(int& o) {rotate(o, 0);}
void LR(int& o) {rotate(ch[o][1], 0); rotate(o, 0);}
void add(int& o, int key) {
    if(!o) {
        o = ++tot;
        ch[o][0] = ch[o][1] = 0;
        siz[o] = cnt[o] = 1;
        val[o] = key;
        return;
    }
    if(key == val[o]) {
        cnt[o]++;
        pushup(o);
    } else if(key < val[o]) {
        add(ch[o][0], key);
        if(hei[ch[o][0]] - hei[ch[o][1]] == 2) {
            if(key < val[ch[o][0]]) RR(o);
            else if(key > val[ch[o][0]]) RL(o);
        }
        pushup(o);
    }
    else {
        add(ch[o][1], key);
        if(hei[ch[o][1]] - hei[ch[o][0]] == 2) {
            if(key > val[ch[o][1]]) RR(o);
            else if(key < val[ch[o][0]]) RL(o);
        }
        pushup(o);
    }
}
void del(int& o, int key) {
    if(!o) return;
    if(key < val[o]) {
        del(ch[o][0], key);
        if(hei[ch[o][1]] - hei[ch[o][0]] == 2) {
            if(key > val[ch[o][1]]) RR(o);
            else if(key < val[ch[o][0]]) RL(o);
        }
        pushup(o);
    } else if(key > val[o]) {
        del(ch[o][1], key);
        if(hei[ch[o][0]] - hei[ch[o][1]] == 2) {
            if(key < val[ch[o][0]]) RR(o);
            else if(key > val[ch[o][0]]) RL(o);
        }
        pushup(o);
    } else {
        if(cnt[o] > 1) {
            cnt[o]--;
            pushup(o);
            return;
        }
        if(ch[o][0] || ch[o][1]) {
            
        }
    }
}

int main() {

}