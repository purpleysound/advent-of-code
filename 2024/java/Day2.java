
import java.util.Arrays;

public class Day2 {
    public static void main(String[] args) {
        String input = AOC.getInput(2);
        String[] lines = input.split("\n");
        int sum1 = 0;
        int sum2 = 0;
        for (String line : lines) {
            String[] stringNums = line.split(" ");
            int[] nums = new int[stringNums.length];
            for (int i = 0; i < stringNums.length; i++) {
                nums[i] = Integer.parseInt(stringNums[i].strip());
            }
            if (valid1(nums)) {
                sum1++;
            }
            if (valid2(nums)) {
                sum2++;
            }
        }
        System.out.println(sum1);
        System.out.println(sum2);
    }    

    private static boolean valid1(int[] nums) {
        int[] deltas = new int[nums.length - 1];
        for (int i = 1; i < nums.length; i++) {
            deltas[i - 1] = nums[i] - nums[i - 1];
        }
        if (deltas[0] < 0) {
            deltas = Arrays.stream(deltas).map(x -> -x).toArray();
        }
        return (int) Arrays.stream(deltas).filter(x -> x < 1 || x > 3).count() == 0;
    }

    private static boolean valid2(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int[] newNums = new int[nums.length - 1];
            for (int j = 0; j < nums.length; j++) {
                if (j < i) {
                    newNums[j] = nums[j];
                } else if (j > i) {
                    newNums[j - 1] = nums[j];
                }
            }
            if (valid1(newNums)) {
                return true;
            }
        }
        return false;
    }
}
