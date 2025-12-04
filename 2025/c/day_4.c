
#include "aoc.h"

struct cycle_result {
    Grid grid;
    int count;
    bool changed;
};

struct cycle_result cycle(Grid grid) {
    Grid new_grid = {0};
    new_grid.rows = grid.rows;
    new_grid.cols = grid.cols;
    new_grid.grid = (char**)malloc(new_grid.rows * sizeof(char*));
    for (size_t i = 0; i < new_grid.rows; i++) {
        new_grid.grid[i] = (char*)malloc(new_grid.cols * sizeof(char));
        strcpy(new_grid.grid[i], grid.grid[i]);
    }

    int total = 0;
    bool changed = false;

    for (size_t r = 0; r < grid.rows; r++) {
        for (size_t c = 0; c < grid.cols; c++) {
            if (grid.grid[r][c] == '.') {
                continue;
            }
            int neighbours = 0;
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) {
                        continue;
                    }
                    size_t nr = r + dr;
                    size_t nc = c + dc;
                    if (nr < 0 || nc < 0 || nr >= grid.rows || nc >= grid.cols) {
                        continue;
                    }
                    if (nr < grid.rows && nc < grid.cols && grid.grid[nr][nc] == '@') {
                        neighbours++;
                    }
                }
            }
            if (neighbours < 4) {
                total++;
                new_grid.grid[r][c] = '.';
                changed = true;
            }
        }
    }

    struct cycle_result result = {0};
    result.grid = new_grid;
    result.count = total;
    result.changed = changed;
    return result;
}


int main() {
    Grid grid = read_grid("../inputs/day_4.txt");
    int total = 0;
    for (size_t r = 0; r < grid.rows; r++) {
        for (size_t c = 0; c < grid.cols; c++) {
            if (grid.grid[r][c] == '.') {
                continue;
            }
            int neighbours = 0;
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) {
                        continue;
                    }
                    size_t nr = r + dr;
                    size_t nc = c + dc;
                    if (nr < 0 || nc < 0 || nr >= grid.rows || nc >= grid.cols) {
                        continue;
                    }
                    if (nr < grid.rows && nc < grid.cols && grid.grid[nr][nc] == '@') {
                        neighbours++;
                    }
                }
            }
            if (neighbours < 4) {
                total++;
            }
        }
    }

    printf("%d\n", total);


    total = 0;
    bool changed = true;
    while (changed) {
        struct cycle_result result = cycle(grid);
        total += result.count;
        changed = result.changed;
        free_grid(grid);
        grid = result.grid;
    }

    printf("%d\n", total);

    free_grid(grid);

    return 0;
}