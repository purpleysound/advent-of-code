
#include <stdio.h>
#include <stdbool.h>

const fpos_t ZERO_POS = 0;

bool valueInArray(int value, int arr[], int n) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == value) {
            return true;
        }
    }
    return false;
}

int main() {
    FILE *fp;
    fp = fopen("inputs/day_1.txt", "r");
    int total = 0;
    char line[10];
    int num;

    while (fgets(line, 10, fp)) {
        num = atoi(line);
        total += num;
    }
    printf("Part 1: %i\n", total);
    
    fsetpos(fp, &ZERO_POS);
    total = 0;
    int seen[500000];
    int idx = 0;

    while (true) {
        while (fgets(line, 10, fp)) {
            num = atoi(line);
            total += num;
            seen[idx] = total;
            if (valueInArray(total, seen, idx)) {
                    printf("Part 2: %i\n", total);
                    fclose(fp);
                    return 0;
            }
            idx++;
        }
        
        fsetpos(fp, &ZERO_POS);
    }
}
