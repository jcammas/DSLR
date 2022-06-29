import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse


def get_dataset_LogReg(dataset):
    """Extraction du dataset et suppression elements useless"""
    dataset = pd.read_csv(dataset)
    dataset = dataset.fillna(0)
    y = dataset['Hogwarts House']
    dataset = dataset[dataset.columns[6:19]]
    dataset = dataset.drop('Astronomy', axis=1)
    dataset = dataset.drop('Defense Against the Dark Arts', axis=1)
    dataset = dataset.drop('Arithmancy', axis=1)
    dataset = dataset.drop('Care of Magical Creatures', axis=1)
    dataset = dataset.drop('Potions', axis=1)
    return dataset, y


def get_theta_from_csv():
    """extraction des thetas depuis le fichier csv"""
    thetas = pd.read_csv("thetas.csv")
    theta_g = thetas['Gryffindor']
    theta_s = thetas['Slytherin']
    theta_r = thetas['Ravenclaw']
    theta_h = thetas['Hufflepuff']
    return theta_g, theta_s, theta_r, theta_h

#-----------------------------------------------------------------------------------#
# Initalisation du parseur d'arguments


parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset for prediction")
options = parser.parse_args()

#
#-----------------------------------------------------------------------------------#


def StandardScaler(X):
    """Scaling de la data avant la regression logistique"""
    mean = np.mean(X, axis=0)
    scale = np.std(X - mean, axis=0)
    return (X - mean) / scale


def predict(X, theta):
    z = np.dot(X, theta)
    sig = 1 / (1 + np.exp(-z))
    return sig


if __name__ == "__main__":
    #--------------------------------------------------------------#
    # Extraction et preparation de la data
    dataset, y = get_dataset_LogReg(options.dataset)
    X = np.array(dataset)
    X = StandardScaler(X)
    X = np.c_[np.ones(X.shape[0]), X]
    theta_g, theta_s, theta_r, theta_h = get_theta_from_csv()
    #
    #--------------------------------------------------------------#
    prediction = []
    pred_g = predict(X, theta_g)
    pred_s = predict(X, theta_s)
    pred_r = predict(X, theta_r)
    pred_h = predict(X, theta_h)
    for i in range(len(pred_g)):
        grade = 0
        house = 0
        if pred_g[i] > pred_s[i]:
            grade = pred_g[i]
            house = 'Gryffindor'
        else:
            grade = pred_s[i]
            house = 'Slytherin'
        if pred_r[i] > grade:
            grade = pred_r[i]
            house = 'Ravenclaw'
        if pred_h[i] > grade:
            grade = pred_h[i]
            house = 'Hufflepuff'
        prediction.append(house)
    prediction = np.array(prediction)
    prediction = pd.DataFrame(prediction, columns=['Hogwarts House'])
    prediction = prediction.rename_axis('Index', axis=0)
    prediction.to_csv('houses.csv')
