import matplotlib.pyplot as plt
import pandas as pd
import argparse


def plot_hist():

    # ici on prépare notre dataset en le récupérant depuis notre argument
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=str, help='input dataset')
    options = parser.parse_args()
    df = pd.read_csv(options.dataset)

    # on veut récupérer les données qu'à partir de la colonne
    grade = df[df.columns[6:]]

    for courses in grade.columns:

        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
        # on va venir récupérer les notes de chaque maison pour toutes les matières (d'où la boucle)
        plt.hist(grade[df["Hogwarts House"] == "Gryffindor"]
                 [courses],  bins=50, label="Gryffindor", color='r', alpha=0.5)
        plt.hist(grade[df["Hogwarts House"] == "Slytherin"]
                 [courses],  bins=50, label="Slytherin", color='g', alpha=0.5)
        plt.hist(grade[df["Hogwarts House"] == "Hufflepuff"]
                 [courses],  bins=50, label="Hufflepuff", color='y', alpha=0.5)
        plt.hist(grade[df["Hogwarts House"] == "Ravenclaw"]
                 [courses],  bins=50, label="Ravenclaw", color="skyblue",  alpha=0.5)

        # le titre de notre graphique correspond au nom du cours
        plt.title(courses)

        # on détermine la position de notre légende pour identifier facilement nos maisons
        # https://fr.acervolima.com/matplotlib-pyplot-legend-en-python/#:~:text=legend()%20en%20Python,-Laisser%20un%20commentaire&text=Matplotlib%20est%20l'un%20des,de%20donn%C3%A9es%20dans%20des%20tableaux.
        plt.legend(loc='upper left')

        # on affiche notre graphique final
        plt.show()


if __name__ == "__main__":
    plot_hist()


#######

# Q:    Quel cours de Poudlard a une répartition des notes homogènes entre les quatres maisons ?
# A:    Care of Magical Creatures et/ou Arithmancy / un peu potion aussi
