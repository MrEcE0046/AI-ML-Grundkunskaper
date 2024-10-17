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
    
    label_data=np.array(label_data,dtype=float)
    x1 = label_data[:, 0]
    y1 = label_data[:, 1]
    label = label_data[:, 2]

    plt.plot(x,y,"r", label=f"y= {k}x {m}")
    plt.scatter(x1[label==0],y1[label==0], c="blue", label="Label 0")
    plt.scatter(x1[label==1],y1[label==1], c="red", label="Label 1")
    plt.title(f"{np.sum(label==0)} of label-0 | {np.sum(label==1)} of label-1")
    plt.xlabel("X-axle")
    plt.ylabel("Y-axle")
    plt.legend()
    plt.grid()
    plt.show()


k = -1.5
m = 0

data = readfile()
label_data = catagories(data, k, m)
write_file(label_data)
x, y = line(k, m)
plott(label_data, x, y)