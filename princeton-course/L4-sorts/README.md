# TODO:
- Reimplement common sorts in rust!
- IMPLEMENT 3-WAY QUICKSORT
- Implement merge sorts with improvements!
- Write a program that solves the convex hull problem in rust!
- Add pictures in this document
- Add more writeupt details for 3-way quicksort

# Contents

## Basic Sorting Algorithms
- Elementary Sorts
  - Selection Sort
  - Insertion Sort
  - Shell sort
- Merge Sort
  - (recursive version + bottoms up version)
- Quick Sort (with improvements)
- Three-way Quick Sort
  - (better for most applications particularly duplicate keys)

## Important Concepts
- Convex hull problem
- Shuffling
- Stability
- Selection (Find Kth Largest)
- Duplicate Keys

# Elementary Sorts

## Selection Sort
- works by repeatedly selecting the smallest remaining item
```

IDEA:
- First, find the smallest item in the array, and exchange it with the first entry.
- Then, find the next smallest item and exchange it with the second entry.
- Continue in this way until the entire array is sorted.
```
- `O(n*n)` comparisions `O(n)` swaps (best, worst and average case)

## Insertion sort
```
IDEA:
The algorithm that people often use to sort bridge hands is to consider the cards one at a time, inserting each into its proper place among those already considered (keeping them sorted).
```
- worst case and average case: `O(n*n)` comparisons and swaps
- best case: `O(n)` comparision, `O(1)` swaps
- BEST CASE: If array is already sorted, `N-1` compares, `O` exchanges
- WORSE CASE: about `1/2 n*n` compares and exchanges
```
Advantages:

- Adaptive
i.e., efficient for data sets that are already substantially sorted: the time complexity is O(nk) when each element in the input is no more than k places away from its sorted position

- Simple implementation
Jon Bentley shows a three-line C version, and a five-line optimized version[2]

- Efficient for (quite) small data sets
much like other quadratic sorting algorithms More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort

- Stable
i.e., does not change the relative order of elements with equal keys

- In-place
i.e., only requires a constant amount O(1) of additional memory space

- Online
i.e., can sort a list as it receives it

```

## Shell-sort
```
IDEA: Move entries more than one position at a time by
h-sorting the array.

h-sort: insertion sort with stride length h

- A x-sorted array remains x-sorted after y-sorting it
```
- Fast unless array size is huge, tiny fixed footprint for code, used in some embedded systems
- Worst case `O(n log squared (n))` given best known gap sequence
(Pratt, Vaughan Ronald (1979). Shellsort and Sorting Networks (Outstanding Dissertations in the Computer Sciences). Garland. ISBN 0-8240-4406-1.)
- Best-case O(n log n), average depends on gap sequence
```
Too few gaps slows down the passes, and too many gaps produces an overhead.

NOT STABLE: it may change the relative order of elements with equal values.

ADAPTIVE: in that it executes faster when the input is partially sorted.
```

# Merge Sort
## Important that you know! How to merge? With Auxillary array?
```
IDEA: (recursive)
- Divide array into two halves
- recursively sort each half
- merge two halves

PRACTICAL IMPROVEMENTS:

1. Mergesort has too much overhead for tiny subarrays cut off to insertion sort for about 7 items

2. Stop if already sorted! Helps for partially-ordered arrays
Is biggest item in first half <= smallest item in second half?

3. Eliminate the copy to the auxiliary array
Save time by switching the role of the input and auxiliary array
at each recursive call.


Bottom-up mergesort (non-recursive)
- Pass through array merge subarrays of size 2
- Repeat for subarrays size 4, 8, 16 ...
About 10% slower than recursive?
```
- Divide and conquer!
- Worst, best and average case `O(n log n)`
- Has a recursive implementation and bottoms up representation
- recursive implementation might cause stack overflow so it's better to use bottoms up approach!
- This is not in-place sorting! You have to have an auxillary array, uses extra space proportional to n to merge two sub arrays
- STABLE
- PARALLELIZABLE: Can have a parallelized merge algorithm for multiple cores

