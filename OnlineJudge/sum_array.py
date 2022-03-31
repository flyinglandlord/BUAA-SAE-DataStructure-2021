if __name__ == '__main__':
    l = input().strip().split()
    data = [int(i) for i in l]
    n = int(input())

    sum = [0 for i in range(0, len(data)+1)]
    sum[0] = data[0]
    for i in range(1, len(data)):
        sum[i] = sum[i-1] + data[i]

    # print(sum)

    found = False
    for length in range(0, len(data)):
        for t in range(length+1, len(data)):
            if sum[t] - sum[t-length-1] >= n:
                print(length+1)
                found = True
                # print(data[t], data[t-length])
                break
        if found:
            break

    if not found:
        print("-1")