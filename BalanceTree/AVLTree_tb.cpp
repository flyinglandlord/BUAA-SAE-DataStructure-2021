#include "AVLTree.c"
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
#include <ctime>

using namespace std;

vector<int> generate_random_array(int n) {
    vector<int> arr;
    arr.clear();
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    for(int i = 1; i <= n; i++) arr.push_back(i);
    shuffle(arr.begin(), arr.end(), std::default_random_engine(seed));
    return arr;
}

const int data_mass[] = {1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000};
// Test Insert, Delete, Search Function in different data_mass
// Repeat 3 times for average
void SimpleFunctionTest() {
    FILE *res_simpletest = fopen("./res/avl_simple.txt", "w");
    vector<int> arr;
    int i = 10;
    for(int i = 0; i < 10; i++) {
        clock_t timer_s, timer_e;
        root = NULL;
        fprintf(res_simpletest, "%d\n", data_mass[i]);
        for(int k = 1; k <= 5; k++) {
            cerr << "[Info] Running Test Case " << (i+1) << "." << (k) << "Data Mass: " << data_mass[i] << endl;

            // Insert Function Test
            arr = generate_random_array(data_mass[i]);
            timer_s = clock();
            for(auto i : arr) root = avltree_insert(root, i);
            timer_e = clock();
            fprintf(res_simpletest, "%f ", (double)(timer_e - timer_s) / CLOCKS_PER_SEC);
            arr.clear();

            // Search Function Test
            arr = generate_random_array(data_mass[i]);
            timer_s = clock();
            for(auto i : arr) avltree_search(root, i);
            timer_e = clock();
            fprintf(res_simpletest, "%f ", (double)(timer_e - timer_s) / CLOCKS_PER_SEC);
            arr.clear();

            // Delete Function Test
            arr = generate_random_array(data_mass[i]);
            timer_s = clock();
            for(auto i : arr) root = avltree_delete(root, i);
            timer_e = clock();
            fprintf(res_simpletest, "%f\n", (double)(timer_e - timer_s) / CLOCKS_PER_SEC);
            arr.clear();
        }
    }
    fclose(res_simpletest);
}

vector<int> arr;
// Fix the Insert Process 100,0000
// Change the ratio of Delete/Insert, Search/Insert, Test the time
void CombinationFunctionTest() {
    const int INS_NUM = 1000000;
    FILE *res_combtest = fopen("./res/avl_comb.txt", "w");
    FILE *tmp_sea, *tmp_del, *tmp_ins;

    clock_t timer_s, timer_e;
    for(int del_num = INS_NUM; del_num >= INS_NUM/100; del_num -= INS_NUM/100) {
        for(int search_num = INS_NUM; search_num >= INS_NUM/100; search_num -= INS_NUM/100) {
            cerr << "[Info] Running Test Case " << "Delete/Insert ratio:" << (double)del_num / INS_NUM << "; Search/Insert ratio:" << (double)search_num / INS_NUM << endl;
            fprintf(res_combtest, "%lf %lf ", (double)del_num / INS_NUM, (double)search_num / INS_NUM);
            // Insert 1000,000 data first
            tmp_sea = fopen("./tmp/tmp_sea.txt", "w");
            tmp_del = fopen("./tmp/tmp_del.txt", "w");
            tmp_ins = fopen("./tmp/tmp_ins.txt", "w");

            arr = generate_random_array(INS_NUM);
            for(auto i : arr) {
                root = avltree_insert(root, i);
                fprintf(tmp_ins, "%d\n", i);
            }
            fclose(tmp_ins);arr.clear();

            arr = generate_random_array(search_num);
            for(auto i : arr) fprintf(tmp_sea, "%d\n", i);
            arr.clear(); fclose(tmp_sea);

            arr = generate_random_array(del_num);
            for(auto i : arr) fprintf(tmp_del, "%d\n", i);
            arr.clear(); fclose(tmp_del);

            tmp_sea = fopen("./tmp/tmp_sea.txt", "r");
            tmp_del = fopen("./tmp/tmp_del.txt", "r");
            
            timer_s = clock();
            for(int i = 0; i < search_num; i++) {
                int x; fscanf(tmp_sea, "%d", &x);
                avltree_search(root, x);
            }
            for(int i = 0; i < del_num; i++) {
                int x; fscanf(tmp_del, "%d", &x);
                root = avltree_delete(root, x);
            }
            timer_e = clock();
            tmp_ins = fopen("./tmp/tmp_ins.txt", "r");
            for(int i = 0; i < INS_NUM; i++) {
                int x; fscanf(tmp_ins, "%d", &x);
                root = avltree_delete(root, x);
            }

            fclose(tmp_ins);
            fclose(tmp_del);
            fclose(tmp_sea);
            fprintf(res_combtest, "%lf\n", (double)(timer_e - timer_s) / CLOCKS_PER_SEC);
            cerr << (double)(timer_e - timer_s) / CLOCKS_PER_SEC << endl;
        }
    }
    fclose(res_combtest);
}

int main() {
    SimpleFunctionTest();
    //CombinationFunctionTest();
    return 0;
}