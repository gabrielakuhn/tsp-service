import json

from compute_distance import compute_distance_matrix
from tsp import tsp_main

def convert_to_json(bytes_value):
    """Method to convert bytes value to Python list"""

    # Decode UTF-8 bytes to Unicode, and convert single quotes
    # to double quotes to make it valid JSON
    json_data = bytes_value.decode('utf8').replace("'", '"')

    # Load the JSON to a Python list
    data = json.loads(json_data)
    return data

def tsp_service(data):
    """Method to compute and return route plan"""

    locations = convert_to_json(data)   # Getting data and load as json
    distance = compute_distance_matrix(locations)   # Creating distance matrix
    route = tsp_main(distance)  # Computing route
    plan_route = print_location_name(locations, route)  # Generating array with locations names
    return plan_route

def print_location_name(locations, route):
    """Method to get array with route index and check the locations names to print"""

    tam = len(route)
    plan_output = []
    plan_output.append(str(locations[0]["name"])) # Route start
    for i in route:
        if i < tam: # This statement is to cheat the array "+1" difference without interfering in the route
            plan_output.append(str(locations[i]["name"]))
        else:
            plan_output.append(str(locations[0]["name"])) # Route end
    return (plan_output)