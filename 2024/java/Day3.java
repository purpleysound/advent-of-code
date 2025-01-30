
import java.util.regex.Pattern;

import aoc.FileHandler;

import java.util.regex.Matcher;
import java.util.List;
import java.util.ArrayList;

public class Day3 {
    public static void main(String[] args) {
        String input = FileHandler.getInput(3);
        System.out.println(part1(input));
        System.out.println(part2(input));
    }

    private static int part1(String input) {
        int total = 0;
        for (int[] nums : getMuls(input)) {
            total += nums[0] * nums[1];
        }
        return total;
    }

    private static int[][] getMuls(String input) {
        String[] matches = regexMatches(input, "mul\\(\\d+,\\d+\\)");
        int[][] muls = new int[matches.length][2];
        for (int i = 0; i < matches.length; i++) {
            muls[i] = parseMatch(matches[i]);
        }
        return muls;
    }

    private static int part2(String input) {
        String[] matches = regexMatches(input, "(mul\\(\\d+,\\d+\\))|(do\\(\\))|(don't\\(\\))");
        int total = 0;
        boolean enabled = true;
        for (String match : matches) {
            if (match.equals("do()")) {
                enabled = true;
            } else if (match.equals("don't()")) {
                enabled = false;
            } else if (enabled) {
                int[] nums = parseMatch(match);
                total += nums[0] * nums[1];
            }
        }
        return total;
    }

    private static String[] regexMatches(String input, String regex) {
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(input);
        List<String> matches = new ArrayList<>();
        while (matcher.find()) {
            matches.add(matcher.group(0));
        }
        return matches.toArray(new String[matches.size()]);
    }

    private static int[] parseMatch(String match) {
        String[] stringNums = match.split(",");
        
        stringNums[0] = stringNums[0].substring(4);
        stringNums[1] = stringNums[1].substring(0, stringNums[1].length() - 1);
        return new int[] {Integer.parseInt(stringNums[0]), Integer.parseInt(stringNums[1])};
    }
}
