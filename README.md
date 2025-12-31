# CS-CE-102-171-Data_structures_and_Alogorithms


<img width="360" height="325" alt="Meri Mitti" src="https://github.com/user-attachments/assets/49a2092f-7aa9-4fed-abf9-63d1e51389a7" />

*Meri Mitti Logo*


## Team Members 

- [Shifa Imran](https://github.com/humna0809)
- [Amna Ali](https://github.com/TheAmna)
- Maryam Fareed Siddique 

## Problem Statement and Significance 

- Agriculture in rural areas of Pakistan faces challenges in efficiently monitoring large farmlands due
to uneven soil conditions, varying moisture levels, and inconsistent nutrient distribution. Traditional
methods of manual data collection are time-consuming and lack precision, leading to suboptimal
crop yields and resource wastage.

- To address this, we propose a *Smart Agriculture System* that uses a *Quadtree-based spatial
partitioning technique* to divide a farm into smaller, manageable patches. Each patch will store
critical agricultural data such as the moisture level, pH value, nutritional content.

## Proposed Solution

1) Represent the entire farm as a root node in a quadtree.
2) Recursively divide the farm into four quadrants (NE, NW, SE, SW) until each patch reaches
an area of 1 by 1.
3) Associate each leaf node with sensor data from the CSV file called SensorData.csv.
4) Implement a search function that, given coordinates, traverses the quadtree and returns soil
metrics for the corresponding patch.
5) The system will allow farmers to input coordinates, and in return, it will retrieve real-time soil
data for the corresponding patch, enabling precise irrigation, fertilization, and soil treatment.



## Quadtree Data Structure 

- A quadtree is a tree data structure that is commonly used to partition a *two-dimensional space*
into smaller regions. It is called a quadtree because each node in the tree has four children, corre-
sponding to the four quadrants of the space.

- The quadtree starts with a *root node* that represents the entire space. Each level of the tree
divides the space into four equal-sized quadrants. The leaf nodes of the tree represent smaller
regions of the space. It allows efficient insertion, deletion, and retrieval of objects based on their
spatial location.

- One of the key advantages of the quadtree is its ability to efficiently handle *spatial queries* such
as range searches and nearest neighbor searches. By dividing each region into cardinal directions,
quadtree can be used to reach specific region quickly by eliminating irrelevant objects.


<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/d7cb8270-2b7d-4436-98bc-fa2ee4b2c1cd" />

## Time Complexity Analysis 


1. **Quadtree Construction**:
  - `create quadtree graph(n)`: O(4ⁿ)  
    The recursive function follows T(k) = 4T(k-1) + 1. Solving this gives roughly (4ⁿ⁺¹ - 1)/3 operations, which is O(4ⁿ). This matches the exponential growth of nodes: 5 nodes for 2×2 grid, 21 nodes for 4×4 grid, and so on for a 2ⁿ × 2ⁿ area.
  - File handling `g(n)`: O(2ⁿ)  
    There are 2ⁿ leaf nodes, and we do constant-time work for each.

2. **Spatial Queries**:
  - `range query(quadtree, region)`: O(k)  
    Typically visits k nodes in the region; worst case O(n) where n is total nodes.
  - `intersection check(quadtree, region)`: O(k)  
    Stops early as soon as the first intersection is found.

3. **Nearest Neighbor Search**:
  - `nearest neighbor search(quadtree, point)`: O(log n)  
    Best case with a balanced tree; worst case O(n).

4. **Statistical Calculations**:
  - `calculate average and extrema()`: O(k)  
    Simple linear scan over k nodes in the region.
  - `calculate median per value()`: O(k log k)  
    Requires sorting the k values to find the median.

5. **Dynamic Filtering**:
  - `check dynamic filters(node, filters)`: O(1)  
    Constant-time checks per node.
  - Flexible filtered range query: O(k · m)  
    Visits k nodes and applies m filters to each.

6. **Region Deletion**:
  - `delete region(quadtree, region)`: O(n)  
    Uses range query to find nodes, then processes them linearly.

## Searching 
 
The search starts at the root node, which covers the entire farm. As it moves down the tree, it checks each quadrant to see how it overlaps with the area the user is interested in.
If a quadrant does not overlap, the whole subtree under it is skipped completely, saving time.
If a quadrant is completely inside the search area, all the data under it is collected.
If it only partially overlaps, the search continues into its four child quadrants. When it reaches the small 1×1 leaf nodes that fall inside the area, their data is added to the results.

## Insertion 

The quadtree is built completely at the beginning, creating every node and every 1×1 leaf for the whole farm grid. 
To add or update information for a particular farm plot at a specific (x, y) position, the program travels down from the root to the exact leaf node that represents that tiny plot. 
Once there, it simply stores or changes the data, such as the crop type or soil value. Updating works in the same way.

## Deletion 

When a crop is harvested or a plot becomes unused, we mark it as empty.
The program travels to the leaf node for that (x, y) position and sets its data to "Null". 
The node remains in the tree, but now it shows that nothing is growing there at the moment. This keeps all searches and other operations fast and simple.
Later, if you want to plant something new in that same spot, you just go back to the same leaf and add the new data.

## Challenges 

-  Standard quadtrees only split areas when there are objects or data points in them. We took a different quadtree approach in this project as compared to the standard ones. We created a full region quadtree that splits the entire farm grid into 1×1 cell right from the start,
creating a fixed and balanced tree with all nodes present always. So this was challenginf yet interesting as we figured out ways to implement this dense quadtree approach.

- The tree structure once built stays fixed, so we had to find a new way to implement insertion and deletion. So we stumbled upon the solution that to *insert* data, we find the correct leaf and add information to it. For *deletion*
  we just mark the leaf as empty without removing it. 


## Key Learnings from this Project 

- We learnt implementing a new data structure instead of relying on the traditional data structures like Linked Lists, Stacks, Queues etc. It was a good learning process.
  
- We learned the trade-offs between different approaches: a full quadtree is good for fixed grids but uses a lot of memory. Adaptive quadtrees save space by only creating nodes where needed.
This helped us understand why real-world applications choose specific data structures based on memory, speed, and flexibility needs.













