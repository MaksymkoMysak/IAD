import pandas as pd
import datetime
import g

pd.set_option("display.max_columns", None)


def dateTime(dt):
    for i in range(dt.shape[0]):
        dt.loc[i, "day/month"] = datetime.datetime.strptime(dt["day/month"][i], "%d.%b %Y")
        dt.loc[i, "Time"] = datetime.datetime.strptime(time(dt["Time"][i]).strip(), "%H:%M")


def time(a):
    if a[-2:] == "AM" and a[:2] == "12":
        return "00" + a[2: - 2]
    elif a[-2:] == "AM":
        return a[: -2]
    elif a[-2:] == "PM" and a[:2] == "12":
        return a[:-2]
    else:
        if int(a.split(":")[0]) < 10:
            return str(int(a[:1]) + 12) + a[1:5]
        else:
            return str(int(a[:2]) + 12) + a[2:5]


def pressure(a):
    return float(a.replace(",", "."))


def percents(a):
    return float(int(a.strip("%")) / 100)


def mph(a):
    return int(a.strip(" mph"))


def parser(dataFrame):
    dataFrame["day/month"] = dataFrame["day/month"] + " " + "2020"
    dateTime(dataFrame)
    dataFrame.set_index("day/month", inplace=True, drop=True)
    dataFrame["Humidity"] = dataFrame["Humidity"].apply(percents)
    dataFrame["Wind Speed"] = dataFrame["Wind Speed"].apply(mph)
    dataFrame["Wind Gust"] = dataFrame["Wind Gust"].apply(mph)
    dataFrame["Pressure"] = dataFrame["Pressure"].apply(pressure)


dt = pd.read_csv("DATABASE.csv", sep=";")
parser(dt)
g.lines(dt, x="Temperature", y="Humidity")
g.scatter(dt, x="Temperature", y="Humidity")
g.piechart(dt, y="Temperature")
g.histohram(dt, y="Temperature")
g.stackplot(dt, y1="Temperature", y2="Humidity")
print(dt)
