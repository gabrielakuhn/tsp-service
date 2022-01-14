"""Simple Travelling Salesperson Problem (TSP) between cities."""

# Original code in https://developers.google.com/optimization/routing/tsp
# Some parts of this code was modified to fit the assigment - Gabriela Kuhn Jan 2022

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def create_data_model(dis_matrix):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = dis_matrix    # Returning data from tsp service -> Modified by Kuhn - Jan 2022
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def return_solution(manager, routing, solution):
    """Prints solution on console."""
    # Method was modified to return an array to print names of locations -> Modified by Kuhn - Jan 2022

    route_arr = []
    index = routing.Start(0)
    while not routing.IsEnd(index):
        index = solution.Value(routing.NextVar(index))
        route_arr.append(index)
    return route_arr


def tsp_main(dis_matrix):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(dis_matrix)    # Receiving data from tsp service -> Modified by Kuhn - Jan 2022

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        solution = return_solution(manager, routing, solution)
        return solution
