import random
import math
import matplotlib.pyplot as plt

def grafiek(x, y):
    """Grafiekje maken

    :param lijst: - list met integers
    :return:
    """
    plt.plot(x, y, 'r+')
    plt.title("Voorbeeld grafiek")
    plt.xlabel("Aantal studenten")
    plt.ylabel("Cijfers behaald")
    plt.show()


def piechart(y):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def stacked_bar():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, men_means, width, yerr=men_std, label='Men')
    ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
           label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()

    plt.show()


def main():
    print("Hello world!")
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [3, 5, 6, 2, 4, 6, 8, 9, 0, 8]
    #grafiek(x, y)
    # piechart(y)
    stacked_bar()
main()