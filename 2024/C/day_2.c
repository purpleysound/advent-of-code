
#include "aoc.h"

bool is_safe(IntArray nums) {
    IntArray deltas = {0};
    deltas.array = (int*)malloc((nums.size-1) * sizeof(int));
    deltas.size = nums.size-1;
    for (size_t i = 1; i < nums.size; i++) {
        deltas.array[i-1] = nums.array[i] - nums.array[i-1];
    }

    if (deltas.array[0] < 0) {
        for (size_t i = 0; i < deltas.size; i++) {
            deltas.array[i] = -deltas.array[i];
        }
    }

    for (size_t i = 0; i < deltas.size; i++) {
        if ((deltas.array[i] > 3) || (deltas.array[i] < 1)) {
            free_int_array(deltas);
            free_int_array(nums);
            return false;
        }
    }
    
    free_int_array(deltas);
    free_int_array(nums);
    return true;
}

int main() {
    char* input = read_input_file("../inputs/day_2.txt");
    StringArray lines = split_string(input, "\n");
    int count = 0;
    for (size_t i = 0; i < 1001; i++) {
        IntArray nums = get_nums(lines.array[i]);
        if (nums.size < 5) {
            free_int_array(nums);
            printf("Skipping line %i\n", i);
            continue;
        }
        if (is_safe(nums)) {
            count++;
        }
    }
    printf("Part 1: %i\n", count);
    free_string_array(lines);
    free(input);
    return 0;
}
