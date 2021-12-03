use std::fs;


fn main() {
    let contents = fs::read_to_string("input_second_part.txt").expect("Something went wrong reading the file");

    let mut increase_count = 0;
    let mut last_sum: Option<i32> = None;
    let mut v: Vec<i32> = Vec::new();

    for line in contents.lines() {
        let current_value = line.parse::<i32>().unwrap();
        v.push(current_value);
    }

    for i in 0..v.len() - 2 {
        let current_sum = v[i] + v[i + 1] + v[i + 2];
        match last_sum {
            Some(last_sum) => {
                if current_sum > last_sum {
                    increase_count += 1;
                }
            }
            None => {
                last_sum = Some(current_sum);
            }
        }
        last_sum = Some(current_sum);
    }

    println!("{}", increase_count);
}