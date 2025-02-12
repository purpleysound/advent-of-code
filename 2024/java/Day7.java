
import aoc.FileHandler;
import java.util.stream.Stream;

public class Day7 {
    public static void main(String[] args) {
        String input = FileHandler.getInput(7);
        String[] lines = input.split("\n");
        long count1 = 0;
        long count2 = 0;
        for (String line : lines) {
            long target = parseTarget(line);
            int[] nums = parseNumbers(line);
            if (part1(target, nums)) {
                count1 += target;
            }
            if (part2(target, nums)) {
                count2 += target;
            }
        }
        System.out.println(count1);
        System.out.println(count2);
    }

    private static long parseTarget(String line) {
        return Long.parseLong(line.split(":")[0]);
    }

    private static int[] parseNumbers(String line) {
        return Stream.of(line.split(": ")[1].split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
    }

    public static boolean part1(long target, int[] nums) {
        for (int i = 0; i < Math.pow(2, nums.length - 1); i++) {
            int ops = i;
            int j = 1;
            long total = nums[0];
            for (int k = 0; k < nums.length - 1; k++) {
                if ((ops % 2) == 0) {
                    total += nums[j];
                } else {
                    total *= nums[j];
                }
                ops /= 2;
                j++;
            }
            if (total == target) {
                return true;
            }
        }
        return false;
    }

    public static boolean part2(long target, int[] nums) {
        for (int i = 0; i < Math.pow(3, nums.length - 1); i++) {
            int ops = i;
            int j = 1;
            long total = nums[0];
            for (int k = 0; k < nums.length - 1; k++) {
                if ((ops % 3) == 0) {
                    total += nums[j];
                } else if ((ops % 3) == 1) {
                    total *= nums[j];
                } else {
                    total = Long.parseLong("" + total + nums[j]);
                }
                ops /= 3;
                j++;
            }
            if (total == target) {
                return true;
            }
        }
        return false;
    }

}
