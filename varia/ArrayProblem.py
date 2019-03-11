int_list = [-22, 555, -2, -1, 99999999999999, -99]


def change_int_list(int_list):
    e = 0
    for i in int_list:
        if int_list[e] < 0:
            int_list[e] = i * -1
        e = e + 1

        print(int_list)


def find_int_same_sign(int_list):
    result = []
    negative = int_list[0] <= 0
    result.append(int_list[0])
    for i in int_list:
        if negative and i <= 0:
            result.append(i)
        if not negative and i > 0:
            result.append(i)

        if (negative and i > 0) or (not negative and i <= 0):
            break

    return result


if __name__ == "__main__":
    # change_int_list(int_list)
    print(find_int_same_sign(int_list))