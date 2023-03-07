n = int(input())
gas = list(map(int, input().split()))
cost = list(map(int, input().split()))

start_index = 0
end_index = 1
tank = gas[0] - cost[0]

while end_index != start_index or tank < 0:
    while tank < 0 and start_index != end_index:
        tank -= gas[start_index] - cost[start_index]
        start_index = (start_index + 1) % n

        if start_index == 0:
            print("-1")
            exit()

    tank += gas[end_index] - cost[end_index]
    end_index = (end_index + 1) % n

print(start_index)
