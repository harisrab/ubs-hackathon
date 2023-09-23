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

    # def __lt__(self, other):
    #     return self.departureTime < other.departureTime


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

    sorted_passengers = sorted(
        passengers, key=lambda passenger: passenger.askTimeToDeparture())
    
    # for eachPerson in sorted_passengers:
    #     print(eachPerson.__dict__)

    # print("\n\n")
    while sorted_passengers and sorted_passengers[0].askTimeToDeparture() < cut_off_time:
        p = sorted_passengers.pop(0)

        # print("Popped Off: ", p.__dict__)

    # for eachPerson in sorted_passengers:
    #     print(eachPerson.__dict__)

    return sorted_passengers

    # # Create a heap with each passenger's departure time and the passenger object
    # heap = [p for p in passengers]

    # # Transform list x into a heap
    # heapq.heapify(heap)

    # # Continue until the heap is empty or the smallest departure time is greater than the cut-off time
    # while heap and heap[0].askTimeToDeparture() <= cut_off_time:
    #     # Remove and return the smallest departure time from the heap
    #     p = heapq.heappop(heap)

    # return [p for p in heap]


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

        # break

    return results
