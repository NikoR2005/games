planes = [1, 3, 5]
mountains = [0, 0, 3, 5, 0, 0]




def main():

    for i in range(0, mountains.lenth() - 1):
        pass


    num_off_light = 0
    for plane in planes:
        for mountain in mountains:
            if plane >= mountain:
                print('ok')
                num_off_light += 1
                print(num_off_light)
            elif plane <= mountain:
                print(mountains)
                print('fail')
                print(num_off_light)


if __name__ == "__main__":
    main()
