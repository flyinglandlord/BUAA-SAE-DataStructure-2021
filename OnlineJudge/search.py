def get_val(arr, i):
    if 0 <= i < len(arr):
        return arr[i]
    else:
        return None

if __name__ == '__main__':
    read = input().strip().split()
    list = [int(x) for x in read]
    length = len(list)-1
    if length == 0:
        print(list[0])
        exit(0)
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        # length = (length) // 2
        print(length, mid, list[mid])
        if mid != 0 and mid != len(list) - 1:
            if list[mid-1] == list[mid]:
                if mid % 2 == 0:
                    high = mid - 2
                else:
                    low = mid + 1
            elif list[mid] == list[mid+1]:
                if mid % 2 == 0:
                    low = mid + 2
                else:
                    high = mid - 1
            else:
                print(list[mid])
                exit(0)
        elif mid == 0:
            if list[mid] == list[mid+1]:
                low = 2
            else:
                print(list[mid])
                exit(0)
        elif mid == len(list) - 1:
            if list[mid] == list[mid-1]:
                high = len(list)-2
            else:
                print(list[mid])
                exit(0)
    print(-1)

