import numpy as np
import matplotlib.pyplot as plt

files = ["Barcelona.jpg", "Paris.jpg", "frac.jpeg", "triangulos.png"]

data = [255 - (plt.imread(file).sum(axis=-1)/3).astype(int) for file in files]

fig, axes = plt.subplots(2, 2)
axes = axes.reshape(4)

for i in range(4):
    axes[i].imshow(data[i], cmap = "Greys")
    axes[i].set_axis_off()
plt.savefig("imagenes.pdf", dpi = 300)
plt.close()

trans = [np.fft.rfft2(image) for image in data]
fig, axes = plt.subplots(2, 2)
axes = axes.reshape(4)

for i in range(4):
    temp = np.log(abs(trans[i]))
    axes[i].imshow(temp, cmap = "Greys")
    axes[i].set_title(files[i])
    axes[i].set_axis_off()
plt.tight_layout()
plt.savefig("transformadas.pdf")
plt.close()

fig, axes = plt.subplots(2, 2)
axes = axes.reshape(4)
for i in range(4):
    center = int(trans[i].shape[0]*0.5)
    axes[i].plot(abs(trans[i][center]))
plt.tight_layout()
plt.savefig("cortes_transversales.pdf")
plt.close()

bw = np.zeros_like(data[0])
bw[(255 - data[0]) > 127] = 1

bw_fft = np.fft.fft2(bw)
bw_fft[:, :5] = bw_fft.mean()
bw_filtered = abs(np.fft.ifft2(bw_fft))

bw2 = np.zeros_like(bw)
bw2[bw_filtered > 0.5*bw_filtered.max()] = 1

plt.imshow(bw2, cmap = "Greys")
plt.savefig("sin_horizontales.pdf")
