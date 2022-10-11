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
