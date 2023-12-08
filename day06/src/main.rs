use std::{fs::File, io::Read};

fn main() {
    let mut file = File::open("input.txt").unwrap();

    let mut contents = String::new();

    file.read_to_string(&mut contents)
        .expect("Failed to read file");

    println!("Part 1: {}", compute(parse_part1_input(&contents)));
    println!("Part 2: {}", compute(parse_part2_input(&contents)));
}

struct Race {
    time: u64,
    dist: u64,
}

fn get_distance(hold_time: u64, total_time: u64) -> u64 {
    hold_time * (total_time - hold_time)
}

fn parse_part1_input(input: &str) -> Vec<Race> {
    let mut time_values = Vec::new();
    let mut dist_values = Vec::new();

    for line in input.lines() {
        // Here we need the type annotation because otherwise the `s.parse()`
        // function will not know which type to parse into.
        let values: Vec<u64> = line
            .split_whitespace()
            .skip(1)
            .map(|s| s.parse().expect("Failed to parse value"))
            .collect();

        if line.starts_with("Time:") {
            time_values.extend(values);
        } else if line.starts_with("Distance:") {
            dist_values.extend(values)
        }
    }

    time_values
        .iter()
        .zip(dist_values.iter())
        .map(|(&time, &dist)| Race { time, dist })
        .collect()
}

fn parse_part2_input(input: &str) -> Vec<Race> {
    let mut time_val: u64 = 0;
    let mut dist_val: u64 = 0;

    for line in input.lines() {
        let val: String = line.split_whitespace().skip(1).collect();

        if line.starts_with("Time:") {
            time_val = val.parse().unwrap();
        } else if line.starts_with("Distance:") {
            dist_val = val.parse().unwrap();
        }
    }

    vec![Race {
        time: time_val,
        dist: dist_val,
    }]
}

fn compute(races: Vec<Race>) -> u64 {
    races
        .iter()
        .map(|race| {
            let mut break_count = 0;

            for hold in 0..race.time {
                if let true = get_distance(hold, race.time) > race.dist {
                    break_count += 1
                };
            }
            break_count
        })
        .product()
}

#[cfg(test)]
mod tests {
    use super::compute;
    use super::parse_part1_input;
    use super::parse_part2_input;

    #[test]
    fn part1_sample() {
        let input = "\
Time:      7  15   30
Distance:  9  40  200\
";
        assert_eq!(compute(parse_part1_input(input)), 288);
        println!("{}", input)
    }

    #[test]
    fn part2_sample() {
        let input = "\
Time:      7  15   30
Distance:  9  40  200\
";
        assert_eq!(compute(parse_part2_input(input)), 71503)
    }
}
