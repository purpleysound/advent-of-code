
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>


#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))


typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    int r;
    int c;
} GridPoint;

typedef struct {
    char** array;
    size_t size;
} StringArray;

typedef struct {
    int* array;
    size_t size;
} IntArray;

typedef struct {
    char** grid;
    size_t rows;
    size_t cols;
} Grid;


void free_string_array(StringArray arr) {
    for (size_t i = 0; i < arr.size; i++) {
        free(arr.array[i]);
    }
    free(arr.array);
}

void free_int_array(IntArray arr) {
    free(arr.array);
}

void free_grid(Grid grid) {
    for (size_t i = 0; i < grid.rows; i++) {
        free(grid.grid[i]);
    }
    free(grid.grid);
}


char* read_input_file(char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error: Could not open file %s\n", filename);
        exit(1);
    }

    fseek(file, 0, SEEK_END);
    long length = ftell(file);
    fseek(file, 0, SEEK_SET);

    char* buffer = (char*)malloc(length + 2);
    if (buffer == NULL) {
        printf("Error: Could not allocate memory for file %s\n", filename);
        fclose(file);
        exit(1);
    }

    fread(buffer, 1, length, file);
    if (buffer[length - 1] != '\n') {
        buffer[length] = '\n';
        length++;
    }
    buffer[length] = '\0';
    fclose(file);

    return buffer;
}

StringArray split_string(char* str, char* delim) {
    StringArray result = {0};
    char* token = strtok(str, delim);
    while (token != NULL) {
        result.array = (char**)realloc(result.array, (result.size + 1) * sizeof(char*));
        result.array[result.size++] = token;
        token = strtok(NULL, delim);
    }
    return result;
}

IntArray get_nums(char* str) {
    IntArray result = {0};
    char* endptr = str;
    while (*endptr != '\0') {
        int num = strtol(endptr, &endptr, 10);
        if (endptr != str) {
            result.array = (int*)realloc(result.array, (result.size + 1) * sizeof(int));
            result.array[result.size++] = num;
            str = endptr;
        } else {
            endptr++;
        }
    }
    return result;
}

Grid read_grid(char* filename) {
    char* input = read_input_file(filename);
    StringArray lines = split_string(input, "\n");

    Grid grid = {0};
    grid.rows = lines.size;
    grid.cols = strlen(lines.array[0]);

    grid.grid = (char**)malloc(grid.rows * sizeof(char*));
    for (size_t i = 0; i < grid.rows; i++) {
        grid.grid[i] = (char*)malloc(grid.cols * sizeof(char));
        strcpy(grid.grid[i], lines.array[i]);
    }

    free_string_array(lines);
    free(input);
    return grid;
}

