class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_data = []
        fleet_arrival_time = []
        for i in range(0, len(position)):
            t = (target - position[i])/speed[i]
            car_data.append((position[i],t))

        car_data.sort(reverse=True)

        _, first_car_time = car_data[0]
        fleet_arrival_time.append(first_car_time)
        for i in range(1, len(car_data)):
            _, curr_car_time = car_data[i]
            if curr_car_time > fleet_arrival_time[-1]:
                fleet_arrival_time.append(curr_car_time)

        return len(fleet_arrival_time)