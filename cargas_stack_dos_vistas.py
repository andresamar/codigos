import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import convolve2d as conv2
from skimage import  color, data,io, restoration
import nibabel
import shutil
from mpl_toolkits import mplot3d

image_T = image.T
image_vertical= image
image_horizontal = image_T


def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)

def view_horizontal(volume):
    remove_keymap_conflicts({'n', 'm'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index], aspect = '0.5',cmap='gray')
    plt.xlabel("$axis z$")
    plt.ylabel("$axis x$")
    fig.canvas.mpl_connect('key_press_event', process_key)

def view_vertical(volume):
    remove_keymap_conflicts({'n', 'm'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index], aspect = '0.9', cmap='gray')
    plt.xlabel("$axis x$")
    plt.ylabel("$axis y$")
    fig.canvas.mpl_connect('key_press_event', process_key)

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'n':
        previous_slice(ax)
    elif event.key == 'm':
        next_slice(ax)
    fig.canvas.draw()

def previous_slice(ax):
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])

def next_slice(ax):
    volume = ax.volume
    ax.index = (ax.index + 1) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])


view_vertical(image_vertical)
view_horizontal(image_horizontal)
plt.show()
