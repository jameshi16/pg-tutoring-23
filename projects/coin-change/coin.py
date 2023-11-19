def coin_change(denominators: [int], value: int) -> int:
    denominators.sort()
    accum = [0] * (value + 1)

    # there is only 1 way to make a 0; that's with no coins
    accum[0] = 1

    for coin in denominators:
        for ind, val in enumerate(accum):
            if ind == 0:
                continue

            if ind >= coin:
                accum[ind] += accum[ind - coin]
            else:
                accum[ind] = max(accum[ind - 1], val)

    return accum[-1]

if __name__ == '__main__':
    print('N=8', coin_change([1,5,10], 8))
    print('N=10', coin_change([1,5,10], 10))
    print('N=12', coin_change([1,5,10], 12))
    print('Different denoms, N=5', coin_change([1,2,3,5,7], 5))
