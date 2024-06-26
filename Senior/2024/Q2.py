def validate_pattern(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    heaviness = {char: counts[char] > 1 for char in counts}

    for i in range(len(s) - 1):
        if heaviness[s[i]] == heaviness[s[i + 1]]:
            return False 
    return True

T, N = map(int, input().split())

results = []
for _ in range(T):
    seq = input()
    results.append("T" if validate_pattern(seq) else "F")
print("\n".join(results))