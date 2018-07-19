#[macro_use]
extern crate lazy_static;

#[macro_use]
extern crate criterion;
use criterion::Criterion;

extern crate sorting;
use sorting::*;

extern crate rand;
use rand::{thread_rng, Rng};

lazy_static! {


    static ref UNIQUE_NUMBERS: Vec<usize> = {
        let mut array: Vec<usize> = (0..3000).collect();
        thread_rng().shuffle(&mut array);
        array
    };

    static ref NUMBERS: Vec<usize> = largedata::random_numbers(3000, 500);
    static ref STRINGS: Vec<String> = largedata::random_strings(3000);
    static ref GAPS: Vec<usize> = vec![701, 301, 132, 57, 23, 10, 4, 1];
}

//----------------------------------------------------------------------------

fn numbers_merge(c: &mut Criterion) {
    c.bench_function("> NUMBERS: Merge Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| merge::sort(&mut d))
    });
}

fn numbers_merge_bottomsup(c: &mut Criterion) {
    c.bench_function("> NUMBERS: Merge Bottomsup Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| merge::bottomsup_sort(&mut d))
    });
}

fn numbers_quick(c: &mut Criterion) {
    c.bench_function("> NUMBERS: Quick Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| quick::sort(&mut d))
    });
}

fn numbers_improved_quick(c: &mut Criterion) {
    c.bench_function("> NUMBERS: Improved Quick Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| quick::improved_sort(&mut d))
    });
}

fn numbers_insertion(c: &mut Criterion) {
    c.bench_function("> NUMBERS: Insertion Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| insertion::sort(&mut d))
    });
}

fn numbers_selection(c: &mut Criterion) {
    c.bench_function("> NUMBERS: Selection Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| selection::sort(&mut d))
    });
}

fn numbers_shell(c: &mut Criterion) {
    c.bench_function("> NUMBERS: Shell Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| shell::sort(&mut d, &GAPS))
    });
}

//----------------------------------------------------------------------------

fn unique_numbers_merge(c: &mut Criterion) {
    c.bench_function("> UNIQUE NUMBERS: Merge Sort", move |b| {
        let mut d = UNIQUE_NUMBERS.to_vec();
        b.iter(|| merge::sort(&mut d))
    });
}

fn unique_numbers_merge_bottomsup(c: &mut Criterion) {
    c.bench_function("> UNIQUE NUMBERS: Merge Bottomsup Sort", move |b| {
        let mut d = UNIQUE_NUMBERS.to_vec();
        b.iter(|| merge::bottomsup_sort(&mut d))
    });
}

fn unique_numbers_quick(c: &mut Criterion) {
    c.bench_function("> UNIQUE NUMBERS: Quick Sort", move |b| {
        let mut d = UNIQUE_NUMBERS.to_vec();
        b.iter(|| quick::sort(&mut d))
    });
}

fn unique_numbers_improved_quick(c: &mut Criterion) {
    c.bench_function("> UNIQUE NUMBERS: Improved Quick Sort", move |b| {
        let mut d = UNIQUE_NUMBERS.to_vec();
        b.iter(|| quick::improved_sort(&mut d))
    });
}

fn unique_numbers_insertion(c: &mut Criterion) {
    c.bench_function("> UNIQUE NUMBERS: Insertion Sort", move |b| {
        let mut d = UNIQUE_NUMBERS.to_vec();
        b.iter(|| insertion::sort(&mut d))
    });
}

fn unique_numbers_selection(c: &mut Criterion) {
    c.bench_function("> UNIQUE NUMBERS: Selection Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| selection::sort(&mut d))
    });
}

fn unique_numbers_shell(c: &mut Criterion) {
    c.bench_function("> UNIQUE NUMBERS: Shell Sort", move |b| {
        let mut d = NUMBERS.to_vec();
        b.iter(|| shell::sort(&mut d, &GAPS))
    });
}

//----------------------------------------------------------------------------

fn strings_merge(c: &mut Criterion) {
    c.bench_function("> STRINGS: Merge Sort", move |b| {
        let mut d = STRINGS.to_vec();
        b.iter(|| merge::sort(&mut d))
    });
}

fn strings_merge_bottomsup(c: &mut Criterion) {
    c.bench_function("> STRINGS: Merge Bottomsup Sort", move |b| {
        let mut d = STRINGS.to_vec();
        b.iter(|| merge::bottomsup_sort(&mut d))
    });
}

fn strings_quick(c: &mut Criterion) {
    c.bench_function("> STRINGS: Quick Sort", move |b| {
        let mut d = STRINGS.to_vec();
        b.iter(|| quick::sort(&mut d))
    });
}

fn strings_improved_quick(c: &mut Criterion) {
    c.bench_function("> STRINGS: Improved Quick Sort", move |b| {
        let mut d = STRINGS.to_vec();
        b.iter(|| quick::improved_sort(&mut d))
    });
}

fn strings_insertion(c: &mut Criterion) {
    c.bench_function("> STRINGS: Insertion Sort", move |b| {
        let mut d = STRINGS.to_vec();
        b.iter(|| insertion::sort(&mut d))
    });
}

fn strings_selection(c: &mut Criterion) {
    c.bench_function("> STRINGS: Selection Sort", move |b| {
        let mut d = STRINGS.to_vec();
        b.iter(|| selection::sort(&mut d))
    });
}

fn strings_shell(c: &mut Criterion) {
    c.bench_function("> STRINGS: Shell Sort", move |b| {
        let mut d = STRINGS.to_vec();
        b.iter(|| shell::sort(&mut d, &GAPS))
    });
}

//----------------------------------------------------------------------------

criterion_group!(numbers_benches,
    numbers_merge_bottomsup, numbers_merge,
    numbers_quick, numbers_improved_quick,
    numbers_selection, numbers_insertion,
    numbers_shell,
);

criterion_group!(unique_numbers_benches,
    unique_numbers_merge_bottomsup, unique_numbers_merge,
    unique_numbers_quick, unique_numbers_improved_quick,
    unique_numbers_selection, unique_numbers_insertion,
    unique_numbers_shell,
);

criterion_group!(strings_benches,
    strings_merge_bottomsup, strings_merge,
    strings_quick, strings_improved_quick,
    strings_selection, strings_insertion,
    strings_shell,
);

criterion_main!(numbers_benches, unique_numbers_benches, strings_benches);
