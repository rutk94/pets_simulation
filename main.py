import pandas as pd
import numpy as np
import datetime
import logging
from pathlib import Path

from pet import Pet
from utils import definelog

coords_path: Path = Path.cwd() / 'coordinates'
pets: list = ['cats_casual', 'cats_lazy', 'cats_pussies', 'mice']
iterations: int = 10
range_x: list[int] = [0, 100]
range_y: list[int] = [0, 100]

action_dist: int = 4

# start logger
log_date: str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir: Path = Path.cwd() / 'outputs'
log_path: Path = output_dir / f'{log_date}.log'
logger = definelog.Logger(log_path)
logger.define_logger()
logger.basic_fill()


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
             all_pets: list[Pet]
             ) -> pd.DataFrame:
    """
    Checking if actual positions of pets causes any action.
    If yes, actualize positions.
    :param pos_df: actual positions of pets as a row of pandas.DataFrame
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
                # mouse position
                mouse_x = int(pos_df.iloc[0, i].split(';')[0])
                mouse_y = int(pos_df.iloc[0, i].split(';')[1])

                # cat position
                cat_x = int(pos_df.iloc[0, j].split(';')[0])
                cat_y = int(pos_df.iloc[0, j].split(';')[1])

                # action
                if abs(mouse_x - cat_x) <= action_dist and abs(mouse_y - cat_y) <= action_dist:
                    mouse = all_pets[i]
                    cat = all_pets[j]
                    cat_kind: str = cat.name

                    logging.info(f'\tMeeting: {cat.name}({cat_x};{cat_y}) - {mouse.name}({mouse_x};{mouse_y})')

                    if 'cats_casual' in cat_kind:
                        mouse.back_to_start()
                        logging.info(f'\t{mouse.name} is back to start ({mouse.curr_x};{mouse.curr_y}')

                    elif 'cats_lazy' in cat_kind:
                        cat.count()
                        if cat.if_interested():
                            mouse.back_to_start()
                            logging.info(f'\t{mouse.name} is back to start ({mouse.curr_x};{mouse.curr_y})')

                    elif 'cats_pussies' in cat_kind:
                        # meeting in cats box area
                        if mouse_x <= cat.start_x + cat.courage_dist \
                                and mouse_y <= cat.start_y + cat.courage_dist:
                            mouse.back_to_start()
                            logging.info(f'\t{mouse.name} is back to start ({mouse.curr_x};{mouse.curr_y})')

                        # meeting anywhere else
                        else:
                            cat.back_to_start()
                            logging.info(f'\t{cat.name} is back to start ({cat.curr_x};{cat.curr_y})')

                    new_pos_df.iloc[0, i] = f'{mouse.curr_x};{mouse.curr_y}'
                    new_pos_df.iloc[0, j] = f'{cat.curr_x};{cat.curr_y}'

                # no action
                else:
                    continue

    new_pos_df.reset_index(inplace=True)

    return new_pos_df


def main():

    # create output dir
    if not output_dir.exists():
        Path.mkdir(output_dir, parents=True)

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
        max_dist=50,
        range_x=range_x,
        range_y=range_y,
        courage_dist=25,
    )

    mice: list = _create_objects(
        name=pets[3],
        color='blue',
        max_move=1,
        range_x=range_x,
        range_y=range_y
    )

    all_pets: list = cats_casual + cats_lazy + cats_pussies + mice

    # create 1st row (start positions)
    start_dict: dict[str, str] = dict(zip(
        [all_pets[i].name for i in range(len(all_pets))],
        [[f'{all_pets[i].start_x};{all_pets[i].start_y}'] for i in range(len(all_pets))]
    ))
    df: pd.DataFrame = pd.DataFrame(
        start_dict
    )
    df.reset_index(inplace=True)

    # simulation algorythm
    for i in range(1, iterations):
        logging.info(f'Day: {i}')

        # all pets moving - one by one
        for single_pet in all_pets:
            single_pet.move()
            df.loc[i, 'index'] = i
            df.loc[i, single_pet.name] = f'{single_pet.curr_x};{single_pet.curr_y}'

        last_row: pd.DataFrame = (df.where(df.loc[:, 'index'] == i)
                                  .dropna(subset='index')
                                  .drop('index', axis=1)
                                  )
        new_last_row = _actions(pos_df=last_row, all_pets=all_pets)
        df.iloc[i] = new_last_row.iloc[0]


if __name__ == '__main__':
    main()
