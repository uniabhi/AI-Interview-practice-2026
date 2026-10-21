def find_max(numbers):
    if not numbers:
        raise ValueError("list is empty")

    biggest = numbers[0]
    for n in numbers[1:]:
        if n > biggest:
            biggest = n
  
    return biggest


result = find_max([2, -7])
print(result)