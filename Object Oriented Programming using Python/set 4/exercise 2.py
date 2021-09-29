"""
Problem Statement
The circus has hired two riders – a bike rider and a cycle rider. Both of them ride vehicles but bike
rider rides the bike in a dome whereas the cycle rider rides the cycle blind folded. The circus manger
has also ensured that both of them are trained and have enough experience of performing these stunts
in circus. Apart from this, bike rider also has a race license.

Create the class diagram for representing the above scenario by choosing the class names, attributes,
methods and relationships from the list given below.

- experience
- performs_tricks()
- __init__(trained_status,experience,race_license)
- rider
- rides_blindfolded()
- trained_status
- __init__(trained_status,experience)
- rides_vehicle()
- bikeRider
- cycleRider
- race_license
- rides_in_dome()

Assume that none of the instance variables can be accessed outside the class whereas methods can be accessed.

Write a python program to implement the created class diagram. Represent bike rider and cycle rider,
make them ride the respective vehicles.

Note: rides_vehicle(), rides_in_dome(), rides_blindfolded() methods should display appropriate messages.
Assume that trained_status and race_license are boolean variables and experience is an integer.
"""
class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status=trained_status
        self.__experience = experience
    def rides_vehicle(self):
        print("Rides vehicle")

class BikeRider(Rider):
    def __init__(self,trained_status,experience,race_license):
        super().__init__(trained_status,experience)
        self.__race_license = race_license
    def rides_in_dome(self):
        print("Bike Rider Rides in dome")

class CycleRider(Rider):
    def rides_blindfolded(self):
        print("Cycle Rider rides blindfolded")

cycle_rider=CycleRider(True,4)
cycle_rider.rides_blindfolded()
bike_rider=BikeRider(True,3,True)
bike_rider.rides_in_dome()
