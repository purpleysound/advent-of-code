
fn main() {
    let input: &str = include_str!("../../../inputs/day_2.txt");
    let reports = parse_input(input);
    println!("Part 1: {}", part1(&reports));
    println!("Part 2: {}", part2(&reports));
}

fn parse_input(input: &str) -> Vec<Vec<i32>> {
    let mut reports = Vec::new();
    for line in input.lines() {
        let levels = line.split_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        reports.push(levels);
    }
    reports
}

fn valid(levels: &Vec<i32>) -> bool {
    let mut deltas: Vec<i32> = Vec::new();
    for i in 0..levels.len() - 1 {
        let delta = levels[i + 1] - levels[i];
        deltas.push(delta);
    }
    if deltas[0] < 0 {
        deltas = deltas.iter().map(|x| -x).collect();
    }
    deltas.iter().all(|&x| 1 <= x && x <= 3)
}

fn part1(reports: &Vec<Vec<i32>>) -> i32 {
    let mut count = 0;
    for levels in reports {
        if valid(levels) {
            count += 1;
        }
    }
    count
}

fn part2(reports: &Vec<Vec<i32>>) -> i32 {
    let mut count = 0;
    for levels in reports {
        for i in 0..levels.len() {
            let new_levels = {
                let mut new_levels = levels[..i].to_vec();
                new_levels.extend(levels[i + 1..].to_vec());
                new_levels
            };
            if valid(&new_levels) {
                count += 1;
                break;
            }
        }
    }
    count
}
