import heapq
import json
import logging
from typing import Dict, List

# Simple passenger class


class Passenger:

    def __init__(self, departureTime):
        self.departureTime = departureTime
        self.numberOfRequests = 0

    def askTimeToDeparture(self):
        self.numberOfRequests += 1
        return self.departureTime

    def getNumberOfRequests(self):
        return self.numberOfRequests

    def __lt__(self, other):
        return self.departureTime < other.departureTime


def execute(prioritisation_function, passenger_data, cut_off_time):
    totalNumberOfRequests = 0
    passengers = []

    # Initialise list of passenger instances
    for eachPassenger in passenger_data:
        passengers.append(
            Passenger(eachPassenger)
        )

    # Apply solution and re-shuffle with departure cut-off time
    prioritised_and_filtered_passengers = prioritisation_function(
        passengers, cut_off_time)

    # Sum totalNumberOfRequests across all passengers
    for i in range(len(passengers)):
        totalNumberOfRequests += passengers[i].getNumberOfRequests()

    prioritised_filtered_list = []
    for i in range(len(prioritised_and_filtered_passengers)):
        prioritised_filtered_list.append(
            prioritised_and_filtered_passengers[i].departureTime)

    print("\n")
    return {
        "total_number_of_requests": totalNumberOfRequests,
        "prioritised_filtered_list": prioritised_filtered_list
    }


def prioritisation_function(passengers, cut_off_time):
    """
    This function prioritises passengers based on their departure time.
    It uses a heap data structure to efficiently sort the passengers.
    Passengers with a departure time less than the cut-off time are removed from the heap.

    Parameters:
    passengers (list): A list of Passenger objects.
    cut_off_time (int): The cut-off time for departure.

    Returns:
    list: A list of prioritised Passenger objects.
    """

    heap = []

    for p in passengers:

        print("Heap: ", heap)

        departure_time = p.askTimeToDeparture()
        heapq.heappush(heap, (departure_time, p))

    heapq.heapify(heap)

    while heap and heap[0][0] < cut_off_time:
        heapq.heappop(heap)

    return [p for _, p in heap]


def run_airport(payload):

    results = []

    for eachPayload in payload:
        result = execute(
            prioritisation_function,
            eachPayload["departureTimes"],
            eachPayload["cutOffTime"]
        )

        results.append({
            "id": eachPayload["id"],
            "sortedDepartureTimes": result['prioritised_filtered_list'],
            "numberOfRequests": result["total_number_of_requests"]
        })

    return results
