
import aoc.FileHandler;
import aoc.Point;
import java.util.Set;
import java.util.HashSet;;

public class Day6 {
    public static void main(String[] args) {
        String input = FileHandler.getInput(6);
        boolean[][] grid = parseInput(input);
        Point start = findStart(input);
        System.out.println(part1(grid, start));
        System.out.println(part2(grid, start));
    }

    private static boolean[][] parseInput(String input) {
        String[] lines = input.split("\n");
        boolean[][] grid = new boolean[lines.length][lines[0].length()];
        for (int i = 0; i < lines.length; i++) {
            for (int j = 0; j < lines[i].length(); j++) {
                grid[i][j] = lines[i].charAt(j) == '#';
            }
        }
        return grid;
    }

    private static Point findStart(String input) {
        String[] lines = input.split("\n");
        for (int r = 0; r < lines.length; r++) {
            for (int c = 0; c < lines[r].length(); c++) {
                if (lines[r].charAt(c) == '^') {
                    return new Point(r, c);
                }
            }
        }
        return null;
    }

    private static void rotate(Point vec) {
        int tmp = vec.x;
        vec.x = vec.y;
        vec.y = -tmp;
    }

    private static boolean isWallAhead(boolean[][] grid, Point pos, Point vec) {
        Point next = pos.add(vec);
        if (0 <= next.x && next.x < grid.length && 0 <= next.y && next.y < grid[0].length) {
            return grid[next.x][next.y];
        }
        return false;
    }

    private static Set<String> getVisited(boolean[][] grid, Point start) {
        Point vec = new Point(-1, 0);
        Point pos = new Point(start.x, start.y);
        Set<String> visited = new HashSet<>();
        while (0 <= pos.x && pos.x < grid.length && 0 <= pos.y && pos.y < grid[0].length) {
            visited.add(pos.x + "," + pos.y);
            if (isWallAhead(grid, pos, vec)) {
                rotate(vec);
            } else {
                pos = pos.add(vec);
            }
        }
        return visited;
    }

    public static int part1(boolean[][] grid, Point start) {
        Set<String> visited = getVisited(grid, start);
        return visited.size();
    }

    private static Point stringToPoint(String s) {
        String[] parts = s.split(",");
        return new Point(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
    }

    private static boolean canEscape(boolean[][] grid, Point start) {
        Point vec = new Point(-1, 0);
        Point pos = new Point(start.x, start.y);
        Set<String> visited = new HashSet<>();
        int maxSteps = 10000;
        int steps = 0;
        while (0 <= pos.x && pos.x < grid.length && 0 <= pos.y && pos.y < grid[0].length && steps < maxSteps) {
            visited.add(pos.x + "," + pos.y);
            if (isWallAhead(grid, pos, vec)) {
                rotate(vec);
            } else {
                pos = pos.add(vec);
                steps++;
            }
        }
        if (steps == maxSteps) {
            return false;
        }
        return true;
    }

    public static int part2(boolean[][] grid, Point start) {
        Set<String> visited = getVisited(grid, start);
        int count = 0;
        for (String s : visited) {
            Point pos = stringToPoint(s);
            if (pos.x == start.x && pos.y == start.y) {
                continue;
            }
            grid[pos.x][pos.y] = true;
            if (!canEscape(grid, start)) {
                count++;
            }
            grid[pos.x][pos.y] = false;
        }
        return count;
    }
}
