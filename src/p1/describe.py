import argparse
import pandas as pd

from utils.stats import *


def describe_dataset(dataset):
    """
    Ici, on utilise les dictionnaires en pyhton, ce qui nous permet
    d'associer des fonctions à des "numéros" et des tableaux afin de stocker les résultats.
    Très pratique pour ce qui est demandé :
                feature x    feature n      ...
    fonction    résultat 1   résultat n     ...
    """
    fn_dict = {
        0: count,
        1: mean,
        2: std,
        3: min,
        4: quartile_low,
        5: quartile_med,
        6: quartile_high,
        7: max,
        8: freq,
        9: unique,
    }
    rows = {
        "Count": [],
        "Mean": [],
        "Std": [],
        "Min": [],
        "25%": [],
        "50%": [],
        "75%": [],
        "Max": [],
        "Frequency": [],
        "Unique": []
    }
    cols_empty = [
        col for col in dataset.columns if dataset[col].isnull().all()]
    dataset.drop(cols_empty, axis=1, inplace=True)
    data = dataset.select_dtypes("float64")
    # ici on vient boucler pour lire toutes nos données et les associés
    # au bon numéro/tableau instancié au préalable dans notre dict
    for col in data.columns:
        lister = list(data[col])
        for i, elem in enumerate(rows):
            rows[elem].append(fn_dict[i](lister))
    cols = list(data.columns)
    df = pd.DataFrame.from_dict(rows, orient="index", columns=cols)
    print(df)


def open_datafile(df):
    """
    Simple fonction permettant de lire un fichier csv => ici notre dataset_train.csv
    """
    try:
        df_ = pd.read_csv(df)
    except pd.errors.EmptyDataError or pd.errors.ParserError:
        exit("Error")
    except Exception:
        exit("Error")
    return df_


if __name__ == "__main__":
    # ici on vient prendre en compte notre argument pour le parser (en l'occurence notre csv)
    parser = argparse.ArgumentParser(
        description="")
    parser.add_argument("dataset", type=open_datafile,
                        help="")
    args = parser.parse_args()
    try:
        describe_dataset(args.dataset)
    except Exception:
        print("Error")
