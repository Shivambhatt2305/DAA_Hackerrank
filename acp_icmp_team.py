def acmTeam(topic):
    n = len(topic)
    max_topics = 0
    team_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Count number of topics known by at least one of the pair
            known = sum(1 for a, b in zip(topic[i], topic[j]) if a == '1' or b == '1')

            if known > max_topics:
                max_topics = known
                team_count = 1
            elif known == max_topics:
                team_count += 1

    return [max_topics, team_count]


def main():
    n, m = map(int, input().strip().split())
    topic = [input().strip() for _ in range(n)]

    result = acmTeam(topic)
    print(result[0])
    print(result[1])


if __name__ == "__main__":
    main()
