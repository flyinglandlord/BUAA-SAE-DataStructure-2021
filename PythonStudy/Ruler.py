"""
Draw an English ruler
这可以出一道OJ题目了呢...
"""


def draw_line(length, label=''):
    """
    划线用

    :param length: 要画线的长度
    :param label: 在线的右侧需要加入的标签
    :return: 无
    """
    line = '-' * length
    print(line + ' ' + label)


def draw(length, size, add):
    """
    利用递归绘制尺子的主体部分

    :param length: 当前需要绘制的'-'的个数
    :param size: 当前这一段的长度
    :param add: 在这一段之前的尺子的长度
    :return: 无
    """
    if length >= 1:
        draw(length - 1, size/2, add)
        draw_line(length, str(add + size/2))
        draw(length - 1, size/2, add + size/2)


def draw_ruler(length, acc):
    draw_line(acc, '0')
    for i in range(length):
        draw(acc - 1, 1, i)
        draw_line(acc, str(i + 1))


draw_ruler(1, 5)
