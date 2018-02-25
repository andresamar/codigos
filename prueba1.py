
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import convolve2d as conv2
from skimage import  color, data,io, restoration
import nibabel
import shutil
from mpl_toolkits import mplot3d
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib import cm, colors

PATH = "/home/a/Tesis/tiff/651-45/centro_bola/"
image = io.imread(PATH + "centro_XY.tif" )

image_T = image.T
image_vertical = image
image_vertical_rot = np.rot90(image_vertical,axes=(0, 1))
image_horizontal = image_T








#plt.imshow(image_c[29])




'''
fig = plt.figure(figsize=(10,10))
grid = plt.GridSpec(3, 3, hspace=0.4, wspace=0.2)
scalebar = ScaleBar(0.16,'um') #1pixel = 0.16 um


gax1 = plt.subplot(grid[0, :-1])
gax1.set_title('Plano XY')
gax1.set_xlabel('Pixel x ')
gax1.set_ylabel('Pixel y ')
gax1.add_artist(scalebar )

gax2 = plt.subplot(grid[1, :-1])
gax2.set_title('Plano XZ')
gax2.set_xlabel('Pixel y ')
gax2.set_ylabel('Pixel z ')

gax3 = plt.subplot(grid[0:1, -1])
gax3.set_title('Plano YZ')
gax3.set_xlabel('Pixel x ')
gax3.set_ylabel('Pixel z ')


gax1.imshow(image_vertical[45],cmap ="inferno")
gax2.imshow(image_horizontal[45],cmap ="inferno")
gax3.imshow(image_vertical_rot[45],cmap ="inferno")
'''


'''
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')

plt.suptitle('Main title')

n_photo = 10
cax3 = ax3.imshow(image_horizontal[n_photo], cmap ='gray')
fig.colorbar(cax3 ,ax =ax3)
ax3.set_title('Vista horizontal')
plt.tight_layout()

cax4 = ax4.imshow(image_horizontal_rot[n_photo], cmap ='gray')
fig.colorbar(cax4 ,ax =ax4)
ax4.set_title('Vista horizontal rotada 90')
plt.tight_layout()

cax2 = ax2.imshow(image_vertical_rot[n_photo], cmap ='gray')
fig.colorbar(cax2 ,ax =ax2)
ax2.set_title('Vista vertical rotada 90')
plt.tight_layout()

cax1 = ax1.imshow(image_vertical[n_photo],cmap='gray')
fig.colorbar(cax1 ,ax =ax1)
ax1.set_title('Vista vertical')
plt.tight_layout()
'''



def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)
def view_vertical(volume):
    remove_keymap_conflicts({'n', 'm'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index], cmap='gray')
    scalebar = ScaleBar(0.16,'um') #1pixel = 0.16 um
    ax.add_artist(scalebar )
    plt.xlabel("$axis x$")
    plt.ylabel("$axis y$")
    fig.canvas.mpl_connect('key_press_event', process_key)
def view_vertical_rot(volume):
    remove_keymap_conflicts({'n', 'm'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index], aspect = '0.9', cmap='gray')
    scalebar = ScaleBar(0.16,'um') #1pixel = 0.16 um
    ax.add_artist(scalebar )
    plt.xlabel("$axis x$")
    plt.ylabel("$axis y$")
    fig.canvas.mpl_connect('key_press_event', process_key)
def view_horizontal(volume):
    remove_keymap_conflicts({'n', 'm'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index], aspect = '0.5',cmap='gray')
    scalebar = ScaleBar(0.16,'um') #1pixel = 0.16 um
    ax.add_artist(scalebar )
    plt.xlabel("$axis z$")
    plt.ylabel("$axis x$")
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
#view_horizontal(image_horizontal)
plt.show()
#plt.savefig("resultado2.pdf")
