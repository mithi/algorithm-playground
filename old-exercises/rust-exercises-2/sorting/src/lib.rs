extern crate rand;
use rand::{thread_rng, Rng};

pub mod merge;
pub mod quick;
pub mod largedata;

#[cfg(test)]
pub mod tests;

pub fn shuffle<T: Ord>(v: &mut [T]) {

    let mut rng = thread_rng();
    for i in 0.. v.len() {
        let r = rng.gen_range(0, i + 1);
        v.swap(i, r);
    }
}

pub mod insertion {

    pub fn sort<T: Ord>(v: &mut [T]) {

        for i in 0..v.len() {
            for j in (1..=i).rev() {
                if v[j] >= v[j - 1] { break; }
                v.swap(j, j - 1);
            }
        }
    }
}

pub mod selection {

    pub fn sort<T: Ord>(v: &mut [T]) {

        for i in 0..v.len() {
            let j = get_min(i, v);
            v.swap(j, i);
        }
    }

    fn get_min<T: Ord>(i: usize, v: &[T]) -> usize {

        let mut min_index = i;
        let mut current_min = &v[i];

        for j in i..v.len() {

            if v[j] < *current_min {
                current_min = &v[j];
                min_index = j;
            }
        }
        min_index
    }
}

pub mod shell {

    pub fn sort<T: Ord>(array: &mut [T], gaps: &[usize]) {
        for gap in gaps {

            if array.len() < *gap { continue; }

            for start in 0..*gap {

                let mut i = start;

                while i < (array.len() - *gap) {
                    let mut j = i;
                    loop {
                        if array[j + *gap] > array[j] { break; }
                        array.swap(j + *gap, j);
                        if j < *gap { break; }
                        j -= *gap;
                    }
                    i += *gap;
                }
            }
        }
    }
}

