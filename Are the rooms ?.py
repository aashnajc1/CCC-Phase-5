import heapq

n, k = map(int, input().split())

bookings = []
for i in range(n):
    arrival, departure = map(int, input().split())
    bookings.append((arrival, departure))

bookings.sort()

heap = []

for booking in bookings:
    while heap and heap[0] < booking[0]:
        heapq.heappop(heap)

    heapq.heappush(heap, booking[1])

    if len(heap) > k:
        print("no")
        exit()

print("yes")
