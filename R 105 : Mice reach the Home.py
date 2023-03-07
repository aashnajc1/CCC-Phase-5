n = int(input())
mice_pos = list(map(int, input().split()))
holes_pos = list(map(int, input().split()))

mice_pos.sort()
holes_pos.sort()

time_taken = max(abs(mice_pos[i] - holes_pos[i]) for i in range(n))

print(time_taken)
