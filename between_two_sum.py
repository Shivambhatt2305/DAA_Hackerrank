def getTotalX(a, b):
    low = max(a)
    high = min(b)
    count = 0

    for x in range(low, high + 1):
        ok = True
        for i in a:
            if x % i != 0:
                ok = False
                break
        for j in b:
            if j % x != 0:
                ok = False
                break
        if ok:
            count += 1

    return count


def main():
    n, m = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))

    result = getTotalX(arr, brr)
    print(result)


if __name__ == "__main__":
    main()
