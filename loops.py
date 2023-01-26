# check even numbers

def checkEvenNumbers(start: int, end: int) -> int:
    count = 0
    for i in range(start, end):
        if i % 2 == 0:
            count += 1
    return count


countOfEvenNumbers = checkEvenNumbers(2, 10)

print(countOfEvenNumbers)
