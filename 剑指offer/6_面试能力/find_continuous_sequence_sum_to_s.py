"""
面试题41 和为s的两个数字VS和为s的连续正数序列

和为S的连续正数序列

题目描述：
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:

输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

解题方法
上题是求，和为S的两个数字。这个题变成了和为S的连续子序列。
其实做法类似。这个题使用了两个指针small 和 big，也是将两个指针根据和的条件进行右移的过程。

和为s的连续整数序列
要求：输入一个正数s， 打印出所有和为s的正整数序列(至少两个数)

思路: 使用两个指针，和比s小，大指针后移，比s大，小指针后移

"""


def sum_to_s(s):
    a, b = 1, 2
    ret = []
    while a < s / 2 + 1:
        if sum(range(a, b+1)) == s:
            ret.append(range(a, b+1))
            a += 1
        elif sum(range(a, b+1)) < s:
            b += 1
        else:
            a += 1
    return ret
