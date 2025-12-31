from create_tree import create_quadtree_graph, file_handling
from delete_from_tree import *
from query import *
from search_tree import update_square
from filters import *
from region_values import *
from search_tree import *

#introduces meri mitti to user
def introduce_project():
    print()
    print("WELCOME TO ** MERI MITTI ** - THE SOIL MANAGEMENT SYSTEM")
    print("\nThis project uses a quadtree structure to manage soil data for different regions.")
    print("Each region has specific parameters like Moisture, pH level, Temperature, Humidity, and Nutrient content.")
    print("The system allows to perform tasks like searching for regions with specific properties, updating values, and more.")

#-------------------------------------------------------------------------------------------------------------------------------------------
#displays a list of available tasks for the user to choose from.
def display_tasks():
    print()
    print("\n" + "="*50)
    print("Please choose a task to perform:")    
    print("1. View farm data for a region")
    print("2. Perform a range query (search for regions with specific properties).")
    print("3. Check if a region intersects with another region.")
    print("4. Update a specific property of a region.")
    print("5. Delete a region")
    print("6. Calculate averages and extrema of a region (for all soil properties)")
    print("7. Calculate distance between two any points of your field.")
    print("8. Exit the program.")
    print("="*50)

#-------------------------------------------------------------------------------------------------------------------------------------------
#prompts the user to choose a task.
def get_task_choice():
    while True:
        try:
            task_choice = int(input("Enter the number of the task you'd like to perform: "))
            if task_choice in [1, 2, 3, 4, 5, 6, 7, 8]:
                return task_choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#-------------------------------------------------------------------------------------------------------------------------------------------
#helper function to get region coordinates from user
def get_region_coordinates(prompt="Enter coordinates for the region (x_min, y_min, x_max, y_max):"):
    print(prompt)
    x_min = int(input("Enter x_min: "))
    y_min = int(input("Enter y_min: "))
    x_max = int(input("Enter x_max: "))
    y_max = int(input("Enter y_max: "))
    return ((x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max))

#-------------------------------------------------------------------------------------------------------------------------------------------
#option 1: View farm data for a specific region
def view_farm_data(quadtree):
    print("\nView Farm Data for a Region")
    region = get_region_coordinates()
    results = range_query(quadtree, region)
    if not results:
        print("\nNo data found for the specified region.")
        return
    print("\nData for the selected region:")
    for node in results:
        if isinstance(quadtree[node], dict):  
            print(f"\nCoordinates: {node}")
            for key, value in quadtree[node].items():
                print(f"{key.capitalize()}: {value}")

#-------------------------------------------------------------------------------------------------------------------------------------------
#prompts the user for a range query and displays the results.
def perform_range_query(quadtree):
    print("\nPerforming Range Query:")
    print("Please enter the coordinates for the region (x_min, y_min, x_max, y_max):")
    x_min = int(input("Enter x_min: "))
    y_min = int(input("Enter y_min: "))
    x_max = int(input("Enter x_max: "))
    y_max = int(input("Enter y_max: "))
    region = ((x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max))
    # ask the user for any filters they want to apply
    filters = {} # stores the users selected filetrs as keys and range as values
    apply_filters = input("Do you want to apply any filters (yes/no)? ").strip().lower()
    if apply_filters == 'yes':
        filters = get_filters_from_user()
    # execute the range query and display results
    filtered_results = flexible_filtered_range_query(quadtree, region, filters)
    if filtered_results:
        print("\nFound the following squares that match your criteria:")
        for result in filtered_results:
            print(result)
    else:
        print("\nNo matching regions found for your query.")

#-------------------------------------------------------------------------------------------------------------------------------------------
#prompts the user for filter inputs for the query.
def get_filters_from_user():
    filters = {}
    moisture = input("Do you want to filter by Moisture? (yes/no) ").strip().lower()
    if moisture == 'yes':
        min_moisture = float(input("Enter the minimum moisture level (e.g., 0.5): "))
        filters["moisture"] = min_moisture
    ph = input("Do you want to filter by pH? (yes/no) ").strip().lower()
    if ph == 'yes':
        min_ph = float(input("Enter the minimum pH level (e.g., 5.0): "))
        max_ph = float(input("Enter the maximum pH level (e.g., 7.0): "))
        filters["ph_range"] = (min_ph, max_ph)
    temperature = input("Do you want to filter by Temperature? (yes/no) ").strip().lower()
    if temperature == 'yes':
        max_temp = float(input("Enter the maximum temperature (e.g., 30.0): "))
        filters["temperature"] = max_temp
    humidity = input("Do you want to filter by Humidity? (yes/no) ").strip().lower()
    if humidity == 'yes':
        min_humidity = float(input("Enter the minimum humidity level (e.g., 20): "))
        filters["humidity"] = min_humidity
    nutrients = input("Do you want to filter by Nutrients? (yes/no) ").strip().lower()
    if nutrients == 'yes':
        min_nutrients = float(input("Enter the minimum nutrients level (e.g., 10): "))
        filters["nutrients"] = min_nutrients
    return filters

