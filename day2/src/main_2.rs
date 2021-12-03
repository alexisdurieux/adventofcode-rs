use std::fs;
use std::time::Instant;

fn main() {
    let now = Instant::now();

   
    let contents = fs::read_to_string("input.txt").expect("Something went wrong reading the file");

    let mut horizontal_pos: i32 = 0;
    let mut depth: i32 = 0;
    let mut aim: i32 = 0;

    for line in contents.lines() {
        let vec: Vec<&str> = line.split(" ").collect();
        match vec.as_slice() {
            ["forward", v] => {
                let v_int = v.parse::<i32>().unwrap();
                horizontal_pos = horizontal_pos + v_int;
                depth = depth + (aim * v_int);
            },
            ["down", v] => {
                let v_int = v.parse::<i32>().unwrap();
                aim = aim + v_int;
            },
            ["up", v] => {
                let v_int = v.parse::<i32>().unwrap();
                aim = aim - v_int;
            },
            _ => ()
        }
    }

    println!("{} in {} ns", horizontal_pos * depth, now.elapsed().as_nanos());
}