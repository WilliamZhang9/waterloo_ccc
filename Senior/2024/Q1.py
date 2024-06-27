def get_match_hat_num(n, hat_nums):
    count = 0
    half_n = n // 2  
    for i in range(half_n):
        if hat_nums[i] == hat_nums[i + half_n]:
            count += 2  
    return count

N = int(input())
hat_numbers = [int(input()) for _ in range(N)]

match_hat_num = get_match_hat_num(N, hat_numbers)
print(match_hat_num)
