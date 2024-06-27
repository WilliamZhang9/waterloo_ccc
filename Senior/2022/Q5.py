from sys import maxsize as INT_MAX

n = int(input())
cost = list(map(int, input().split()))
p = input()
v = [[] for _ in range(n)]
dp = [[-1 for _ in range(5)] for __ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)

nrm, on, pay = 0, 1, 2

def rec(u, prev, state):
    global v, dp, p, cost
    ret = dp[u][state]
    if ret != -1:
        return ret
    if p[u] == 'Y' or state == on:
        ans = cost[u]
        for x in v[u]:
            if x == prev:
                continue
            cur = rec(x, u, on)
            ans = INT_MAX if cur == INT_MAX else ans + cur
        if state != pay:
            ans1 = 0
            for x in v[u]:
                if x == prev:
                    continue
                cur = rec(x, u, nrm)
                ans1 = INT_MAX if cur == INT_MAX else ans1 + cur
            ans = min(ans, ans1)
        ret = ans
    else:
        if len(v[u]) == 1 and v[u][0] == prev:
            return INT_MAX
        sum = 0
        ans = INT_MAX
        for x in v[u]:
            if x == prev:
                continue
            cur = rec(x, u, on)
            sum += cur
        for x in v[u]:
            if x == prev:
                continue
            cur1 = rec(x, u, on)
            cur2 = rec(x, u, pay)
            if cur2 != INT_MAX:
                ans = min(ans, sum - cur1 + cur2)
        if ans != INT_MAX:
            ans += cost[u]
        if state != pay:
            sum2 = 0
            ans2 = INT_MAX
            valid = True
            for x in v[u]:
                if x == prev:
                    continue
                cur = rec(x, u, nrm)
                if cur != INT_MAX:
                    sum2 += cur
                else:
                    valid = False
                    break
            if valid:
                for x in v[u]:
                    if x == prev:
                        continue
                    cur1 = rec(x, u, nrm)
                    cur2 = rec(x, u, pay)
                    if cur1 != INT_MAX and cur2 != INT_MAX:
                        ans2 = min(ans2, sum2 - cur1 + cur2)
                ans = min(ans, ans2)
        ret = ans
    dp[u][state] = ret
    return ret

print(rec(0, -1, nrm))
