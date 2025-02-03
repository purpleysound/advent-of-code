
import aoc.FileHandler;
import java.util.stream.IntStream;

public class Day5 {
    public static void main(String[] args) {
        String input = FileHandler.getInput(5);
        String[] splitInput = input.split("\n\n");
        String[] strRules = splitInput[0].split("\n");
        String[] strPages = splitInput[1].split("\n");
        int[][] rules = parseRules(strRules);
        int[][] pagesArray = parsePages(strPages);
        System.out.println(part1(rules, pagesArray));
        System.out.println(part2(rules, pagesArray));
    }

    private static int[][] parseRules(String[] strRules) {
        int[][] rules = new int[strRules.length][2];
        for (int i = 0; i < strRules.length; i++) {
            String[] splitRule = strRules[i].split("\\|");
            rules[i][0] = Integer.parseInt(splitRule[0]);
            rules[i][1] = Integer.parseInt(splitRule[1]);
        }
        return rules;
    }

    private static int[][] parsePages(String[] strPages) {
        int[][] pages = new int[strPages.length][];
        for (int i = 0; i < strPages.length; i++) {
            String[] splitPages = strPages[i].split(",");
            pages[i] = new int[splitPages.length];
            for (int j = 0; j < splitPages.length; j++) {
                pages[i][j] = Integer.parseInt(splitPages[j]);
            }
        }
        return pages;
    }

    public static int part1(int[][] rules, int[][] pagesArray) {
        int count = 0;
        int middle;
        for (int[] pages : pagesArray) {
            if (isOrdered(rules, pages)) {
                middle = pages[pages.length/2];
                count += middle;
            }
        }
        return count;
    }

    private static boolean isOrdered(int[][] rules, int[] pages) {
        for (int[] rule : rules) {
            if (IntStream.of(pages).filter(page -> page == rule[0] || page == rule[1]).count() == 2) {
                // both values in rule are in the array
                int index1 = -1;
                int index2 = -1;
                for (int i = 0; i < pages.length; i++) {
                    if (pages[i] == rule[0]) {
                        index1 = i;
                    }
                    if (pages[i] == rule[1]) {
                        index2 = i;
                    }
                }
                if (index1 > index2) {
                    return false;
                }
            }
        }
        return true;
    }

    public static int part2(int[][] rules, int[][] pagesArray) {
        int count = 0;
        for (int[] pages : pagesArray) {
            if (isOrdered(rules, pages)) {
                continue;
            }
            int[] orderedPages = orderPages(rules, pages);
            int middle = orderedPages[orderedPages.length/2];
            count += middle;
        }
        return count;
    }

    private static int[] orderPages(int[][] rules, int[] pages) {
        int[] orderedPages = pages.clone();
        for (int[] rule : rules) {
            if (IntStream.of(orderedPages).filter(page -> page == rule[0] || page == rule[1]).count() == 2) {
                // both values in rule are in the array
                int index1 = -1;
                int index2 = -1;
                for (int i = 0; i < orderedPages.length; i++) {
                    if (orderedPages[i] == rule[0]) {
                        index1 = i;
                    }
                    if (orderedPages[i] == rule[1]) {
                        index2 = i;
                    }
                }
                if (index1 > index2) {
                    int temp = orderedPages[index1];
                    orderedPages[index1] = orderedPages[index2];
                    orderedPages[index2] = temp;
                    break;
                }
            }
        }
        if (!isOrdered(rules, orderedPages)) {
            return orderPages(rules, orderedPages);
        }
        return orderedPages;
    }
}
