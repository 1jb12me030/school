schools = [
    {"name": "School A", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "School B", "latitude": 34.0522, "longitude": -118.2437},
    {"name": "School C", "latitude": 41.8781, "longitude": -87.6298},
    
]

import math

def calculate_distance(lat1, lon1, lat2, lon2):
    
    radius = 6371  

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance

def calculate_total_distance(route):
    
    total_distance = 0
    for i in range(len(route) - 1):
        school1 = schools[route[i]]
        school2 = schools[route[i + 1]]
        distance = calculate_distance(school1['latitude'], school1['longitude'],
                                      school2['latitude'], school2['longitude'])
        total_distance += distance
    return total_distance

def nearest_neighbor_algorithm():
    
    route = [0]  

    
    while len(route) < len(schools):
        current_school = route[-1]
        min_distance = float('inf')
        nearest_school = None

        for i, school in enumerate(schools):
            if i not in route:
                distance = calculate_distance(schools[current_school]['latitude'], schools[current_school]['longitude'],
                                              school['latitude'], school['longitude'])
                if distance < min_distance:
                    min_distance = distance
                    nearest_school = i

        route.append(nearest_school)

    return route


optimized_route = nearest_neighbor_algorithm()

# Print the optimized route
for i in optimized_route:
    school = schools[i]
    print(school['name'])
