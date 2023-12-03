import math
import random as rd


class Pet:
    def __init__(self,
                 name: str,
                 color: str,
                 start_x: int,
                 start_y: int,
                 range_x: tuple[int, int],
                 range_y: tuple[int, int],
                 max_move: int,
                 max_dist: int | None = None,
                 counter: bool = False
                 ) -> None:
        self.name: str = name
        self.color: str = color
        self.start_x: int = start_x
        self.start_y: int = start_y
        self.range_x: tuple[int, int] = range_x
        self.range_y: tuple[int, int] = range_y
        self.max_move: int = max_move
        self.max_dist: int = max_dist
        self.counter: bool = counter

        self.all_coords: list[tuple[int, int]] = [(self.start_x, self.start_y)]
        self.curr_x: int = self.all_coords[-1][0]
        self.curr_y: int = self.all_coords[-1][1]

        self.n: int | None = 0 if self.counter is True else None

    def move(self) -> None:
        while True:
            try:
                step_x: int = rd.randint(-self.max_move, self.max_move)
                step_y: int = rd.randint(-self.max_move, self.max_move)
                assert self.range_x[0] < step_x < self.range_x[1]
                assert self.range_y[0] < step_y < self.range_y[1]
            except AssertionError:
                continue
            else:
                self.curr_x += step_x
                self.curr_y += step_y
                break

        self.all_coords.append((self.curr_x, self.curr_y))

    def back_to_start(self) -> None:
        self.curr_x = self.start_x
        self.curr_y = self.start_y
        self.all_coords.append((self.curr_x, self.curr_y))

    def back_one_step(self) -> None:
        self.curr_x = self.all_coords[-2][0]
        self.curr_y = self.all_coords[-2][1]
        self.all_coords.pop(-1)
        self.all_coords.append((self.curr_x, self.curr_y))

    def if_interested(self) -> bool:
        if self.counter is True and self.n is not None:
            prob: float = (1 / (1 + math.e ** (-0.1 * self.n)))
            return rd.random() < prob

    def count(self) -> None:
        if self.counter is True and self.n is not None:
            self.n += 1
