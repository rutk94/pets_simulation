from pathlib import Path

from pet import Pet

coords_path: Path = Path.cwd() / 'coordinates'
pets: list = ['cats_casual', 'cats_lazy', 'cats_pussies', 'mice']
iterations: int = 5


def create_objects(name: str, **kwargs) -> list:
    """
    Creates list of objects from class Pet by opening files with starting coordinates.
    :param name: pet name
    :param kwargs: color, start_x, start_y, max_move, max_dist, counter
    :return: list of Pet objects
    """

    result: list = []
    with open(coords_path / f'{name}.txt', 'r') as file:
        nr: int = 0
        for line in file:
            nr += 1
            coords: list = line.strip().split(' ')
            pet_object: Pet = Pet(
                    name=f'{name}_{nr}',
                    start_x=int(coords[0]),
                    start_y=int(coords[1]),
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

    all_pets: list = cats_casual + cats_lazy + cats_pussies + mice

    # create pandas.DataFrame


    # simulation algorithm
    # for i in range(iterations):
    #     # moves
    #     for m in range(len(mice)):
    #         mice[m].move()
    #
    #     for cc in range(len(cats_casual)):
    #         cats_casual[cc].move()
    #
    #     for cl in range(len(cats_lazy)):
    #         cats_lazy[cl].move()
    #
    #     for cp in range(len(cats_pussies)):
    #         cats_pussies[cp].move()

        # check positions


        # if cat meets mouse


    # print(mice[0].all_coords, mice[0].curr_x, mice[0].curr_y)
    # mice[0].move()
    # print(mice[0].all_coords, mice[0].curr_x, mice[0].curr_y)

    print(mice[0].name)


if __name__ == '__main__':
    main()
