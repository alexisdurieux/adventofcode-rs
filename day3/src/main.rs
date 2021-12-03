fn select_vector(arr: Vec<Vec<u16>>, bit_criteria: u16, idx: usize) -> Vec<u16> {
    // println!("{:?}", arr);
    match arr.len() as usize {
        1 => arr[0].clone(),
        _ => {
            let criteria_count: u16 = arr.iter().fold(0, |c, x| {
                if x[idx] == bit_criteria { c + 1 } else { c }
            });
            // println!("bit_criteria: {} criteria_count: {}, {}", bit_criteria, criteria_count, arr.len());
            let filtered = arr.iter().filter(|x| {
                if bit_criteria == 1 {
                    if criteria_count as f32 >= (arr.len() as f32 / 2 as f32) { x[idx] == bit_criteria } else { x[idx] != bit_criteria }
                } else {
                    if criteria_count as f32 <= (arr.len() as f32 / 2 as f32) { x[idx] == bit_criteria } else { x[idx] != bit_criteria }
                }
            }).cloned().collect();
            select_vector(filtered, bit_criteria, idx + 1)
        }
    }
    


}   

fn main() {
    let lines_iter = include_str!("../input.txt")
        .lines()
        .map(|l| {
            return l.chars().map(|c| {
                c.to_digit(10).unwrap() as u16
            }).collect();
        });
    let res = 
        lines_iter.clone()
        .fold( (Vec::new(), 0), | (mut acc, c), x: Vec<u16> | {
            match acc.is_empty() {
                true => (x, c+1),
                false => {
                    x.iter().enumerate().for_each(|(i, &v)| {
                        acc[i] += v
                    });
                    (acc, c + 1)
                }
            }
        });
    let mut gamma = vec![0; res.0.len()];
    res.0.iter().enumerate().for_each(|(i, &v)| {
        gamma[i] = (v > (res.1 / 2)) as u8;
    });
    let base: i32 = 2;
    let (gamma_int, epsilon_int) = gamma.iter().enumerate().fold((0, 0), |(gamma, epsilon), (idx, &v)| {
        (   gamma + (base.pow(res.0.len() as u32 - idx as u32 - 1) * v as i32), 
            epsilon + (base.pow(res.0.len() as u32 - idx as u32 - 1) * if v == 0 { 1 } else { 0 } as i32)
        )
    });
    println!("{}, {}, {}, {:?}", epsilon_int, gamma_int, gamma_int * epsilon_int, gamma);

    let oxygen_vec = select_vector(lines_iter.clone().collect(), 1, 0);
    let cotwo_vec = select_vector(lines_iter.clone().collect(), 0, 0);

    let oxygen_int = oxygen_vec.iter().enumerate().fold(0, |acc, (idx, &v)| {
        acc + (base.pow(oxygen_vec.len() as u32 - idx as u32 - 1) * v as i32)
    });

    let cotwo_int = cotwo_vec.iter().enumerate().fold(0, |acc, (idx, &v)| {
        acc + (base.pow(cotwo_vec.len() as u32 - idx as u32 - 1) * v as i32)
    });



    print!("{}", oxygen_int * cotwo_int);


    
}
