"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        # stop -> list of route indices
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # BFS
        queue = deque()
        queue.append((source, 0))  # (current_stop, buses_taken)

        visited_stops = set([source])
        visited_routes = set()

        while queue:
            stop, buses = queue.popleft()

            if stop == target:
                return buses

            # Try all routes you can take from this stop
            for route_idx in stop_to_routes[stop]:
                if route_idx in visited_routes:
                    continue
                visited_routes.add(route_idx)

                # Once you board this bus (route), you can visit all its stops
                for next_stop in routes[route_idx]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))

        # If we exhaust the queue and never reach target
        return -1
