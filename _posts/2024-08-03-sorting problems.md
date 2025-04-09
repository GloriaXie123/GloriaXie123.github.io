---
layout: post
tags: [Algorithm,]
---

## Sorting problems

### The rules for sorting
We want to sort collections of data of different types, that means we want our algorithm to be general enough so we don't have to modify our algorithm for specific data type, that's why we need **callback**.

In java we implement **callback** by including **comparable** interface in each object's class, all the **comparable** interface has to implement the **comapreTo** method.

the **binary relation <=** has to satisfy:

Antisymmetry;

Transitivity;

Totality;

### Elementary sorting algorithms

1) Selection sort, each selection round takes O(n) time complexity.

2) Insertion sort, move entries only once a time.

3) Shell sort, move entries more than one position at a time, that's how it gives efficiency.

### Application of sorting

#### Shuffle

Using **Knuth's shuffling** to shuffle a deck of poker cards.

Implementation of **Knuth's shuffling**:

In ith iteration, pick a random number r between 0 and i, and then swap ith entry and rth entry.

#### Randomness is important

there is a quote " the generation of randomness is too important to be left to chance".

### Merge sort and Quick sort

These two algorithms are classic sorting algorithms, they take at most nlgn compares.


By comparing the efficiency of different algorithms, we realize that good algorithms are much better than spending a lot of time and money to use a bad one.






