meals = [0, 3, 5, -5, 100, -8, -9]
guests = 3
l = 0


def sum_all(sub_lists):
    result = 0
    for sub_list in sub_lists:
        for elem in sub_list:
            result = result + elem
    return result

def result_in_range(start_pos, end_pos):
    for i in range(start_pos, end_pos):
        for k in range(i, end_pos + 1):
            for elem in meals[i:k]:
                current_sum = result + elem
            if result < current_sum:
                result = current_sum
    return result

def main():
    meals_num = len(meals)
    result = 0
    start = 0
    while start < len(meals):
        try:
            end = meals.index(item, start + 1)
        except ValueError:
            end = len(meals)
        result.extend(meals[x + start:x + start + size] for x in range(end - start - size + 1))
        start = end + 1
    for guest in range(0, guests + 1):
        current_result = 0


    for i in range(0, meals_num):
        for k in range(i, meals_num + 1):
            current_sum = sum_all([meals[i:k]])
            if result < current_sum:
                result = current_sum

    print(result)


if __name__ == "__main__":
        main()
