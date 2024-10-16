import numpy as np, matplotlib.pyplot as plt, csv


def readfile():
    """ Open file and append to list """

    data = []
    with open("unlabelled_data.csv") as f:
        rows = f.readlines()
        for row in rows:
            data.append([float(i) for i in row.split(",")])
    return data


def catagories(data, k, m):
    """ Catagories data according to y=kx+m """

    data_label = []
    for x, y in data:
        val = k*x+m
        if y > val:
            data_label.append((x, y, 0))
        elif y < val:
            data_label.append((x, y, 1))
    return data_label


def write_file(label_data):
    """" Write new file with labels """

    with open("labelled_data.csv", "w", newline="") as ld:
        writer = csv.writer(ld)
        writer.writerows(label_data)


def line(k, m):
    """ Define a line """

    x = np.linspace(-5, 5, 10) 
    y = k * x + m
    return x, y


def plott(label_data, x, y):
    """ Plot a line and scatterplot """

    zeroes = [i for i in label_data if i[2] ==  0] # Separerar 1/0 från stora listan, bara för att plotta
    ones = [i for i in label_data if i[2] ==  1]

    plt.plot(x,y,"r")
    plt.scatter(np.array(ones)[:, 0], np.array(ones)[:, 1], c="blue")
    plt.scatter(np.array(zeroes)[:, 0], np.array(zeroes)[:, 1], c= "green")
    plt.title(f"{len(zeroes)} of label-0 | {len(ones)} of label-1")
    plt.xlabel("X-axle")
    plt.ylabel("Y-axle")
    plt.legend((f"y= {k}x {m}", "Label 1", "Label 0"))
    plt.grid()
    plt.show()


k = -1.5
m = 0

data = readfile()
label_data = catagories(data, k, m)
write_file(label_data)
x, y = line(k, m)
plott(label_data, x, y)