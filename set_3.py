'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
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
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def relationship_status(from_member, to_member, social_graph):

        from_follows_to = to_member in social_graph[from_member]["following"] 
            # checks if "to_member" is following "from_member" using the dictionary and indexing 
            # returns true or false, stored in the value "from_follows_to"
        to_follows_from = from_member in social_graph[to_member]["following"] 
            # checks if "from_member" is following "to_member" using the dictionary and indexing 
            # returns true or false, stored in the value "to_follows_from" 

        if from_follows_to and to_follows_from: # if both "from_follows_to" and "to_follows_from" are true (they follow each other)
            return "friends" # then it returns "friends"
        elif from_follows_to: # if only "from_member" follows "to_member" (from_follows_to is true)
            return "follower" # then it returns "follower"
        elif to_follows_from: # if only "to_member" follows "from_member" (to_follows_from is true)
            return "followed by" # then it returns "followed by"
        else: # otherwise, if neither follows the other
            return "no relationship" # then it returns "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
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
    def tic_tac_toe(board):
        size = len(board) # defines the size of the board, since it is a square, it gives both the number of rows and columns

        for row in board: # loops through every row in the board,
            if row[0] != '' and all(symbol == row[0] for symbol in row): # if the first space in the row is not empty, and every symbol in that row is the same as the symbol in the first space
                return row[0] # then return the symbol in the first space

        for col in range(size): # loops through every column index from 0 to size-1 in the board
            column = [board[row][col] for row in range(size)] 
                # defines what a column is
                    # for row in range(size) loops through each row
                    # board[row][col] (for each row) grabs the value in the column col
                # combines it all to say: for every row, it grabs the nth index, which defines a column
            if column[0] != '' and all(symbol == column[0] for symbol in column): # if the first space in the column is not empty, and every symbol in that column is the same as the symbol in the first space
                return column[0] # then return the symbol in the first space

        first = board[0][0] # defines "first" as the top-left space in the board
        if first != '' and all(board[i][i] == first for i in range(size)): # if the first space in the column is not empty, and every symbol in the board diagonally from top-left to bottom-right where row index equals column index (i, i) is the same as the symbol in the first place
            return first # then return the symbol in the first space

        first = board[0][size - 1] # defines "first" as the top-right space in the board
        if first != '' and all(board[i][size - 1 - i] == first for i in range(size)): # if the first space in the column is not empty, and every symbol in the board diagonally from top-right to bottom-left where coordinates follow (i, size - 1 - i) is the same as the symbol in the first place
            return first # then return the symbol in the first space

        return "NO WINNER" # returns "NO WINNER" when none of the previous conditions were met

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
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
    def eta(first_stop, second_stop, route_map):
        total_time = 0 # initializes the variable "total_time" to track the total travel time from "first_stop" to "second_stop"; starts at 0, time is added for each leg travelled
        current_stop = first_stop # sets the "current_stop" as the starting point of the journey, the variable will update as the shuttle travels through each leg

        while current_stop != second_stop: 
            # loops through checking if the "current_stop" is not equal to "second_stop"
            # as long as the condition is true ("current_stop" is not equal to "second_stop"), then continue with the code
            for (start, end), travel_info in route_map.items(): 
                # loops through each route leg in "route_map"
                    # (start, end) is a tuple key representing the start stop and the end stop of a one-way leg
                    # travel_info is a dictionary containing travel details, including the key "travel_time_mins" and its corresponding integer value
                if start == current_stop: # loops through checking if the current leg starts at the current stop
                    total_time += travel_info["travel_time_mins"] # if it does, accesses the integer value corresponding with "travel_time_mins" from "travel_info" and adds that to "total_time"
                    current_stop = end # updates the "current_stop" to the end stop
                    break 
                        # breaks out of the inner for loop to return to the while loop, even if the loop condition isn't finished yet
                            # this is done because only one leg is needed, and once it is found, you don't have to keep looping to look for it

        return total_time # returns the final total travel time