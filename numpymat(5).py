from matplotlib import pyplot as plt
x = ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16']
yo = [774.25, 776.030029, 779.309998, 779, 779.659973]
yh=[776.065002,778.710022,782.070007,780.47998,779.659973]
yl=[772.559998,776.429993,776.469971,776.859985,775.080017]
plt.plot(x, yo, color="red", linewidth=0.6, label="Open Price")
plt.title("Alphabet Inc. Open Prices (Oct 3, 2016 - Oct 7, 2016)")
plt.plot(x, yh, color="blue", linewidth=0.6, label="High Price")
plt.plot(x, yl, color="black", linewidth=0.6, label="Low Price")
plt.legend()
plt.show()
