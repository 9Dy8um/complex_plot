import colorsys

import numpy as np
from matplotlib import pyplot as plt


def make_colors(w) -> np.ndarray[float]:
    w_shape = w.shape
    Mo_w = np.absolute(w)
    An_w = np.angle(w)
    # 模归一化到[0.5,1]，辐角归一化到[0,1]
    Mo_w_nom_hls = plt.Normalize(vmin=0, vmax=np.max(Mo_w))(Mo_w.reshape(-1, 1)) * 0.5 + 0.5
    An_w_nom = plt.Normalize(-np.pi, np.pi)(An_w.reshape(-1, 1))
    # 辐角映射到色相,模映射到亮度，饱和度填充1
    H_hls = np.array(An_w_nom)
    L_hls = np.array(Mo_w_nom_hls)
    S_hls = np.full_like(H_hls, 0.5)
    re_hls = np.hstack((H_hls, L_hls, S_hls))
    # hls转rgb
    li = []
    for i in re_hls:
        re_rgb_from_hls = colorsys.hls_to_rgb(*i)
        li.append(re_rgb_from_hls)
    # 转成3通道RGB图像矩阵
    li_nd = np.array(li).reshape((*w_shape, 3))
    return li_nd


def domain(z, w,title):
    color_array = make_colors(w)
    l = np.real(z[0][0])
    b = np.imag(z[0][0])
    r = np.real(z[-1][-1])
    t = np.imag(z[-1][-1])
    fig, ax = plt.subplots()
    ax.imshow(color_array, interpolation_stage='rgba', origin='lower', extent=(l, r, b, t))
    ax.set_title(title)
    ax.set_aspect('1')
    plt.savefig(f'.\\img\\{title}.png', dpi=300)
    plt.show()


def create_complex_ndarray(xlim, ylim, pointsum):
    x = np.linspace(*xlim, pointsum).reshape(1, -1)
    y = np.linspace(*ylim, pointsum).reshape(-1, 1)
    z = x + y * 1j
    return z
