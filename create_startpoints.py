import random as rd
from pathlib import Path


def _random_coords(max_value: int = 100, n: int = 3) -> list[str]:
    return [f'{rd.randint(1, max_value)} {rd.randint(1, max_value)}' for _ in range(n)]


def create(dest_path: Path, n: int) -> None:
    coords_list: list[str] = _random_coords(max_value=100, n=n)

    if not dest_path.parent.exists():
        Path.mkdir(dest_path.parent, parents=True)

    with open(dest_path, 'w+') as file:
        for coords in coords_list:
            file.write(f'{coords}\n')


names_amounts: dict[str, int] = {
    'cats_pussys': 3,
    'cats_lazy': 3,
    'cats_casual': 3,
    'mice': 3
}
for name, amount in names_amounts.items():
    file_path: Path = Path.cwd() / 'coordinates' / f'{name}.txt'
    create(file_path, amount)