#-------------------------------------------------------------------------------------------------------------------------------------------
#prompts the user for two regions and checks if they intersect.
def perform_intersection_check(quadtree):
    print("\nPerforming Intersection Check:")
    print("Please enter the coordinates for the first region (x_min, y_min, x_max, y_max):")
    x_min1 = int(input("Enter x_min: "))
    y_min1 = int(input("Enter y_min: "))
    x_max1 = int(input("Enter x_max: "))
    y_max1 = int(input("Enter y_max: "))
    region1 = ((x_min1, y_min1), (x_min1, y_max1), (x_max1, y_min1), (x_max1, y_max1))
    print("Please enter the coordinates for the second region (x_min, y_min, x_max, y_max):")
    x_min2 = int(input("Enter x_min: "))
    y_min2 = int(input("Enter y_min: "))
    x_max2 = int(input("Enter x_max: "))
    y_max2 = int(input("Enter y_max: "))
    region2 = ((x_min2, y_min2), (x_min2, y_max2), (x_max2, y_min2), (x_max2, y_max2))
    # check if the regions intersect
    if intersection_check(quadtree, region1) and intersection_check(quadtree, region2):
        print("\nThe regions intersect.")
    else:
        print("\nThe regions do not intersect.")

#-------------------------------------------------------------------------------------------------------------------------------------------
#prompts the user for a square to update and performs the update.
def perform_update(quadtree):
    print("\nUpdating a Square:")
    print("Please enter the coordinates for the square to update (x_min, y_min, x_max, y_max):")
    x_min = int(input("Enter x_min: "))
    y_min = int(input("Enter y_min: "))
    x_max = int(input("Enter x_max: "))
    y_max = int(input("Enter y_max: "))
    square = ((x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max))
    # if it's not a leaf node & exit.
    if not (abs(x_max - x_min) <= 1 and abs(y_max - y_min)) <= 1:
        print(f"Square {square} is not a leaf node, cannot update.")
        return
    #ask for the new value to update
    print("Please enter the new values for the square:")
    new_value = {}
    new_value["moisture"] = float(input("Enter moisture level: "))
    new_value["ph"] = float(input("Enter pH level: "))
    new_value["temperature"] = float(input("Enter temperature: "))
    new_value["humidity"] = float(input("Enter humidity: "))
    new_value["nutrients"] = float(input("Enter nutrient level: "))
    #update 
    update_success = update_square(quadtree, square, new_value)
    if update_success:
        print(f"\nSquare {square} updated successfully.")
    else:
        print(f"\nFailed to update square {square}.")

#-------------------------------------------------------------------------------------------------------------------------------------------
#option 5: delete a region
def perform_delete_region(quadtree):
    print("\nDelete a Region")
    print("WARNING: This will remove all data for the selected region.")
    confirm = input("Are you sure you want to continue? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Operation cancelled.")
        return
    region = get_region_coordinates()
    delete_region(quadtree, region) 
    print("\nRegion deleted successfully.")

#-------------------------------------------------------------------------------------------------------------------------------------------
#option 6: Calculate average and extrema for a region
def calculate_averages(quadtree):
    print("\nCalculate Averages and Extremes")
    region = get_region_coordinates()
    
    stats = calculate_average_and_extrema(quadtree, region)
    print("\nSoil Statistics for the region:")
    print(f"Average Moisture: {stats['avg_moisture']:.2f}%")
    print(f"Min/Max Moisture: {stats['min_moisture']}% / {stats['max_moisture']}%")
    print(f"\nAverage pH: {stats['avg_ph']:.2f}")
    print(f"Min/Max pH: {stats['min_ph']} / {stats['max_ph']}")
    print(f"\nAverage Temperature: {stats['avg_temperature']:.2f}°C")
    print(f"Min/Max Temperature: {stats['min_temperature']}°C / {stats['max_temperature']}°C")
    print(f"\nAverage Humidity: {stats['avg_humidity']:.2f}%")
    print(f"Min/Max Humidity: {stats['min_humidity']}% / {stats['max_humidity']}%")
    print(f"\nAverage Nutrients: {stats['avg_nutrients']:.2f}")
    print(f"Min/Max Nutrients: {stats['min_nutrients']} / {stats['max_nutrients']}")

#-------------------------------------------------------------------------------------------------------------------------------------------
#option 7: Calculate distance between two points
def calculate_distance_between_points():
    print("\nCalculate Distance Between Two Points")
    print("First point:")
    x1 = int(input("Enter x coordinate: "))
    y1 = int(input("Enter y coordinate: "))
    print("\nSecond point:")
    x2 = int(input("Enter x coordinate: "))
    y2 = int(input("Enter y coordinate: "))
    distance = calculate_distance((x1, y1), (x2, y2))
    print(f"\nDistance between the points: {distance:.2f} units")

#-------------------------------------------------------------------------------------------------------------------------------------------

def main():
    g = create_quadtree_graph(4)  
    quadtree = file_handling(g)  
    introduce_project()
    # main interaction loop
    while True:
        display_tasks()
        task_choice = get_task_choice()
        if  task_choice == 1:
            view_farm_data(quadtree)
        elif task_choice == 2:
            perform_range_query(quadtree)
        elif task_choice == 3:
            perform_intersection_check(quadtree)
        elif task_choice == 4:
            perform_update(quadtree)
        elif task_choice == 5:
            perform_delete_region(quadtree)
        elif task_choice == 6:
            calculate_averages(quadtree)
        elif task_choice == 7:
            calculate_distance_between_points()
        elif task_choice == 8:
            print("\nExiting the program.")
            print("\nThank you for using Meri Mitti. Goodbye!")
            break

if __name__ == "__main__":
    main()
