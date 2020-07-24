import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector

# constant
x_list = []
y_list = []
j = 0
image_folder = "images"


def line_select_callback(clk, rls):
    global xmin, xmax, ymin, ymax, xy_list
    xmax = int(clk.xdata)
    xmin = int(rls.xdata)
    ymax = int(clk.ydata)
    ymin = int(rls.ydata)
    x_list.append((xmin, xmax))
    y_list.append((ymin, ymax))
    xy_list = list(zip(x_list, y_list))


def onkeypress(event):
    global x_list, y_list, xy_list, j
    if (event.key == 'y' or event.key == 'Y'):
        print(xy_list)
        write_image()
        plt.close()
        xy_list = []
        x_list = []
        y_list = []
        j += 1


def write_image():
    for i in range(len(xy_list)):
        cropped_image = image[xy_list[int(i)][1][1]:xy_list[int(i)][1][0], xy_list[int(i)][0][1]:xy_list[int(i)][0][0]]
        # cop = cv2.imshow('im', cropped_image)
        cv2.imwrite('WELD DEFECT {}.jpg'.format([j, i]), cropped_image)
        print("image WELD DEFECT{}.jpg is saved!".format([j, i]))
        print([j, i])


def toggel_selector(event):
    toggel_selector.ES.set_active(True)


for n, image_file in enumerate(os.scandir(image_folder)):
    fig, ax = plt.subplots()

    mngr = plt.get_current_fig_manager()

    mngr.resize(1000, 600)

    image = cv2.imread(image_file.path)
    ax.imshow(image)
    toggel_selector.ES = RectangleSelector(ax, line_select_callback, drawtype='box', useblit=True, button=[1], minspanx=5,
                                         minspany=5, spancoords='pixels', interactive=True)
    bbox = plt.connect('key_press_event', toggel_selector)
    key = plt.connect('key_press_event', onkeypress)
    plt.show()

