int_list = [-20, 50, 4874897498, - 4776776757, -43578943, 45, 67, -98]





def find_int_same_sign(int_list):
    result = []
    e = 2
    negative = int_list[e] > 0
    positive = int_list[e] < 0
    result.append(int_list)
    for i in int_list:
        if negative and i <= 0:
            i = i * -1
            result.append(i)
            print('neg')
        else:
            result.append(i)
            print('pos')

        e = e + 1

    return result


if __name__ == "__main__":
    # change_int_list(int_list)
    print(find_int_same_sign(int_list))
