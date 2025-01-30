package aoc;

public class Point {
    public int x;
    public int y;
    public static final Point[] DIR4 = {
        new Point(0, -1), new Point(1, 0),
        new Point(0, 1), new Point(-1, 0)
    };
    public static final Point[] DIR8 = {
        new Point(-1, -1), new Point(0, -1), new Point(1, -1),
        new Point(-1, 0),                     new Point(1, 0),
        new Point(-1, 1), new Point(0, 1), new Point(1, 1)
    };

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Point add(Point other) {
        return new Point(this.x + other.x, this.y + other.y);
    }   
}