# Quick Sort!
## Important that you know! How to partition??
```
IDEA:
1. Shuffle the array
2. Partition such that for the pivot point j
- entry a[j] is in the correct place
- no larger entry to the left of j
- no smaller entry to the right of j
3. Sort left and right of j recursively

How to partition?
Repeat unti i and j pointers cross
- scan i from left to right as long as a[i] < a[pivot]
- scan j from right to left as long as a[j] > a[pivot]
- Exchange a[i] with a[j]

```
- Divide and conquer!
- Many small tweaks that from the original quicksort algorithm can be used to improve its performance!
- If implemented well, it's two or three times faster than its main competitors merge sort and heap sort
- Worst-case `O(n*n)` when already sorted, so shuffle first
- Best case and average `O(n log n)` when you shuffle first before sorting
- NOT STABLE
- IN PLACE SORTING ALGORITHM!
- IMPORTANT: SHUFFLING IS NEEDED FOR PERFORMANE GUARANTEE
- IMPORTANT: When duplicates are present, it is (counter intuitively) better to stop on keys equal to the partitioning item's key
- Can be parallelized!
- On average 39% ore compares than merge sort but it's faster than mergesort because of less data movement
- IMPORTANT: Many textbook implementations go quadratic if array is sorted or reverse sorted, or if it has many DUPLICATES (even if randomized)
```
PRACTICAL IMPROVEMENTS:

1. Insertion sort small subarrays
- Quicksort has too much overhead for tiny subarrays
-Cutoff to insertion sort for 10-15 items


What pivot to use?
- median of 3 random items
```

# 3-WAY PARTITIONING QUICKSORT
- Important to sort items with many duplicate keys!
- DUTCH NATIONAL FLAG PROBLEM [Edsger Dijkstra]
## TODO: Write more notes about this!

# Shuffling
- Make sure the array is randomized!
- See: Knuth Shuffle or Fisher Yates Shuffle
- Linear time
```
IDEA:
- scan pointer i from left to right
- in iteration i, pick integer r between 0 and i
uniformly at random then swap a[i] and a[r]
```

# Computational Complexity
- Framework to study efficiency of algorithms for solving a particular problem x.

- MODEL OF COMPUTATION
  - Allowable operations

- COST MODEL
  - Operation count(s)

- UPPERBOUND
  - you are sure that at least one algorithm has this as its worst case in terms of big-oh performance

- LOWERBOUND
  - You are sure that all algorithms will not perform better than this

- OPTIMAL ALGOIRTHM
  - You are sure that this is the best algorithm based on the cost model

```
Example: Sorting
Model of computation:
- decision tree, can access information only thru compares
- height of the decision tree is the worst-case number of compares

Cost model: number of compares
Upperbound: ~N lg N (mergesort)
Lowerbound: N lg N
Optimal algorithm: mergesort
```
- Merge sort is optimal with respect to number of compares
- Merge sort is NOT optimal with respect to space usage
- Computational complexity is based on context
- Lowerbound may not hold if it has some prior information example
```
Partially-ordered arrays
- insertion sort requires only N - 1 compares if input array is sorted

Duplicate Keys
- we may not need N lg N compares
- Stay tuned for quicksort

Digital properties of keys
- we can use digit/character compares instead of key compares
for numbers and strings
- Stay tuned for radix sort
```

# Stability
- Example: First sort by name, then sort by section (student)
- Example: Sort bby time then sort by location (airplane)
- Sort preserves the relative order of items with equal keys
- insertion sort and merge sort are stable.
- selection sort or shellsort are not stable

# Selection
- Given an array of N items, find a kth smallest item
- Minimum number k = 0
- Maximum number k = N
- Median number k = N / 2
```
QUICK SELECT
- takes linear time on average

IDEA:

Partition array so that:
- Entry a[j] is in place
- no large entry to the left of j
- no smaller entry to the right of j

Repeat in one subarray, depending on j
finished when j = k
```
- There exists a compare-based selection algorithm whose worst-case running time is linear, but constants are too high so not used in practice

# Duplicate Keys
- When there are many duplicate keys, use 3-way partition quicksort

# Convex Hull
- Cool problem! Please see slides for more information
