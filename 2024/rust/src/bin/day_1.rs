
fn main() {
    let input: &str = include_str!("../../../inputs/day_1.txt");
    let (left, right) = parse_input(input);
    println!("Part 1: {}", part1(&left, &right));
    println!("Part 2: {}", part2(&left, &right));
}

fn parse_input(input: &str) -> (Vec<i32>, Vec<i32>) {
    let mut left = Vec::new();
    let mut right = Vec::new();
    
    for line in input.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() == 2 {
            left.push(parts[0].parse().unwrap());
            right.push(parts[1].parse().unwrap());
        } else {
            panic!("Invalid input format");
        }
    }
    (left, right)
}

fn part1(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    let mut left = left.clone();
    left.sort();
    let mut right = right.clone();
    right.sort();
    let mut total = 0;
    for (ln, rn) in left.iter().zip(right.iter()) {
        total += (ln - rn).abs();
    }
    total
}

fn part2(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    let mut total = 0;
    for ln in left.iter() {
        for rn in right.iter() {
            if ln == rn {
                total += ln
            }
        }
    }
    total
}
