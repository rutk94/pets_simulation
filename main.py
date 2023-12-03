import pandas as pd
import numpy as np
from pathlib import Path

from pet import Pet

coords_path: Path = Path.cwd() / 'coordinates'
pets: list = ['cats_casual', 'cats_lazy', 'cats_pussies', 'mice']
iterations: int = 5
range_x: tuple[int, int] = (0, 100)
range_y: tuple[int, int] = (0, 100)


def _create_objects(name: str, **kwargs) -> list:
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


def _actions(pos_df: pd.DataFrame,
             # pet: Pet,
             all_pets: list[Pet]
             ) -> pd.DataFrame:
    """
    Checking if actual positions of pets causes any action.
    If yes, actualize positions.
    :param pos_df: actual positions of pets as a row of pandas.DataFrame
    # :param pet: single Pet object to check
    :param all_pets: all Pet objects
    :return: positions of pets after actions as a row of pandas.DataFrame
    """
    new_pos_df: pd.DataFrame = pos_df.copy()

    for i in range(len(pos_df.columns)):
        if pets[3] not in all_pets[i].name:     # pets[3] = 'mice'
            continue

        for j in range(len(pos_df.columns)):
            if pets[3] in all_pets[j].name:     # pets[3] = 'mice'
                continue

            else:
                # mice position
                mouse_x = pos_df.iloc[0, i].split(';')[0]
                mouse_y = pos_df.iloc[0, i].split(';')[1]

                # cat position
                cat_x = pos_df.iloc[0, j].split(';')[0]
                cat_y = pos_df.iloc[0, j].split(';')[1]

                # action
                if abs(mouse_x - cat_x) <= 4 or abs(mouse_y - cat_y) <= 4:
                    pass

                # no action
                else:
                    continue

    return new_pos_df


def main():

    # create lists of Pet objects
    cats_casual: list = _create_objects(
        name=pets[0],
        color='yellow',
        max_move=10,
        range_x=range_x,
        range_y=range_y
    )

    cats_lazy: list = _create_objects(
        name=pets[1],
        color='red',
        max_move=10,
        counter=True,
        range_x=range_x,
        range_y=range_y
    )

    cats_pussies: list = _create_objects(
        name=pets[2],
        color='orange',
        max_move=5,
        max_dist=100,
        range_x=range_x,
        range_y=range_y
    )

    mice: list = _create_objects(
        name=pets[3],
        color='blue',
        max_move=1,
        range_x=range_x,
        range_y=range_y
    )

    all_pets: list = cats_casual + cats_lazy + cats_pussies + mice

    # create pandas.DataFrame
    cols: list[str] = [all_pets[i].name for i in range(len(all_pets))]
    df: pd.DataFrame = pd.DataFrame(
        data=np.array([[None]*len(all_pets)]*iterations),
        columns=cols
    )

    # simulation algorythm
    for i in range(iterations):

        # all pets moving - one by one
        for single_pet in all_pets:
            single_pet.move()
            df.loc[i, single_pet.name] = f'{single_pet.curr_x};{single_pet.curr_y}'

            # actions caused by one move
            if pets[3] in single_pet.name:  # pets[3] = 'mice'
                df.iloc[-1] = _actions(pos_df=df.iloc[-1], all_pets=all_pets)

        # new position checking algorythm

    print(df)

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
