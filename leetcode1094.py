
def carPooling(trips,capacity):

    capacities = [0]*1000
    place = 0
    for trip in trips:
        people = trip[0]
        start = trip[1]
        end = trip[2]

        for i in range(start,end):
            capacities[i] += people
            if capacities[i] > place:
                place = capacities[i]


    if place <= capacity:
        return True
    return False


trips = [[2,1,5],[3,3,7]]
capacity = 5

print(carPooling(trips,capacity))


