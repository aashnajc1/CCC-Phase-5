n = int(input())
ratings = list(map(int, input().split()))

candies = [1] * n

# Traverse from left to right
for i in range(1, n):
    if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1] + 1

# Traverse from right to left
for i in range(n-2, -1, -1):
    if ratings[i] > ratings[i+1]:
        candies[i] = max(candies[i], candies[i+1] + 1)

# Calculate the sum of candies
min_candies = sum(candies)

print(min_candies)
