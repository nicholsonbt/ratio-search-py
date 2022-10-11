import random, searches

def getArray(maximumValue, maxValueCount):
    # Generate 'maxValueCount' random numbers between 0 and 'maximumValue'.
    values = [random.randrange(0, maximumValue) for i in range(maxValueCount)]

    # Remove duplicate values.
    unique_values = list(set(values))

    # Return a sorted list of the unique values.
    return sorted(unique_values)

# The maximumValue should be at least as large as maxValueCount, so as to
# reduce the number of duplicate values.
maximumValue = 100000000
maxValueCount = 1000000

# Generate an ordered array of at most maxValueCount values between
# 0 and maximumValue.
print("Generating array...")
arr = getArray(maximumValue, maxValueCount)
print("Array generated.")

# Get the length of the array
n = len(arr)

# Set the number of values to search for.
reps = 100000

# Initialise the recursion count values.
aRecCount = 0
bRecCount = 0

# Repeatedly attempt to find a randomly generated value in the array
# using both binary search and ratio search, and print the number
# of recursions required on average for each.
for i in range(reps):

    # Generate a value to search for.
    value = random.randrange(0, maximumValue)

    # Generate the initial ratio value.
    k = (value - arr[0]) / (arr[n - 1] - arr[0])

    # Try to find the value using both algorithms.
    aVal, aRecs = searches.binarySearch(arr, 0, n - 1, value)
    bVal, bRecs = searches.ratioSearch(arr, 0, n - 1, k, value)

    # Sum the number of recursions required for each algorithm.
    aRecCount += aRecs
    bRecCount += bRecs

# Output the results.
print("Out of " + str(reps) + " repetitions, A averaged " +
      str(aRecCount / reps) + " recursions, and B " + str(bRecCount / reps) +
      " with an ordered array of " + str(n) + " unique values.")
