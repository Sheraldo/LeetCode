"""
https://leetcode.com/problems/design-parking-system/description/?envType=daily-question&envId=2023-09-05

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
"""
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cap = (big, medium, small)
        self.used = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        carType -= 1
        if self.used[carType] < self.cap[carType]:
            self.used[carType] += 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
