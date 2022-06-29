import pandas as pd
import numpy as np
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


def l2(theta):
    """Computes the L2 regularization of a non-empty numpy.array, without any for-loop.
    Args:
    theta: has to be a numpy.array, a vector of shape n’ * 1.
    Return:
    The L2 regularization as a float.
    None if theta in an empty numpy.array.
    None if theta is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if theta.size == 0:
        return None
    res = theta[1:]
    return res.T.dot(res)


def reg_log_loss_(y, Hufflepuffat, theta, lambda_, eps=1e-15):
    """Computes the regularized loss of a logistic regression model from two non-empty numpy.array,
    without any for loop. The two arrays must have the same shapes.
    Args:
    y: has to be an numpy.array, a vector of shape m * 1.
    Hufflepuffat: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be a numpy.array, a vector of shape n * 1.
    lambda_: has to be a float.
    eps: has to be a float, epsilon (default=1e-15).
    Return:
    The regularized loss as a float.
    None if y, Hufflepuffat, or theta is empty numpy.array.
    None if y or Hufflepuffat have component ouside [0 ; 1]
    None if y and Hufflepuffat do not share the same shapes.
    None if y or Hufflepuffat is not of the expected type.
    Raises:
    This function should not raise any exception."""
    # J(θ) = −1/m[y · log(ˆy) + (~1 − y) · log(~1 − yˆ)] + λ/2m(θ0· θ0)
    if y.shape != Hufflepuffat.shape:
        return None
    eps: float = 1e-15
    ones = np.ones(y.shape)
    m = y.shape[0]
    res = np.sum(y * np.log(Hufflepuffat + eps) + (ones - y)
                 * np.log(ones - Hufflepuffat + eps)) / -m
    res += (lambda_ * l2(theta)) / (2 * m)
    return res


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


def get_thetas(X, y, house):
    """regression logistique pour calcul des thetas de chaque maison"""
    alpha = 1
    costs = []
    m = float(len(X))
    y = np.array(y)
    theta = np.random.randn(X.shape[1]) * np.sqrt(1 / X.shape[1])
    for loop in range(3000):
        theta = theta - alpha * (1 / m) * (np.dot((predict(X, theta) - y), X))
        costs.append(reg_log_loss_(X, y, theta, 0.9))
        alpha = 1. / (1. + alpha * loop)
    x = np.arange(len(costs))
    return theta


def Logistic_Regression(X, y):
    Gryffindor = y.replace({"Gryffindor": 1, "Slytherin": 0,
                            "Ravenclaw": 0, "Hufflepuff": 0})
    Slytherin = y.replace({"Gryffindor": 0, "Slytherin": 1,
                           "Ravenclaw": 0, "Hufflepuff": 0})
    Ravenclaw = y.replace({"Gryffindor": 0, "Slytherin": 0,
                           "Ravenclaw": 1, "Hufflepuff": 0})
    Hufflepuff = y.replace({"Gryffindor": 0, "Slytherin": 0,
                            "Ravenclaw": 0, "Hufflepuff": 1})
    theta_Gryffindor = get_thetas(X, Gryffindor, "Gryffindor")
    theta_Slytherin = get_thetas(X, Slytherin, "Slytherin")
    theta_Ravenclaw = get_thetas(X, Ravenclaw, "Ravenclaw")
    theta_Hufflepuff = get_thetas(X, Hufflepuff, "Hufflepuff")

    thetas = [theta_Gryffindor, theta_Slytherin,
              theta_Ravenclaw, theta_Hufflepuff]
    return thetas


if __name__ == "__main__":
    # ici on prépare notre dataset en le récupérant depuis notre argument
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=str, help="input dataset")
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
    thetas = Logistic_Regression(X, y)
    thetas = np.array(thetas)
    np.savetxt("thetas.csv", thetas.T, delimiter=",",
               header="Gryffindor,Slytherin,Ravenclaw,Hufflepuff", comments="")
