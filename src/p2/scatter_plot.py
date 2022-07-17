import csv
import argparse
import numpy as np
import matplotlib.pyplot as plt


def read_csv(filename):
    dataset = list()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        try:
            for _ in reader:
                row = list()
                for value in _:
                    try:
                        value = float(value)
                    except:
                        if not value:
                            value = np.nan
                    row.append(value)
                dataset.append(row)
        except csv.Error as e:
            print(f'file {filename}, line {reader.line_num}: {e}')
    return np.array(dataset, dtype=object)


def scatter_plot():

    # ici on prépare notre dataset en le récupérant depuis notre argument
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=str, help="input dataset")
    options = parser.parse_args()
    dataset = read_csv(options.dataset)
    data = dataset[1:, :]
    data = data[data[:, 1].argsort()]

    # on sélectionne la colonne du csv utilisée pour le titre, les données etc
    x_values = 7
    y_values = 9

    # on va chercher le titre de notre x (ici ce sera Arithmancy car il est en [0, 7] comme à la bataille navale)
    x_label = dataset[0, x_values]
    y_label = dataset[0, y_values]  # même principe

    # même principe sauf qu'ici on vient récupérer les valeurs des colonnes
    X = np.array(data[:, x_values], dtype=float)
    y = np.array(data[:, y_values], dtype=float)
    legend = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    # ensuite on utilise plt.scatter afin d'afficher nos données pour les 4 maisons
    # X[:values] => nous permet de visualiser les données même si elles sont superposées car on joue sur l'opacité des couleurs
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
    plt.scatter(X[:250], y[:250], color='red', alpha=0.5)
    plt.scatter(X[250:750], y[250:750], color='yellow', alpha=0.5)
    plt.scatter(X[750:1500], y[750:1500], color='skyblue', alpha=0.5)
    plt.scatter(X[1500:], y[1500:], color='green', alpha=0.5)

    # on détermine la position de notre légende pour identifier facilement nos maisons
    # https://fr.acervolima.com/matplotlib-pyplot-legend-en-python/#:~:text=legend()%20en%20Python,-Laisser%20un%20commentaire&text=Matplotlib%20est%20l'un%20des,de%20donn%C3%A9es%20dans%20des%20tableaux.
    plt.legend(legend, loc='lower left')

    # on récupère le titre de notre axe en fonction du csv
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # on affiche notre graphique final
    plt.show()


if __name__ == "__main__":
    scatter_plot()


#######

# Q:    Quelles sont les deux features qui sont semblables ?
# A:    Les deux features semblables sont "Defense Against the Dark Arts" & "Astronomy"
