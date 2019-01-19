


arr=[234,43243242523,62356235,14243533432]

def sort(arr):
    limit = len(arr) - 1
    for i in range(len(arr) - 1):
        fg = 0
        while fg < limit:
            limit = limit - 1
            if arr[fg] > arr[fg + 1]:

                temp = arr[fg]
                arr[fg] = arr[fg + 1]
                arr[fg + 1] = temp
                print(arr)



            fg = fg + 1





if __name__ == "__main__":
    sort(arr)