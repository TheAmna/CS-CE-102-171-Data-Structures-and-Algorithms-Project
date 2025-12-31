import csv
import ast

#time complexity: 4^n because we are performing o(1) operations for each node & there are 4^n nodes in the quadtree
def create_quadtree_graph(n):
    size = (2 ** n) 
    graph = {}
    def subdivide(x_min, x_max, y_min, y_max):
        node = ((x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max))
        if x_max - x_min == 1 and y_max - y_min == 1:
            graph[node] = []
            return
        mid_x = (x_min + x_max) // 2
        mid_y = (y_min + y_max) // 2
        children = [
            ((x_min, y_min), (x_min, mid_y), (mid_x, y_min), (mid_x, mid_y)),  # SW
            ((x_min, mid_y), (x_min, y_max), (mid_x, mid_y), (mid_x, y_max)),  # NW
            ((mid_x, y_min), (mid_x, mid_y), (x_max, y_min), (x_max, mid_y)),  # SE
            ((mid_x, mid_y), (mid_x, y_max), (x_max, mid_y), (x_max, y_max)),  # NE
        ]
        graph[node] = children
        for child in children:
            subdivide(child[0][0], child[3][0], child[0][1], child[3][1])
    subdivide(0, size, 0, size)
    return graph

#time complexity: 2^n where n is no of nodes in quadtree bcz the no of leaf nodes are 2^n & we are performing o(1) operation for each
def file_handling(g): 
    with open("soil_data.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        count=0
        for row in reader:
            bl = ast.literal_eval(row['bottom_left'])
            br = ast.literal_eval(row['bottom_right'])
            tl = ast.literal_eval(row['top_left'])
            tr = ast.literal_eval(row['top_right'])
            node = (bl, br, tl, tr)
            data = {
                "moisture": float(row["moisture"]),
                "ph": float(row["ph"]),
                "nutrients": int(row["nutrients"]),
                "temperature": float(row["temperature"]),
                "humidity": int(row["humidity"])
            }
            if node not in g:
                print(f"Node {node} not available in graph")
            else:
                g[node] = data
                count+=1
        print(count)
    return g

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# example testcase
g=create_quadtree_graph(4)
file_handling(g)
print(g)
print(len(g))
