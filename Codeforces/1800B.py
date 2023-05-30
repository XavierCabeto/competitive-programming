t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    counts = [0] * 26

    for c in s:
        counts[ord(c.lower()) - ord('a')] += 1

    ans = 0

    for i in range(26):
        cnt_upper = counts[i]
        cnt_lower = counts[i + 32]
        pairs = min(cnt_upper, cnt_lower)
        if pairs * 2 <= cnt_upper or pairs * 2 <= cnt_lower:
            ans += pairs
        else:
            ans += cnt_upper // 2 + cnt_lower // 2

    if k > 0:
        for i in range(26):
            cnt_upper = counts[i]
            cnt_lower = counts[i + 32]
            pairs = min(cnt_upper, cnt_lower)
            if pairs * 2 <= cnt_upper or pairs * 2 <= cnt_lower:
                continue
            else:
                if cnt_upper > cnt_lower:
                    diff = min(cnt_upper - pairs, k)
                    ans += diff // 2
                    k -= diff
                else:
                    diff = min(cnt_lower - pairs, k)
                    ans += diff // 2
                    k -= diff
            if k == 0:
                break

    print(ans)
