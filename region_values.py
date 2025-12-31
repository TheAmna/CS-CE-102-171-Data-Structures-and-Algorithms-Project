from create_tree import *  
from query import *

# this runs for O(n) times worst case (based on the size of the region mainly)
def calculate_average_and_extrema(quadtree, region):
    data_points = range_query(quadtree, region)  
    moisture_values = []
    ph_values = []
    temperature_values = []
    humidity_values = [] 
    nutrients_values = []  
    
    for node_key in data_points:
        node = quadtree[node_key]
        if isinstance(node, dict): 
            moisture_values.append(node.get("moisture", 0))
            ph_values.append(node.get("ph", 0))
            temperature_values.append(node.get("temperature", 0))
            humidity_values.append(node.get("humidity", 0))  
            nutrients_values.append(node.get("nutrients", 0))  
        else:
            print(f"Unexpected node structure for {node_key}: {node}")
    avg_moisture = sum(moisture_values) / len(moisture_values) if moisture_values else 0
    avg_ph = sum(ph_values) / len(ph_values) if ph_values else 0
    avg_temperature = sum(temperature_values) / len(temperature_values) if temperature_values else 0
    avg_humidity = sum(humidity_values) / len(humidity_values) if humidity_values else 0 
    avg_nutrients = sum(nutrients_values) / len(nutrients_values) if nutrients_values else 0  
    
    min_moisture = min(moisture_values) if moisture_values else 0
    max_moisture = max(moisture_values) if moisture_values else 0
    
    min_ph = min(ph_values) if ph_values else 0
    max_ph = max(ph_values) if ph_values else 0
    
    min_temperature = min(temperature_values) if temperature_values else 0
    max_temperature = max(temperature_values) if temperature_values else 0
    
    min_humidity = min(humidity_values) if humidity_values else 0  
    max_humidity = max(humidity_values) if humidity_values else 0  
    
    min_nutrients = min(nutrients_values) if nutrients_values else 0  
    max_nutrients = max(nutrients_values) if nutrients_values else 0 
    return {
        "avg_moisture": avg_moisture,
        "avg_ph": avg_ph,
        "avg_temperature": avg_temperature,
        "avg_humidity": avg_humidity,  
        "avg_nutrients": avg_nutrients,  
        "min_moisture": min_moisture,
        "max_moisture": max_moisture,
        "min_ph": min_ph,
        "max_ph": max_ph,
        "min_temperature": min_temperature,
        "max_temperature": max_temperature,
        "min_humidity": min_humidity, 
        "max_humidity": max_humidity, 
        "min_nutrients": min_nutrients, 
        "max_nutrients": max_nutrients,  
    }

# time complexity : only sorting values of list, so it runs in O(nlogn) time , the rest is O(1)
def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2


#this runs for O(n) times worst case (based on the size of the region mainly
def calculate_median_per_value(quadtree, region):
    data_points = range_query(quadtree, region) 
    moisture_values, ph_values, temperature_values, humidity_values, nutrients_values = [], [], []

    for node_key in data_points:# this loop runs for O(n) times
        node = quadtree[node_key]
        if isinstance(node, dict):
            moisture_values.append(node.get("moisture", 0))
            ph_values.append(node.get("ph", 0))
            temperature_values.append(node.get("temperature", 0))
            humidity_values.append(node.get("humidity", 0))
            nutrients_values.append(node.get("nutrients", 0))
    median_values = {
        "moisture": calculate_median(moisture_values),
        "ph": calculate_median(ph_values),
        "temperature": calculate_median(temperature_values),
        "humidity": calculate_median(humidity_values),  
        "nutrients": calculate_median(nutrients_values),  
    }
    return median_values

#again, runs for worst case O(n) based on the size of the region mainly
#the loop runs for O(n) times too
def calculate_sum_per_value(quadtree, region):
    data_points = range_query(quadtree, region)
    sum_values = {
        "moisture": 0,
        "ph": 0,
        "temperature": 0,
        "humidity": 0,
        "nutrients": 0,
    }
    for node_key in data_points:
        node = quadtree[node_key]
        if isinstance(node, dict):
            sum_values["moisture"] += node.get("moisture", 0)
            sum_values["ph"] += node.get("ph", 0)
            sum_values["temperature"] += node.get("temperature", 0)
            sum_values["humidity"] += node.get("humidity", 0)
            sum_values["nutrients"] += node.get("nutrients", 0)
    return sum_values

g = create_quadtree_graph(4)  
quadtree = file_handling(g)  
region_to_query = ((0, 0), (0, 8), (8, 0), (8, 8))  
result = calculate_average_and_extrema(quadtree, region_to_query)
print(result)
