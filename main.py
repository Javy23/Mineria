import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def function():
    file_name = 'Historico del Bitcoin.csv'
    data = pd.read_csv(file_name, header=0)
    date = data['Fecha']
    price = data['Cierre']
    price2 = []

    for x in price:
        x = x.replace(",", "")
        price2.append(x)

    price2 = [float(x) for x in price2]

    date = list((reversed(date)))
    price2 = np.array(list(reversed(price2)))

    month = []
    for i in range(1,25):
        month.append(i)

    coef = np.polyfit(month, price2, 4)
    p = np.polyval(coef, 25)
    p = float(p)
    p = round(p,2)
    price2 = list(price2)

    plt.figure(figsize=[20, 10])
    plt.title('Precio de Bitcoin por mes los ultimos dos anios')
    plt.scatter(date, price2)
    plt.scatter("Ene 2023", p, c='red')
    plt.ylabel('Dolares')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    function()
