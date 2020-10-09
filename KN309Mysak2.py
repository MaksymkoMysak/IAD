import matplotlib.pyplot as plt
import datetime


def lines(dt, x, y):
    dt.plot(x=x, y=y)
    plt.show()


def scatter(dt, x, y):
    dt.plot(kind="scatter", x=x, y=y)
    plt.show()


def piechart(dt, y):
    dt.groupby(y)[y].count().plot.pie(autopct='%.2f', figsize=(10, 10))
    plt.show()


def histohram(dt, y):
    dt.hist(column=y)
    plt.show()


def stackplot(dt, y1, y2):
    plt.stackplot(dt.index, dt[y1], dt[y2], labels=[y1, y2])
    plt.show()
