
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int sx;
    int sy;
    int ex;
    int ey;
} rect;

rect get_rect(char *line) {
    const char delims[] = "# @,x:";
    char * token = strtok(line, delims);
    rect r;
    token = strtok(NULL, delims);
    r.sx = atoi(token);
    token = strtok(NULL, delims);
    r.sy = atoi(token);
    token = strtok(NULL, delims);
    r.ex = r.sx + atoi(token);
    token = strtok(NULL, delims);
    r.ey = r.sy + atoi(token);
    return r;
}

int main() {
    FILE * fp = fopen("inputs/day_3.txt", "r");
    char line[30];
    short int grid[1000][1000];
    for (size_t i = 0; i < 1000; i++) {
        for (size_t j = 0; j < 1000; j++) {
            grid[i][j] = 0;
        }
    }
    rect r;

    while (fgets(line, 30, fp)) {
        r = get_rect(line);
        for (int i = r.sx; i < r.ex; i++) {
            for (int j = r.sy; j < r.ey; j++) {
                grid[i][j]++;
            }
        }
    }
    fclose(fp);

    FILE * fp_out = fopen("output.txt", "w");
    int count = 0;
    for (size_t i = 0; i < 1000; i++) {
        for (size_t j = 0; j < 1000; j++) {
            if (grid[i][j] >= 2) {
                count++;
            }
            if (grid[i][j] == 1) {
                fprintf(fp_out, "#");
            }
            else {
                fprintf(fp_out, ".");
            }
        }
        fprintf(fp_out, "\n");
    }
    fclose(fp_out);
    // Part 2 can be found by observing the most rectangular object in output.txt and finding its corresponding ID in the file
    printf("Part 1: %i", count);
    return 0;
}