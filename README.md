# ratio-search-py
An experiment to compare the binary search algorithm against a 'weighted' binary search algorithm.

## Introduction:
I predict that for very large, uniformly distributed, ordered lists a search algorithm that calculates the expected location of the target value will on average be quicker than a binary search.

I will explore this by testing both algorithms against a range of arrays. I will vary:
 - The number of elements in the array,
 - The maximum possible values of elements in the array,
 - The distribution of elements (both clumping of values and skewing of them),
 
For this experiment, I will assume that:
 - All values are greater than or equal to 0,
 - The array is ordered,
 - All values are unique,


## Initial Experiment:
A basic initial experiment shows that, for very large arrays of ordered, uniformly distributed numbers, the 'ratio search' (I haven't yet found any examples of this variant of the binary search algorithm so will call it as such for now) I implemented requires far fewer recursions than a typical binary search.

Given an array of ~1,000,000 unique values the binary search required an average of 20.9 recursions whilst the ratio search required only 4.7! These results were calculated using 100,000 randomly generated values, of which ~1% were in the array.

There are many areas in which I can improve upon this experiment. However, it seems likely that under the conditions expressed in the introductory paragraph, this ratio sort algorithm may be more efficient (on average) than a traditional binary search. That said, it will take far longer in the worst case, and requires added complexity in each recursion - having to calculate a new expected position - that may increase the time taken more than expected, even if fewer recursions are required.
