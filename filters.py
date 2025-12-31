from create_tree import create_quadtree_graph, file_handling
from query import range_query  

# runs in constant time O(1) as primitive operations like comparisions
def check_dynamic_filters(node, filters):
    if node is None:
        return False
    if "moisture_range" in filters:
        min_moisture, max_moisture = filters["moisture_range"]
        if "moisture" not in node or not (min_moisture <= node["moisture"] <= max_moisture):
            return False
    if "ph_range" in filters:
        min_ph, max_ph = filters["ph_range"]
        if "ph" not in node or not (min_ph <= node["ph"] <= max_ph):
            return False
    if "temperature_range" in filters:
        min_temp, max_temp = filters["temperature_range"]
        if "temperature" not in node or not (min_temp <= node["temperature"] <= max_temp):
            return False
    if "humidity_range" in filters:
        min_humidity, max_humidity = filters["humidity_range"]
        if "humidity" not in node or not (min_humidity <= node["humidity"] <= max_humidity):
            return False
    if "nutrients_range" in filters:
        min_nutrients, max_nutrients = filters["nutrients_range"]
        if "nutrients" not in node or not (min_nutrients <= node["nutrients"] <= max_nutrients):
            return False
    return True

## this function runs for O(k*m) times based on the k size of the nodes in region 
# the loop runs for O(m) times too, as m filters applied

def flexible_filtered_range_query(quadtree, region, filters):
    valid_nodes = [] # list of leaf nodes of that region
    nodes_in_region = range_query(quadtree, region)
    for node_key in nodes_in_region:
        node = quadtree.get(node_key)
        if check_dynamic_filters(node, filters):
            valid_nodes.append(node_key)
    return valid_nodes


# example testcase
g = create_quadtree_graph(4)
quadtree = file_handling(g)
region = ((0, 0), (0, 8), (8, 0), (8, 8))
filters = {
    "moisture_range": (0.5, 1.0),
    "ph_range": (5.0, 7.0),
    "temperature_range": (10.0, 30.0),
    "humidity_range": (20.0, 70.0),
    "nutrients_range": (10, 50)
}
print("Filtered Range Query Results:", flexible_filtered_range_query(quadtree, region, filters))
