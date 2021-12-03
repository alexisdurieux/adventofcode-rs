use std::fs;


fn main() {
    let contents = fs::read_to_string("input_first_part.txt").expect("Something went wrong reading the file");

    let mut increase_count = 0;
    let mut last_value: Option<i32> = None;

    for line in contents.lines() {
        let current_value = line.parse::<i32>().unwrap();
        match last_value {
            Some(last_value) => {
                if current_value > last_value {
                    increase_count += 1;
                }
            }
            None => {
                last_value = Some(current_value);
            }
        }
        last_value = Some(current_value);
    }

    println!("{}", increase_count);
}