

class Pet:

    def __init__(self,
                 color: str,
                 start_x: int,
                 start_y: int,
                 max_move: int,
                 max_dist: int | None = None,
                 counter: bool = False
                 ) -> None:
        self.color: str = color
        self.start_x: int = start_x
        self.start_y: int = start_y
        self.max_move: int = max_move
        self.max_dist: int = max_dist
        self.counter: bool = counter

        self.curr_x: int = self.start_x
        self.curr_y: int = self.start_y
        self.all_coords: list[tuple[int, int]] = [(self.start_x, self.start_y)]

    def move(self) -> None:
        pass