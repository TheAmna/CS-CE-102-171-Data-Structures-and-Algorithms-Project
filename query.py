from create_tree import create_quadtree_graph, file_handling

#Time complexity: O(n) in the worst case, where n is the number of nodes in the quadtree.
#In best case, O(1) if region doesnt intersect with any nodes & on average it could be any number k between 1 and n.
def range_query(quadtree, region):
    results = []
    stack = [list(quadtree.keys())[0]]  
    print(stack)
    while stack:
        current_key = stack.pop() # LIFO-pop the last element of the stack
        current_node = quadtree[current_key] 
        if isinstance(current_node, dict): #if it is a dict, then reached leaf node, so check whetehr it intersects with region or not
            if does_intersect(current_key, region):
                results.append(current_key) 
        else:  
            for child_key in current_node: 
                #if it is a list, then check the children of current node by checking whetehr it is in the region & then add to stack
                if does_intersect(child_key, region):
                    stack.append(child_key)
    return results

#checks whether a the quadtree has a particular region
def intersection_check(quadtree, region): 
    stack = [list(quadtree.keys())[0]] 
    while stack:
        current_key = stack.pop()
        if current_key not in quadtree or quadtree[current_key] is None: #because we also have to look out for deleted nodes
            continue
        if does_intersect(current_key, region):
            return True
        current_node = quadtree[current_key]
        if isinstance(current_node, list):
            stack.extend(current_node)
    return False

#finds the nearest neighbor of a point in the quadtree field, basically the surrounding squares
def nearest_neighbor_search(quadtree, target_point):
    neighbors = []
    stack = [list(quadtree.keys())[0]]  
    while stack:
        current_key = stack.pop()
        current_node = quadtree[current_key]
        if current_node is None:
            continue  
        if not isinstance(current_node, list): 
            x_min, y_min = current_key[0]
            x_max, y_max = current_key[3]
            if x_min <= target_point[0] <= x_max and y_min <= target_point[1] <= y_max:
                neighbors.append(current_key)
        else:
            stack.extend(current_node)
    return neighbors


#This function runs in constant time because its only making comparisons. O(1)
def does_intersect(node, region):
    node_x_min, node_y_min = node[0]#bottom left of the node which we r checking 
    node_x_max, node_y_max = node[3]#top right of the node  
    region_x_min, region_y_min = region[0]  # bottom-left of the region
    region_x_max, region_y_max = region[3]  # top-right of the region
    #If any of these are true, the rectangles do NOT intersect
    is_left = region_x_max < node_x_min 
    is_right = region_x_min > node_x_max 
    is_below = region_y_max < node_y_min 
    is_above = region_y_min > node_y_max 
    if is_left or is_right or is_below or is_above:
        return False
    else:
        return True


#purpose is to get center of node, to find the dist b/w the target & center of the node, so that we can find the nearest neighbor
#runs in constant time because its only doing calcukations. O(1)

def get_node_center(region):
    x_min, y_min = region[0]
    x_max, y_max = region[3]
    center_x = (x_min + x_max) / 2
    center_y = (y_min + y_max) / 2
    return (center_x, center_y)


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

g = create_quadtree_graph(4)  
quadtree = file_handling(g)  
region = ((0, 0), (0, 8), (8, 0), (8, 8))
range_results = range_query(quadtree, region)
print("Range Query Results:", range_results)

region_to_check = ((4, 4), (4, 6), (6, 4), (6, 6))
intersection_found = intersection_check(quadtree, region_to_check)
print("Intersection Found:", intersection_found)

target_point = (3, 3)
nearest_neighbor = nearest_neighbor_search(quadtree, target_point)
print("Nearest Neighbor:", nearest_neighbor)
