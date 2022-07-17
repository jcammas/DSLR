import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def pair_plot():
    plt.figure()

    # https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
    sns.set(style="whitegrid", color_codes=True)

    # ici on prépare notre dataset en le récupérant depuis notre argument
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=str, help="input dataset")
    options = parser.parse_args()
    dataset = pd.read_csv(options.dataset)
    # dataset = dataset.drop('Astronomy', axis='columns')
    # dataset = dataset.drop('Defense Against the Dark Arts', axis='columns')

    # on configure notre affichage
    sns.pairplot(dataset, hue='Hogwarts House', markers="+")

    # on affiche notre graphique final
    plt.show()


if __name__ == "__main__":

    pair_plot()

#######

# Q:    À partir de cette visualisation, quelles caractéristiques
#       allez-vous utiliser pour entraîner votre prochaine régression logistique ?
# A:    On cherche à conserver les cours qui ont un résultat relativement hétérogène afin d'avoir une différence marquée entre les maisons (si le résultat est homogène, ça devient compliquer de les différenciers nettement etc)
#       Ainsi on veut éliminer : Astronomy / Defense Against the Dark Arts / Arithmancy / Care of Magical Creatures / Potions
