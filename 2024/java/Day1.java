
import java.util.Arrays;

public class Day1 {
    public static void main(String[] args) {
        String input = AOC.getInput(1);
        int[][] nums = parseInput(input);
        System.out.println(part1(nums[0], nums[1]));
        System.out.println(part2(nums[0], nums[1]));
    }

    private static int[][] parseInput(String input) {
        String[] lines = input.split("\n");
        int[] nums1 = new int[lines.length];
        int[] nums2 = new int[lines.length];
        for (int i = 0; i < lines.length; i++) {
            String[] nums = lines[i].split("   ");
            nums1[i] = Integer.parseInt(nums[0].strip());
            nums2[i] = Integer.parseInt(nums[1].strip());
        }
        return new int[][] {nums1, nums2};
    }

    private static int part1(int[] nums1, int[] nums2) {
        nums1 = Arrays.stream(nums1).sorted().toArray();
        nums2 = Arrays.stream(nums2).sorted().toArray();
        int sum = 0;
        for (int i = 0; i < nums1.length; i++) {
            sum += Math.abs(nums1[i] - nums2[i]);
        }
        return sum;
    }

    private static int part2(int[] nums1, int[] nums2) {
        int sum = 0;
        for (int num : nums1) {
            for (int num2 : nums2) {
                if (num == num2) {
                    sum += num;
                }
            }
        }
        return sum;
    }
}
