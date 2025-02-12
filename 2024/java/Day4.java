
import aoc.FileHandler;
import aoc.Point;

public class Day4 {
    public static void main(String[] args) {
        String input = FileHandler.getInput(4);
        String[] splitInput = input.split("\n");
        int gridSize = splitInput.length;
        char[][] grid = new char[gridSize][gridSize];
        for (int i = 0; i < gridSize; i++) {
            grid[i] = splitInput[i].toCharArray();
        }
        System.out.println(part1(grid));
        System.out.println(part2(grid));
    }

    public static int part1(char[][] grid) {
        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                for (Point dir : Point.DIR8) {
                    if (findXMAS(grid, r, c, dir)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    private static boolean findXMAS(char[][] grid, int r, int c, Point dir) {
        String toFind;
        Point cur;
        boolean success;
        char nextLetter;
        cur = new Point(r, c);
        success = true;
        toFind = "XMAS";
        while (!toFind.equals("")) {
            if (cur.x < 0 || cur.x >= grid[0].length || cur.y < 0 || cur.y >= grid.length) {
                success = false;
                break;
            }
            nextLetter = toFind.charAt(0);
            toFind = toFind.substring(1);
            if (grid[cur.y][cur.x] == nextLetter) {
                cur = cur.add(dir);
            } else {
                success = false;
                break;
            }
        }
        return success;
    }

    public static int part2(char[][] grid) {
        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 'A') {
                    if (findMAS(grid, r, c)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    private static boolean findMAS(char[][] grid, int r, int c) {
        if (r - 1 < 0 || r + 1 >= grid.length || c - 1 < 0 || c + 1 >= grid[0].length) {
            return false;
        }
        if (grid[r - 1][c - 1] == 'M') {
            if (grid[r + 1][c + 1] != 'S') {
                return false;
            }
        } else if (grid[r - 1][c - 1] == 'S') {
            if (grid[r + 1][c + 1] != 'M') {
                return false;
            }
        } else {
            return false;
        }

        if (grid[r - 1][c + 1] == 'M') {
            if (grid[r + 1][c - 1] != 'S') {
                return false;
            }
        } else if (grid[r - 1][c + 1] == 'S') {
            if (grid[r + 1][c - 1] != 'M') {
                return false;
            }
        } else {
            return false;
        }

        return true;
    }
}
