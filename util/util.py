"""
utility function group
such as load_images

date: 9/17
author: arabian9ts
"""

import numpy as np
import PIL
from imageio import imread

def preprocess(path):
    """
    load specified image

    Args: image path
    Return: resized image, its size and channel
    """
    img = imread(path)
    h, w, c = img.shape
    img = np.array(PIL.Image.fromarray(img).resize((300, 300)))
    img = img[:, :, ::-1].astype('float32')
    img /= 255.
    return img, w, h, c


def deprocess(x, w, h):
    """
    restore processed image

    Args: processed image
    Return: restored image
    """
    # x = x[:, :, ::-1]
    x *= 255.
    x = np.clip(x, 0, 255).astype('uint8')
    x = imresize(x, (h, w))
    return x