use super::*;
use std::fmt::Debug;

pub fn check_sort<T, F>(x: &[T], sort: F)
    where T: Ord + Clone + Debug,
          F: Fn(&mut [T]) {

    let mut v = x.to_vec();
    shuffle(&mut v);
    sort(&mut v);

    assert_eq!(x.to_vec(), v);
}

pub fn check_shellsort<T>(x: &[T], gaps: &[usize])
    where T: Ord + Clone + Debug {

    let mut v = x.to_vec();
    shuffle(&mut v);
    shell::sort(&mut v, gaps);
    assert_eq!(x.to_vec(), v);
}

#[test]
pub fn check_sorts() {

    let v_int1 = vec![4, 7, 7, 8, 9, 11, 14, 15, 16, 17, 18, 18, 21, 22, 23, 23, 25,
        25, 28, 28, 29, 30, 47, 53, 62, 69, 83, 86, 95];
    let v_int2: Vec<usize> = (0..100).collect();
    let v_string = vec!["apple", "banana", "carrot", "d", "deer", "zebra"];
    let v_char = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

    check_sort(&v_int1, selection::sort);
    check_sort(&v_int2, selection::sort);
    check_sort(&v_string, selection::sort);
    check_sort(&v_char, selection::sort);

    check_sort(&v_int1, insertion::sort);
    check_sort(&v_int2, insertion::sort);
    check_sort(&v_string, insertion::sort);
    check_sort(&v_char, insertion::sort);

    check_sort(&v_int1, merge::sort);
    check_sort(&v_int2, merge::sort);
    check_sort(&v_string, merge::sort);
    check_sort(&v_char, merge::sort);

    check_sort(&v_int2, merge::bottomsup_sort);
    check_sort(&v_int2, merge::bottomsup_sort);
    check_sort(&v_string, merge::bottomsup_sort);
    check_sort(&v_char, merge::bottomsup_sort);

    let gaps = vec![701, 301, 132, 57, 23, 10, 4, 1];
    check_shellsort(&v_int1, &gaps);
    check_shellsort(&v_int2, &gaps);
    check_shellsort(&v_string, &gaps);
    check_shellsort(&v_char, &gaps);
}



