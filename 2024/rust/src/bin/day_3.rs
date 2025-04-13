use regex::Regex;

fn main() {
    let input = include_str!("../../../inputs/day_3.txt");
    println!("Part 1: {}", part1(input));
    println!("Part 2: {}", part2(input));
}

fn part1(input: &str) -> i32 {
    let re = Regex::new(r"mul\(\d+,\d+\)").unwrap();
    let mut total = 0;
    for re_match in re.find_iter(input) {
        let mul_str = re_match.as_str();
        let left = mul_str[4..mul_str.find(',').unwrap()].parse::<i32>().unwrap();
        let right = mul_str[mul_str.find(',').unwrap() + 1..mul_str.len() - 1].parse::<i32>().unwrap();
        total += left * right;
    }
    total
}

fn part2(input: &str) -> i32 {
    let re = Regex::new(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))").unwrap();
    let do_str = "do()";
    let dont_str = "don't()";
    let mut total = 0;
    let mut active = true;
    for re_match in re.find_iter(input) {
        let mul_str = re_match.as_str();
        
        if mul_str == do_str {
            active = true;
            continue;
        } else if mul_str == dont_str {
            active = false;
            continue;
        }
        if !active {
            continue;
        }

        let left = mul_str[4..mul_str.find(',').unwrap()].parse::<i32>().unwrap();
        let right = mul_str[mul_str.find(',').unwrap() + 1..mul_str.len() - 1].parse::<i32>().unwrap();
        total += left * right;
    }
    total
}
