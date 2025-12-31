from create_tree import *

#time complexity: O(n) where n is the number of nodes in the quadtree
def traverse_square(g, square):
    if square not in g:
        print(f"Square {square} not found in graph.")
        return None

    print(f"Found square: {square}  Data: {g[square]}")
    bl, br, tl, tr = square
    x0, y0 = bl
    x1, y1 = tr
    if abs(x1 - x0) <= 1 and abs(y1 - y0) <= 1:
        print(f"Reached leaf node: {square}")
        return g[square]
    
    mx = (x0 + x1) // 2
    my = (y0 + y1) // 2

    children = [
        ((bl), (x0, my), (mx, y0), (mx, my)),     
        ((x0, my), (br), (mx, my), (mx, y1)),   
        ((mx, y0), (mx, my), (tl), (x1, my)),     
        ((mx, my), (mx, y1), (x1, my), (tr))      
    ]
    for child in children: 
        traverse_square(g, child)
    return g[square]


#runs in constant time, because it IS a dictionary
def update_square(g, square, new_value):
    if square in g:
        bl, br, tl, tr = square
        x0, y0 = bl
        x1, y1 = tr
        if abs(x1 - x0) <= 1 and abs(y1 - y0) <= 1:
            print(f"Updating leaf node {square} to new value: {new_value}")
            g[square] = new_value
            return True
        else:
            print(f"Square {square} is not a leaf node, cannot update.")
            return False
    else:
        print(f"Square {square} not found in quadtree.")
        return False
    
    # example testcase
g = create_quadtree_graph(4)  
quadtree = file_handling(g) 
print(quadtree)
start = ((2, 5), (2, 6), (3, 5), (3, 6))  
traverse_square(g, start)
