def solution(input):
    left = input[0]
    right = sum(input[1:])
    min_delta = abs(left - right)
    if len(input) == 2:
        return min_delta

    for x in range(1, len(input)-1):
        left += input[x]
        right -= input[x]
        new_delta = abs(left - right)

        if new_delta < min_delta:
            min_delta = new_delta
    return min_delta


if __name__ == '__main__':
    solution()
