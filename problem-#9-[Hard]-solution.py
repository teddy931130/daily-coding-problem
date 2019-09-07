# Function to return max sum such that
# no two elements are adjacent


def find_max_sum(nums):
    include = 0  # max sum including the previous element
    exclude = 0  # max sum excluding the previous element

    for num in nums:
        # Current max excluding num (No ternary in Python)
        new_exclude = exclude if exclude > include else include

        # Current max including num
        include = exclude + num
        exclude = new_exclude

        # return max of incl and excl
    return exclude if exclude > include else include


numbers = [2, 4, 6, 2, 5, 8]
print(find_max_sum(numbers))
