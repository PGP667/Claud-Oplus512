class Nim:
    """Represents a game of Nim where players take turns removing matches.

    Attributes:
        initial_matches (int): The initial number of matches in the game.
        matches (int): The current number of matches remaining.
        turn (int): The current turn count.
        last_move (int | None): The number of matches taken in the last move.
        current_player (int): The player whose turn it is (0 or 1).
        is_over (bool): Whether the game has finished.
        winner (int | None): The winning player (0 or 1), or None if game is ongoing.
    """

    def __init__(self, initial_matches: int = 10):
        """Initialize the Nim game.

        Args:
            initial_matches (int): The starting number of matches. Defaults to 10.
        """
        self.initial_matches = initial_matches
        self.reset()

    def reset(self):
        """Reset the game to its initial state.

        Returns:
            list: The initial game state formatted as [turn, matches, last_move, possible_moves].
        """
        self.matches = self.initial_matches
        self.turn = 0
        self.last_move = None
        self.current_player = 0
        self.is_over = False
        self.winner = None

        return self.get_state()

    def get_state(self):
        """Get the current game state.

        Returns:
            list: A list containing:
                - turn (int): Number of turns elapsed.
                - matches (int): Remaining matches.
                - last_move (int | None): Matches taken in the last move.
                - possible_moves (list[int]): Valid moves available for the current player.
        """
        possible_moves = []

        if not self.is_over:
            possible_moves = [
                choice for choice in [1, 2]
                if choice <= self.matches
            ]

        return [
            self.turn,
            self.matches,
            self.last_move,
            possible_moves
        ]

    def play(self, choice: int):
        """Make a move by removing a specified number of matches.

        Args:
            choice (int): The number of matches to remove (1 or 2).

        Returns:
            list: The updated game state.

        Raises:
            ValueError: If the game is already over or the choice is invalid.
        """
        if self.is_over:
            raise ValueError("The game is already over.")

        if choice not in self.get_state()[3]:
            raise ValueError(f"Invalid move: {choice}")

        self.matches -= choice
        self.last_move = choice
        self.turn += 1

        if self.matches == 0:
            self.is_over = True
            self.winner = self.current_player
        else:
            self.current_player = 1 - self.current_player

        return self.get_state()