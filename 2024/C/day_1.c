
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int cmp(const void * a, const void * b) {
    return (*(int*)a - *(int*)b);
}

int count(int * arr, int len, int val) {
    int count = 0;
    for (int i = 0; i < len; i++) {
        if (arr[i] == val) {
            count++;
        }
    }
    return count;
}

int main() {
    FILE * fp = fopen("../inputs/day_1.txt", "r");
    if (fp == NULL) {
        return 1;
    }
    int lefts[1000];
    int rights[1000];
    char line[15];
    int idx = 0;
    while (fgets(line, 15, fp)) {
        int left, right;
        sscanf(line, "%i   %i", &left, &right);
        lefts[idx] = left;
        rights[idx] = right;
        idx++;
    }
    fclose(fp);
    qsort(lefts, idx, sizeof(int), cmp);
    qsort(rights, idx, sizeof(int), cmp);

    int total1 = 0;
    int total2 = 0;
    for (int i = 0; i < idx; i++) {
        total1 += abs(lefts[i] - rights[i]);
        total2 += lefts[i] * count(rights, idx, lefts[i]);
    }
    printf("Part 1: %i\n", total1);
    printf("Part 2: %i\n", total2);

    return 0;
}