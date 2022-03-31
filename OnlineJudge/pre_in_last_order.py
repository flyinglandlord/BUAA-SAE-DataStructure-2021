def solve(preorder, inorder, pre_now, in_l, in_r):
    if in_l > in_r:
        return
    i = in_l
    while i <= in_r:
        if inorder[i] == preorder[pre_now]:
            len_l = i - in_l
            solve(preorder, inorder, pre_now+1, in_l, i-1)
            solve(preorder, inorder, pre_now+len_l+1, i+1, in_r)
            break
        i += 1
    print(preorder[pre_now], end=' ')


if __name__ == '__main__':
    preorder = input().strip().split()
    inorder = input().strip().split()
    solve(preorder, inorder, 0, 0, len(inorder)-1)