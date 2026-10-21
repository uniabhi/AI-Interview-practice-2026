# import cProfile

# def calculate_squares(numbers):
#     result = []

#     for number in numbers:
#         result.append( number * number)

#     return result

# numbers = list(range(1_000_000))

# cProfile.run("calculate_squares(numbers)")

# import timeit
# print(timeit.timeit("calculate_squares(numbers)", globals=globals(), number=5))


import cProfile
import timeit

def calculate_squares_old(numbers):
    result = []

    for n in numbers:
        result.append(n * n)
    return result


## new version 
def calculate_squares(numbers):
    return [n * n for n in numbers]

numbers = list(range(1_000_000))

# 1) Profiler से देखें
print("=== OLD (append) ===")
cProfile.run("calculate_squares_old(numbers)")

print("=== NEW (list comprehension) ===")
cProfile.run("calculate_squares(numbers)")

# 2) असली speed नापें (profiler के overhead के बिना)
old_time = timeit.timeit(lambda: calculate_squares_old(numbers), number=5)
new_time = timeit.timeit(lambda: calculate_squares(numbers), number=5)

print(f"Old (append)          : {old_time:.3f} sec")
print(f"New (list comprehension): {new_time:.3f} sec")
print(f"Speedup               : {old_time / new_time:.2f}x faster")