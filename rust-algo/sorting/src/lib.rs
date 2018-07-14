extern crate rand;
use rand::{thread_rng, Rng};

#[cfg(test)]
pub mod tests;

pub fn shuffle<T: Ord>(v: &mut [T]) {

    let mut rng = thread_rng();
    for i in 0.. v.len() {
        let r = rng.gen_range(0, i + 1);
        v.swap(i, r);
    }
}

pub mod merge {
    use std::fmt::Debug;

    fn merge<T: Ord + Debug + Clone>(array: &mut [T], aux: &mut [T], lo: usize, mid: usize, hi: usize) {

        let mut i = lo;
        let mut j = mid + 1;

        for x in lo..=hi {
            aux[x] = array[x].clone();
        }

        for x in lo..=hi {

            if i > mid {
                array[x] = aux[j].clone();
                j+=1;
            } else if j > hi {
                array[x] = aux[i].clone();
                i+=1;
            } else if aux[j] >= aux[i] {
                array[x] = aux[i].clone();
                i+=1;
            } else {
                array[x] = aux[j].clone();
                j+=1;
            }
        }
        //println!("merge: {}, {} = {:?}", lo, hi, &array[lo..=hi]);
    }

    fn sort_recurse<T: Ord + Debug + Clone>(array: &mut [T], aux: &mut [T], lo: usize, hi: usize) {
        //println!("sort: {}, {}", lo, hi);
        if hi <= lo { return; }

        let mid = lo + (hi - lo) / 2;
        sort_recurse(array, aux, lo, mid);
        sort_recurse(array, aux, mid + 1, hi);
        merge(array, aux, lo, mid, hi);
    }

    pub fn sort<T: Ord + Debug + Clone>(array: &mut [T]) {

        let mut aux = Vec::new();

        for i in 0..array.len() {
            aux.push(array[i].clone());
        }

        let hi = array.len() - 1;
        sort_recurse(array, &mut aux, 0, hi);
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


