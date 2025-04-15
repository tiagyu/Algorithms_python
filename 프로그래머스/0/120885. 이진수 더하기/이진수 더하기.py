def solution(bin1, bin2):
    bin_list = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9, 2**10]

    bin1_split = list(map(int,bin1))
    bin2_split = list(map(int,bin2))

    bin1_split.reverse()
    bin2_split.reverse()

    bin1_value = 0
    bin2_value = 0

    for i in range(len(bin1)):
        bin1_value += bin_list[i] * bin1_split[i]

    for i in range(len(bin2)):
        bin2_value += bin_list[i] * bin2_split[i]

    answer = bin1_value + bin2_value
    return bin(answer)[2:]