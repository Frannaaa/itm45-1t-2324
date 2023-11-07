'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    follows = to_member in social_graph[from_member]["following"]
    followed_by = from_member in social_graph[to_member]["following"]
    
    #If follow each other
   follows = to_member in social_graph[from_member]["following"]
   followed_by = from_member in social_graph[to_member]["following"]
    
    if follows and followed_by:
        return "friends"
    elif follows:
        return "follower"
    elif followed_by:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
     size = len(board)
    
    # Chek rows and columns
    for i in range(size):
        if len(set(board[i])) == 1 and board[i][0] != ' ':
            return board[i][0]
        if len(set([board[j][i] for j in range(size)])) == 1 and board[0][i] != ' ':
            return board[0][i]
    
    # Check diagonals
    if len(set([board[i][i] for i in range(size)])) == 1 and board[0][0] != ' ':
        return board[0][0]
    if len(set([board[i][size - 1 - i] for i in range(size)])) == 1 and board[0][size - 1] != ' ':
        return board[0][size - 1]
    
    # If no winner, return "NO WINNER"
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    
    # Find starting leg
    current_leg = next(((start, end) for (start, end) in route_map if start == first_stop), None)
    
    # If starting leg doesn't exist, return 0 bc cannot calculate ETA
    if not current_leg:
        return 0
    
    # Loop til second stop is reached
    while current_leg[1] != second_stop:
        # Add travel time of current leg-olas 
        travel_time += route_map[current_leg]["travel_time_mins"]
        
        # Move to next leg
        current_leg = next(((start, end) for (start, end) in route_map if start == current_leg[1]), None)
        
        # If looped around to first stop without finding second stop, break
        if not current_leg or current_leg[0] == first_stop:
            return 0
    
    # Add travel time of last leg to reach second stop
    travel_time += route_map[current_leg]["travel_time_mins"]
    
    return travel_time
