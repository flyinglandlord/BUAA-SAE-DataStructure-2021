def lson(data, now):
    if now*2 + 1 >= len(data):
        return None
    if data[now*2 + 1] == "None":
        return None
    return data[now*2 + 1]


def rson(data, now):
    if now*2 + 2 >= len(data):
        return None
    if data[now*2 + 2] == "None":
        return None
    return data[now*2 + 2]

ans = 0
k = 0

def get_ans(data, now, depth) -> int:
    ans = 0
    if now >= len(data):
        return 0
    # print(data[now])
    if depth == k and data[now] != "None":
        ans += int(data[now])
    return ans + get_ans(data, now*2+1, depth+1) + get_ans(data, now*2+2, depth+1)


def input_node() -> list:
    data = input().strip().split()
    return data


if __name__ == '__main__':
    data = input_node()
    k = int(input())
    res_1 = get_ans(data, 0, 1)
    print(res_1)
