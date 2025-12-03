def viralAdvertising(n):
    shared = 5
    cumulative = 0
    
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    
    return cumulative


def main():
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)


if __name__ == "__main__":
    main()
