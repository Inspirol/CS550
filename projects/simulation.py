'''
Monte-carlo simulation of the amount of planes taking off at any given moment in America.
Using other data to simulate the amount of planes taking off at any given moment in America:
- Weather -> not too big of a factor, unless its a hurricane or something
- Day of the week -> More planes probably take off on a Monday than a Sunday
- Normal travel times -> how long does it take to get from one airport to another usually
- Total flights per day -> how many flights are there in America per day
- Average departure time -> how long does it take to get from the gate to the runway
- Average departures at an airport per day -> how many planes take off from an airport per day
- Average ATC scheduling time -> how long does it take to get a plane scheduled for takeoff
- average number of runways at an airport -> how many runways does an airport have
- Number of active planes in service 
- Average time to take off
- Number of airports

-- Considering the difference between the day and night, 

'''

# import necessary libraries
import numpy as np
from numpy import random
from enum import Enum
import matplotlib.pyplot as plt
from typing import Literal
from datetime import datetime

# Define a custom type for representing time in minutes
minutes = float

# Constants class to store simulation parameters
class CONSTANTS:
    # Average number of commercial planes and private planes in service
    ave_planes_in_service_commercial = 5791
    ave_planes_in_service_private = 15000
    ave_planes_in_service_total = ave_planes_in_service_commercial + ave_planes_in_service_private

    # Number of public, private, and total airports
    num_airports_public = 5193
    num_airports_private = 14776
    num_airports_total = num_airports_public + num_airports_private

    # Ranges for various parameters in the simulation
    flight_time_range = (26, 585)
    takeoff_time_range = (5, 30)
    departure_time_range = (5, 15)
    runways_range = (1, 7)

    flights_per_day = 4500 # this is actually 45000, but my computer can't handle that much data, so its scaled to 4500
    flight_departure_time_range = (6, 23)
    plane_flights_per_day_commercial_range = (2, 5)
    plane_flights_per_day_private_range = (1, 3)

# Flight class to represent a single flight
class Flight:
    def __init__(self, duration: minutes, departure_time: minutes):
        self.duration = duration
        self.departure_time = departure_time

# Plane class to represent a single plane
class Plane:
    def __init__(self, type: Literal['commercial', 'private']):
        self.type = type
        # Set the number of flights per day based on the type of plane
        if self.type == 'commercial':
            self.flights_per_day = random.randint(*CONSTANTS.plane_flights_per_day_commercial_range)
        else:
            self.flights_per_day = random.randint(*CONSTANTS.plane_flights_per_day_private_range)
        self.takeoff_time = random.randint(*CONSTANTS.takeoff_time_range)

    def generate_flights(self) -> list[Flight]:
        self.flights = []
        current_time = (
            CONSTANTS.flight_departure_time_range[0] if self.type == 'commercial' else
            random.normal(*CONSTANTS.flight_departure_time_range)
        ) * 60
        for i in range(self.flights_per_day):
            duration = random.normal(*CONSTANTS.flight_time_range)
            self.flights.append(Flight(duration, current_time))
            current_time += duration
        return self.flights

# Simulation class to run the Monte Carlo simulation
class Simulation:
    def __init__(self):
        self.available_flights = CONSTANTS.flights_per_day
        self.tot_flights: list[Flight] = []

        # Create planes - commercial planes first
        self.planes_commercial = [Plane('commercial') for i in range(CONSTANTS.ave_planes_in_service_commercial)]
        for plane in self.planes_commercial:
            self.available_flights -= plane.flights_per_day
        print(self.available_flights)
        # Then create private planes
        self.planes_private = [Plane('private') for i in range(CONSTANTS.ave_planes_in_service_private)]
        for plane in self.planes_private:
            self.available_flights -= plane.flights_per_day
        print(self.available_flights)

        # Combine commercial and private planes
        self.planes = self.planes_commercial + self.planes_private

        # Distribute any remaining flights randomly
        for i in range(self.available_flights):
            plane = random.choice(self.planes)
            plane.flights_per_day += 1

        # Generate flights for all planes
        for plane in self.planes:
            self.tot_flights += plane.generate_flights()

    def get_data(self):
        return self.tot_flights

    def plot(self):
        data = self.get_data()

        # Group departure times within 15 minutes intervals
        scheduled_day = range(CONSTANTS.flight_departure_time_range[0] * 60, CONSTANTS.flight_departure_time_range[1] * 60, 30)
        takeoffs = []

        for period in scheduled_day:
            takeoffs.append(0)
            for flight in data:
                if flight.departure_time < period and flight.departure_time > period - 30:
                    takeoffs[-1] += 1

        x = [i for i in scheduled_day]
        y = [i for i in takeoffs]
        average = sum(y) / len(y)

        # Plotting the data
        plt.plot(x, y)
        plt.axhline(average, color='r', linestyle='--')  # Add average line
        plt.show()

# Main function to run the simulation
def main():
    sim = Simulation()
    sim.plot()
    print(sim.get_data())

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
