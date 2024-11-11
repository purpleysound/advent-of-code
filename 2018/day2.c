
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char letter;
    int count;
} letter_count;

letter_count* initialise_counters() {
    const char alphabet[26] = "abcdefghijklmnopqrstuvwxyz";
    letter_count *counts = malloc(sizeof(letter_count)*26);
    if (!counts) {
        printf("Error allocating memory");
    }
    for (size_t i = 0; i < 26; i++) {
        counts[i] = (letter_count){.letter = alphabet[i], .count = 0};
    }
    return counts;
};


int get_counter_idx(letter_count* counters, char c) {
    for (size_t i = 0; i < 26; i++) {
        letter_count counter = counters[i];
        if (counter.letter == c) {
            return i;     
        }
    }
}


bool check_num_count(char line[28], int target_count) {
    letter_count* counters = initialise_counters();
    for (size_t i = 0; i < 26; i++) {
        char c = line[i];
        int counter_idx = get_counter_idx(counters, c);
        counters[counter_idx].count++;
    }
    for (size_t i = 0; i < 26; i++) {
        letter_count finished_counter = counters[i];
        if (finished_counter.count == target_count) {
            return true;
        }
    }
    return false;
}


int main() {
    FILE *fp = fopen("inputs/day_2.txt", "r");
    char line[28];
    char* lines[250];
    int two_count = 0;
    int three_count = 0;
    int idx = 0;
    while (fgets(line, 28, fp)) {
        lines[idx] = strdup(line);
        idx++;
        if (check_num_count(line, 2)) {
            two_count++;
        }
        if (check_num_count(line, 3)) {
            three_count++;
        }
        
    }
    printf("Part 1: %i\n", two_count*three_count);

    for (size_t i = 0; i < 249; i++) {
        char* str1 = lines[i];
        for (size_t j = i+1; j <= 249; j++) {
            char* str2 = lines[j];
            int matching = 0;
            for (size_t k = 0; k < 26; k++) {
                if (str1[k] == str2[k]) {
                    matching++;
                }
            }
            if (matching == 25) {
                printf("Part 2: ");
                for (size_t l = 0; l < 26; l++) {
                    if (str1[l] == str2[l]) {
                        printf("%c", str1[l]);
                    }
                }
                printf("\n");
            }
        }  
    }

    return 0;
}
