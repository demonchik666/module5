def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0: # Base case for <= 0
            return 0
        elif n == 1: # Base case for 1
            return 1
        if n in cache: # Check if result is already cached
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)# Recursive case
        return cache[n] # Store result in cache
    return fibonacci

nums = range(1, 50)
nums1 = nums[::-1]
for num in nums1:
    print(caching_fibonacci()(num))