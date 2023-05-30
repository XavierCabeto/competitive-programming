t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    i = 0
    while i < n and (s[i] == 'm' or s[i] == 'M'):
        i += 1
    if i == 0 or i == n:
        print("NO")
        continue

    while i < n and (s[i] == 'e' or s[i] == 'E'):
        i += 1
    if i == 1 or i == n:
        print("NO")
        continue

    while i < n and (s[i] == 'o' or s[i] == 'O'):
        i += 1
    if i == 2 or i == n:
        print("NO")
        continue

    while i < n and (s[i] == 'w' or s[i] == 'W'):
        i += 1
    if i != n:
        print("NO")
        continue
    
    print("YES")
