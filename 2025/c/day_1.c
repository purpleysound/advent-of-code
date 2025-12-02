
#include "aoc.h"

int main() {
    char* input = read_input_file("../inputs/day_1.txt");
    StringArray lines = split_string(input, "\n");
    
    int start = 50;
    int zeros = 0;
    for (int i = 0; i < lines.size; i++) {
        char d = lines.array[i][0];
        int val = get_nums(lines.array[i]).array[0];
        if (d == 'R') {
            start = (start + val) % 100;
            if (start == 0) {
                zeros++;
            }
        } else if (d == 'L') {
            start = (start - val) % 100;
            if (start == 0) {
                zeros++;
            }
        }
    }
    printf("\r\n%i\r\n", zeros);


    start = 50;
    zeros = 0;
    for (int i = 0; i < lines.size; i++) {
        char d = lines.array[i][0];
        int val = get_nums(lines.array[i]).array[0];
        if (d == 'R') {
            for (int j = 0; j < val; j++) {
                start++;
                if (start > 99) {
                    start = 0;
                }
                if (start == 0) {
                    zeros++;
                }
            }
        } else if (d == 'L') {
            for (int j = 0; j < val; j++) {
                start--;
                if (start < 0) {
                    start = 99;
                }
                if (start == 0) {
                    zeros++;
                }
            }
        }
    }
    printf("%i\r\n", zeros);

    return 0;
}