use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Something went wrong reading the file");

    let mut horizontal_pos: i32 = 0;
    let mut depth: i32 = 0;

    for line in contents.lines() {
        let vec: Vec<&str> = line.split(" ").collect();
        match vec.as_slice() {
            ["forward", v] => horizontal_pos = horizontal_pos + v.parse::<i32>().unwrap(),
            ["down", v] => depth = depth + v.parse::<i32>().unwrap(),
            ["up", v] => depth = depth - v.parse::<i32>().unwrap(),
            _ => ()
        }
    }

    println!("{} {} {}", horizontal_pos, depth, horizontal_pos * depth);
}