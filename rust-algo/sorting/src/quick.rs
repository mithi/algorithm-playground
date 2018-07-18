use std::fmt::Debug;
use super::*;


pub fn sort<T: Ord + Debug + Clone>(array: &mut [T]) {
    shuffle(array);
    sort_recurse(array);
}


pub fn improved_sort<T: Ord + Debug + Clone>(array: &mut [T]) {
    shuffle(array);
    improved_sort_recurse(array);
}


pub fn median_trick<T: Ord + Debug + Clone> (array: &mut [T]) {
    let mid = array.len() / 2;
    let last = array.len() - 1;

    if array[mid] < array[last] {

        if array[0] <= array[mid] {
            array.swap(0, mid);
        } else if array[last] <= array[0] {
            array.swap(0, last);
        }

    } else {

        if array[0] >= array[mid] {
            array.swap(0, mid);
        } else if array[last] >= array[0] {
            array.swap(0, last);
        }
    }
}


pub fn improved_sort_recurse<T: Ord + Debug + Clone> (array: &mut [T]) {

    if array.len() <= 20 {
        insertion::sort(array);
        return;
    }

    median_trick(array);
    let hi = array.len() - 1;
    let pivot = partition(array, 0, hi);
    improved_sort_recurse(&mut array[0..pivot]);
    improved_sort_recurse(&mut array[(pivot+1)..]);

}


pub fn sort_recurse<T: Ord + Debug + Clone>(array: &mut [T]) {

    if array.len() <= 1 { return; }
    let hi = array.len() - 1;
    let pivot = partition(array, 0, hi);
    sort_recurse(&mut array[0..pivot]);
    sort_recurse(&mut array[(pivot + 1)..]);
}


fn partition<T: Ord + Debug + Clone>(array: &mut [T], mut left: usize, mut right: usize) -> usize {

    loop {
        while array[left] < array[0] {
            left+=1;
            if left == right { break; }
        }

        while array[right] >= array[0] {
            right-=1;
            if right == 0 { break; }
        }

        if left >= right {
            array.swap(0, right);
            return right;
        }

        array.swap(left, right)
    }
}
