extern crate rand;
use rand::{thread_rng, Rng};

pub fn shuffle<T: PartialOrd>(v: &mut [T]) {

    let mut rng = thread_rng();
    for i in 0.. v.len() {
        let r = rng.gen_range(0, i + 1);
        v.swap(i, r);
    }
}

pub mod selection {

    pub fn sort<T: PartialOrd>(v: &mut [T]) {

        for i in 0..v.len() {
            let j = get_min(i, v);
            v.swap(j, i);
        }
    }

    fn get_min<T: PartialOrd>(i: usize, v: &[T]) -> usize {

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


pub mod insertion {

    pub fn sort<T: PartialOrd>(v: &mut [T]) {

        for i in 0..v.len() {
            for j in (1..=i).rev() {
                if v[j] >= v[j - 1] { break; }
                v.swap(j, j - 1);
            }
        }
    }
}


pub mod shell {

    pub fn sort<T: PartialOrd>(array: &mut [T], gaps: &[usize]) {
        for gap in gaps {

            if array.len() < *gap {
                continue;
            }

            for i in 0..*gap {

                let mut index_pointer = i;

                while index_pointer < array.len() {
                    let min_index = get_min(index_pointer, *gap, &array);
                    array.swap(index_pointer, min_index);
                    index_pointer += *gap;
                }
            }
        }
    }

    fn get_min<T: PartialOrd>(i: usize, gap: usize, array: &[T]) -> usize {

        let mut min_index = i;
        let mut current_min = &array[i];
        let mut j = i + gap;

        while j < array.len(){
            if array[j] < *current_min {
                current_min = &array[j];
                min_index = j;
            }
            j += gap;
        }
        min_index
    }
}


