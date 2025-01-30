package aoc;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FileHandler {
    public static String getInput(int day) {
        String dayString = Integer.toString(day);
        String path = "../inputs/day_" + dayString + ".txt";
        return readFile(path);
    }

    private static String readFile(String path) {
        try {
            return new String(Files.readAllBytes(Paths.get(path)));
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        }
    } 
}
