fn main() {
    let res = include_str!("../input.txt")
        .lines()
        .map(|l| {
            return l.chars().map(|c| {
                c.to_digit(10).unwrap() as u16
            }).collect();
        })
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
    let test = 9;
    println!("{}, {}, {}, {:?}", epsilon_int, gamma_int, gamma_int * epsilon_int, gamma);
    println!("{}, {}", test, !test);
    
}
