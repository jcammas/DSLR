import numpy as np
import pandas as pd
import argparse


def add_intercept(x: np.ndarray, axis: int = 1) -> np.ndarray:
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None
    ones = np.ones((x.shape[0], 1))
    res = np.concatenate((ones, x), axis=axis)
    return res


def StandardScaler(X):
    """
    StandardScaler performs the task of Standardization.
    Our dataset contains variable values that are different in scale.
    As these two columns are different in scale, they are Standardized
    to have a common scale while building a machine learning model.
    """
    mean = np.mean(X, axis=0)
    scale = np.std(X - mean, axis=0)
    return (X - mean) / scale


def sigmoid_(x: np.ndarray) -> np.ndarray:
    """
    Compute the sigmoid of a vector.
    Args:
    x: has to be an numpy.array, a vector
    Return:
    The sigmoid value as a numpy.array.
    None otherwise.
    Raises:
    This function should not raise any Exception.
    """
    return 1 / (1 + np.exp(-x))


def predict(x, theta):
    y = sigmoid_(x.dot(theta))
    return y


if __name__ == "__main__":
    # ici on prépare notre dataset en le récupérant depuis notre argument
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=str, help="pred")
    options = parser.parse_args()

    # ici on récupère notre dataset (notre csv passé en paramètre)
    dataset = pd.read_csv(options.dataset)

    # on le prépare afin de récupérer ce dont on a besoin
    dataset = dataset.fillna(0)
    y = dataset['Hogwarts House']

    # seul les colonnes [a:b] nous intéressent
    dataset = dataset[dataset.columns[6:19]]

    # on veut effacer les cours qui ne seront pas pertinents (cf. pair plot)
    dataset = dataset.drop('Astronomy', axis=1)
    dataset = dataset.drop('Defense Against the Dark Arts', axis=1)
    dataset = dataset.drop('Arithmancy', axis=1)
    dataset = dataset.drop('Care of Magical Creatures', axis=1)
    dataset = dataset.drop('Potions', axis=1)

    X = np.array(dataset)
    X = StandardScaler(X)
    X = add_intercept(X, axis=1)

    # ici on récupère les valeurs de nos thetas grâce au csv créé via train
    thetas = pd.read_csv("thetas.csv")

    # on initialise ces derniers
    theta_Gryffindor = thetas['Gryffindor']
    theta_Slytherin = thetas['Slytherin']
    theta_Ravenclaw = thetas['Ravenclaw']
    theta_Hufflepuff = thetas['Hufflepuff']

    # on commence notre pred
    prediction = []

    # On fait la prediction au cas par cas
    pred_Gryffindor = predict(X, theta_Gryffindor)
    pred_Slytherin = predict(X, theta_Slytherin)
    pred_Ravenclaw = predict(X, theta_Ravenclaw)
    pred_Hufflepuff = predict(X, theta_Hufflepuff)

    # on agit en fonction de nos résultats (on vient chercher les notes, on fait un diff et on assigne en fonction de ça)
    for i in range(len(pred_Gryffindor)):
        grade = 0
        house = 0
        if pred_Gryffindor[i] > pred_Slytherin[i]:

            print("pred gryff :", pred_Gryffindor[i])
            print("pred slyth :", pred_Slytherin[i])

            grade = pred_Gryffindor[i]
            house = 'Gryffindor'

        else:
            grade = pred_Slytherin[i]
            house = 'Slytherin'
        if pred_Ravenclaw[i] > grade:
            grade = pred_Ravenclaw[i]
            house = 'Ravenclaw'
        if pred_Hufflepuff[i] > grade:
            grade = pred_Hufflepuff[i]
            house = 'Hufflepuff'

        prediction.append(house)

    # on paramètre notre houses.csv qui affichera les maisons données aux moldus, ou aux pas moldus je sais plus ?
    prediction = np.array(prediction)
    prediction = pd.DataFrame(prediction, columns=['Hogwarts House'])
    prediction = prediction.rename_axis('Index', axis=0)
    prediction.to_csv('houses.csv')
