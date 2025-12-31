from create_tree import *  
from query import *

#time complexity: range_query worst case is o(n) & then loop which runs o(n) times so o(n) worst time 
#if the node is a leaf the function deletes it by marking it None
def delete_region(quadtree, region):
    intersecting_nodes = range_query(quadtree, region)
    for node_key in intersecting_nodes:
        if node_key in quadtree and isinstance(quadtree[node_key], dict):
            quadtree[node_key] = None  

# example testcase
g = create_quadtree_graph(4) 
quadtree = file_handling(g) 
region_to_delete = ((0, 0), (0, 12), (12, 0), (12, 12))  
delete_region(quadtree, region_to_delete)
print(quadtree)
