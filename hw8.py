import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        combined_cable = cable1 + cable2

        total_cost += combined_cable

        heapq.heappush(cables, combined_cable)

    return total_cost
