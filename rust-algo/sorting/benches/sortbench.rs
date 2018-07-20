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

    static ref NUMBERS: Vec<usize> = largedata::random_numbers(3000, 100);
    static ref STRINGS: Vec<String> = largedata::random_strings(3000);
    static ref GAPS: Vec<usize> = vec![701, 301, 132, 57, 23, 10, 4, 1];
}

//----------------------------------------------------------------------------

fn numbers_bench(c: &mut Criterion) {

    c.bench_function("> NUMBERS: Selection Sort", move |b| {
        b.iter(|| selection::sort(&mut NUMBERS.clone()))
    });

    c.bench_function("> NUMBERS: Insertion Sort", move |b| {
        b.iter(|| insertion::sort(&mut NUMBERS.clone()))
    });

    c.bench_function("> NUMBERS: Shell Sort", move |b| {
        b.iter(|| shell::sort(&mut NUMBERS.clone(), &GAPS))
    });

    c.bench_function("> NUMBERS: Merge Sort", move |b| {
        b.iter(|| merge::sort(&mut NUMBERS.clone()))
    });

    c.bench_function("> NUMBERS: Merge Bottomsup Sort", move |b| {
        b.iter(|| merge::bottomsup_sort(&mut NUMBERS.clone()))
    });

    c.bench_function("> NUMBERS: Quick Sort", move |b| {
        b.iter(|| quick::sort(&mut NUMBERS.clone()))
    });

    c.bench_function("> NUMBERS: Improved Quick Sort", move |b| {
        b.iter(|| quick::improved_sort(&mut NUMBERS.clone()))
    });
}



//----------------------------------------------------------------------------

fn unique_numbers_bench(c: &mut Criterion) {

    c.bench_function("> UNIQUE NUMBERS: Selection Sort", move |b| {
        b.iter(|| selection::sort(&mut UNIQUE_NUMBERS.clone()))
    });

    c.bench_function("> UNIQUE NUMBERS: Insertion Sort", move |b| {
        b.iter(|| insertion::sort(&mut UNIQUE_NUMBERS.clone()))
    });

    c.bench_function("> UNIQUE NUMBERS: Shell Sort", move |b| {
        b.iter(|| shell::sort(&mut UNIQUE_NUMBERS.clone(), &GAPS))
    });

    c.bench_function("> UNIQUE NUMBERS: Merge Sort", move |b| {
        b.iter(|| merge::sort(&mut UNIQUE_NUMBERS.clone()))
    });

    c.bench_function("> UNIQUE NUMBERS: Merge Bottomsup Sort", move |b| {
        b.iter(|| merge::bottomsup_sort(&mut UNIQUE_NUMBERS.clone()))
    });

    c.bench_function("> UNIQUE NUMBERS: Quick Sort", move |b| {
        b.iter(|| quick::sort_recurse(&mut UNIQUE_NUMBERS.clone()))
    });

    c.bench_function("> UNIQUE NUMBERS: Improved Quick Sort", move |b| {
        b.iter(|| quick::improved_sort(&mut UNIQUE_NUMBERS.clone()))
    });
}

//----------------------------------------------------------------------------

fn strings_bench(c: &mut Criterion) {

    c.bench_function("> STRINGS: Selection Sort", move |b| {
        b.iter(|| selection::sort(&mut STRINGS.clone()))
    });

    c.bench_function("> STRINGS: Insertion Sort", move |b| {
        b.iter(|| insertion::sort(&mut STRINGS.clone()))
    });

    c.bench_function("> STRINGS: Shell Sort", move |b| {
        b.iter(|| shell::sort(&mut STRINGS.clone(), &GAPS))
    });

    c.bench_function("> STRINGS: Merge Sort", move |b| {
        b.iter(|| merge::sort(&mut STRINGS.clone()))
    });

    c.bench_function("> STRINGS: Merge Bottomsup Sort", move |b| {
        b.iter(|| merge::bottomsup_sort(&mut STRINGS.clone()))
    });


    c.bench_function("> STRINGS: Quick Sort", move |b| {
        b.iter(|| quick::sort(&mut STRINGS.clone()))
    });

    c.bench_function("> STRINGS: Improved Quick Sort", move |b| {
        b.iter(|| quick::improved_sort(&mut STRINGS.clone()))
    });
}


fn shuffle_bench(c: &mut Criterion) {

    c.bench_function("> UNIQUE_NUMBERS: Shuffle 1", move |b| {
        b.iter(|| shuffle(&mut UNIQUE_NUMBERS.clone()))
    });

    c.bench_function("> NUMBERS: Shuffle 1", move |b| {
        b.iter(|| shuffle(&mut NUMBERS.clone()))
    });

    c.bench_function("> STRINGS: Shuffle 1", move |b| {
        b.iter(|| shuffle(&mut STRINGS.clone()))
    });

    c.bench_function("> UNIQUE_NUMBERS: Shuffle 2", move |b| {
        b.iter(|| thread_rng().shuffle(&mut UNIQUE_NUMBERS.clone()))
    });

    c.bench_function("> NUMBERS: Shuffle 2", move |b| {
        b.iter(|| thread_rng().shuffle(&mut NUMBERS.clone()))
    });

    c.bench_function("> STRINGS: Shuffle 2", move |b| {
        b.iter(|| thread_rng().shuffle(&mut STRINGS.clone()))
    });
}

fn clone_bench(c: &mut Criterion) {

    c.bench_function("> UNIQUE_NUMBERS: clone", move |b| {
        b.iter(|| UNIQUE_NUMBERS.clone())
    });

    c.bench_function("> NUMBERS: clone", move |b| {
        b.iter(|| NUMBERS.clone())
    });

    c.bench_function("> STRINGS: clone", move |b| {
        b.iter(|| STRINGS.clone())
    });
}

//----------------------------------------------------------------------------

criterion_group!(benches, numbers_bench, unique_numbers_bench, strings_bench, shuffle_bench, clone_bench);
criterion_main!(benches);
