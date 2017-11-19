"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import isolation

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    
    raise NotImplementedError


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    raise NotImplementedError


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    raise NotImplementedError


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """


    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    
    def minimax(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        else:
            '''
            action, state = argmax(game.successors(state),
                           lambda ((a, s)): min_value(s))
            '''
            return self.Min_Value(game.forecast_move(legal_moves[0]),depth-1)

        raise NotImplementedError
    #using exclusive recurrsive techniques
    #prepare variables used in max and min value function
    

    def Max_Value(self,gameStatus, currentDepth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # v = -infinity
        max_highest_score_so_far = float("-inf")
        max_best_move_so_far = (-1, -1)
        player_legal_moves = gameStatus.get_legal_moves()
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        max_level_score = None
        if currentDepth == 1:  # handle the situation of level 1
            for move in player_legal_moves:
                # Evaluate this move.
                max_level_score = self.score(
                    gameStatus.forecast_move(move), self)
                # If this is a winning move, no need to search further. Otherwise, remember the best move.
                if max_level_score == float("inf"):
                    return max_level_score, move
                if max_level_score > max_highest_score_so_far:
                    max_highest_score_so_far, max_best_move_so_far = max_level_score, move
            return max_highest_score_so_far, max_best_move_so_far
        else:
            for move in player_legal_moves:
                # Evaluate this move in depth.
                max_level_score, _ = self.Min_Value(
                    gameStatus.forecast_move(move), currentDepth - 1)
                # If this branch yields a sure win, no need to search further. Otherwise, remember the best move.
                if max_level_score == float("inf"):
                    return max_level_score, move
                if max_level_score > max_highest_score_so_far:
                    highest_score_so_far, best_move_so_far = max_level_score, move
            return highest_score_so_far, best_move_so_far

    def Min_Value(self,gameStatus, currentDepth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        min_lowest_score_so_far = float("inf"), float("-inf")
        min_best_move_so_far = (-1, -1)
        min_level_score = None
        player_legal_moves = gameStatus.get_legal_moves()
        if currentDepth == 1:
            for move in player_legal_moves:
                # Evaluate this move.
                score = self.score(gameStatus.forecast_move(move), self)
                # If this is a winning move, no need to search further. Otherwise, remember the best move.
                if min_level_score == float("-inf"):
                    return min_level_score, move
                
                if min_level_score < min_lowest_score_so_far:
                    min_lowest_score_so_far, min_best_move_so_far = min_level_score, move
            return min_lowest_score_so_far, min_best_move_so_far
        else:
            for move in player_legal_moves:
                # Evaluate this move in depth.
                min_level_score, _ = self.Max_Value(
                    gameStatus.forecast_move(move), currentDepth - 1)
                # If this branch yields a sure win, no need to search further. Otherwise, remember the best move.
                if min_level_score == float("-inf"):
                    return min_level_score, move
                if min_level_score < min_lowest_score_so_far:
                    min_lowest_score_so_far, min_best_move_so_far = min_level_score, move
            return min_lowest_score_so_far, min_best_move_so_far

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        # Did we just start the game? Then, of course, pick the center position.
        if game.move_count == 0:
            return(int(game.height / 2), int(game.width / 2))
        # Let's search for a good move!
        best_move_so_far = (-1, -1)
        
        iterative_search_depth = 1
        while True:
            best_score_so_far, best_move_so_far = self.alphabeta(game, iterative_search_depth)
            if best_score_so_far == float("inf") or best_score_so_far == float("-inf"):
                break
            iterative_search_depth += 1
        # Return the best move from the last completed search iteration
        return best_move_so_far

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        """
        # Body of alphabeta_search starts here:
         action, state = argmax(game.successors(state),lambda ((a, s)): min_value(s, -infinity, infinity))
         return action
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        else:
            return self.min_search(game.forecast_move(legal_moves[0]), depth, alpha=float("-inf"), beta=float("inf"))
    
    def max_search(self,gameStatus,currentDepth,alpha,beta):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # set variabes
        maximize_highest_score_so_far = float("-inf")  # v = -infinity
        maximize_best_move_so_far = (-1, -1)
        #get moves
        maximize_legal_moves = gameStatus.get_legal_moves()
        #dealing depth == 1 : end condition
        """
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -infinity
        for (a, s) in game.successors(state):
            v = max(v, min_value(s, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        """
        if currentDepth == 1:
            for move in maximize_legal_moves:
                # Evaluate this move.
                maximize_score = self.score(gameStatus.forecast_move(move), self)
                # If this is a score better than beta, no need to search further. Otherwise, remember the best move.
                if maximize_score >= beta:
                    return maximize_score, move
                if maximize_score > maximize_highest_score_so_far:
                    maximize_highest_score_so_far, maximize_best_move_so_far = maximize_score, move
            return maximize_highest_score_so_far, maximize_best_move_so_far
        else:
            for move in maximize_legal_moves:
                # Evaluate this move in depth.
                maximize_score, _ = self.min_search(gameStatus.forecast_move(
                    move), currentDepth - 1, alpha, beta)
                # If this branch yields a score better than beta, no need to search further.
                if maximize_score >= beta:
                    return maximize_score, move
                # Otherwise, remember the best move and update alpha.
                if maximize_score > maximize_highest_score_so_far:
                    maximize_highest_score_so_far, maximize_best_move_so_far = maximize_score, move
                alpha = max(alpha, maximize_highest_score_so_far)
            return maximize_highest_score_so_far, maximize_best_move_so_far
        
    def min_search(self, gameStatus, currentDepth,alpha,beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # set variabes
        minimize_lowest_score_so_far = float("inf")  # v = infinity
        minimize_best_move_so_far = (-1, -1)
        #get moves
        minimize_legal_moves = gameStatus.get_legal_moves()
        #dealing depth == 1 : end condition
        if currentDepth == 1:
            for move in minimize_legal_moves:
                # Evaluate this move.
                minimize_score = self.score(gameStatus.forecast_move(move), self)
                # If this is a score worse than alpha, no need to search further. Otherwise, remember the best move.
                if minimize_score <= alpha:
                    return minimize_score, move
                if minimize_score < minimize_lowest_score_so_far:
                        minimize_lowest_score_so_far, minimize_best_move_so_far = minimize_score, move
            return minimize_lowest_score_so_far, minimize_best_move_so_far
        else:
            """
            if game.terminal_test(state):
            return game.utility(state, player)
            v = infinity
            for (a, s) in game.successors(state):
                v = min(v, max_value(s, alpha, beta))
                if v <= alpha:
                return v
                beta = min(beta, v)
            return v
            """
            for move in minimize_legal_moves:
                # Evaluate this move in depth.
                minimize_score, _ = self.max_search(gameStatus.forecast_move(
                    move), currentDepth - 1, alpha, beta)
                # If this branch yields a score worse than alpha, no need to search further.
                if minimize_score <= alpha:
                    return minimize_score, move
                # Otherwise, remember the best move and update beta.
                if minimize_score < minimize_lowest_score_so_far:
                    minimize_lowest_score_so_far, minimize_best_move_so_far = minimize_score, move
                beta = min(beta, minimize_lowest_score_so_far)
            return minimize_lowest_score_so_far, minimize_best_move_so_far
