class GameException(Exception):
    """Exception raised for not valid move.
    """

    def __init__(self, message="Move not valid"):
        self.message = message
        super().__init__(self.message)


class NotValidMove(GameException):
    """Exception raised for not valid move.
    """

    def __init__(self, message="Move not valid"):
        self.message = message
        super().__init__(self.message)


class ValidMoveNotExists(GameException):
    """Exception raised for not available valid move.
    """

    def __init__(self, message="Valid move not exists"):
        self.message = message
        super().__init__(self.message)


class GameOver(GameException):
    """Exception raised when game is over.
    """

    def __init__(self, message="Game over"):
        self.message = message
        super().__init__(self.message)
