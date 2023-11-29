from pathlib import Path

from pet import Pet

coords_path: Path = Path.cwd() / 'coordinates'
pets: list = ['cats_casual', 'cats_lazy', 'cats_pussies', 'mice']


def create_objects(name: str, **kwargs) -> list:
    """
    Creates list of objects from class Pet by opening files with starting coordinates.
    :param name: pet name
    :param kwargs: color, start_x, start_y, max_move, max_dist, counter
    :return: list of Pet objects
    """

    result: list = []
    with open(coords_path / f'{name}.txt', 'r') as file:
        for line in file:
            coords: list = line.strip().split(' ')
            pet_object: Pet = Pet(
                    start_x=coords[0],
                    start_y=coords[1],
                    **kwargs
                )
            result.append(pet_object)

    return result


def main():

    # create lists of Pet objects
    cats_casual: list = create_objects(
        name=pets[0],
        color='yellow',
        max_move=10
    )

    cats_lazy: list = create_objects(
        name=pets[1],
        color='red',
        max_move=10,
        counter=True
    )

    cats_pussies: list = create_objects(
        name=pets[2],
        color='orange',
        max_move=5,
        max_dist=100
    )

    mice: list = create_objects(
        name=pets[3],
        color='blue',
        max_move=1,
    )


if __name__ == '__main__':
    main()
