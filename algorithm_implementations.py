import random


def perform_bubble_sort(item_count):
    numbers = [random.randint(1, 1000) for _ in range(item_count)]

    for i in range(item_count):
        for j in range(0, item_count - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def perform_linear_search(item_count):
    items = list(range(item_count))
    target = item_count

    for item in items:
        if item == target:
            return True
    return False


def perform_binary_search(item_count):
    items = list(range(item_count))
    target = item_count // 2

    left = 0
    right = item_count - 1

    while left <= right:
        middle = (left + right) // 2
        if items[middle] == target:
            return True
        elif items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False


def perform_nested_loop(item_count):
    total = 0
    for i in range(item_count):
        for j in range(item_count):
            total += i + j
    return total


def perform_exponential_operation(item_count):
    safe_limit = min(item_count, 20)
    result = 0
    for i in range(2 ** safe_limit):
        result += i % 100
    return result


def get_algorithm_function(algorithm_name):
    algorithms = {
        'bubble': perform_bubble_sort,
        'linear': perform_linear_search,
        'binary': perform_binary_search,
        'nested': perform_nested_loop,
        'exponential': perform_exponential_operation
    }
    return algorithms.get(algorithm_name)


def get_time_complexity(algorithm_name):
    complexities = {
        'bubble': 'O(n²)',
        'linear': 'O(n)',
        'binary': 'O(log n)',
        'nested': 'O(n²)',
        'exponential': 'O(2ⁿ)'
    }
    return complexities.get(algorithm_name, 'Unknown')
