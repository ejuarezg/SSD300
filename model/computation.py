"""
compute required indicies.

date: 10/1
author: arabian9ts
"""

import numpy as np

def jaccard(rect1, rect2):
    """
    Jaccard index.
    Jaccard index is defined as #(A∧B) / #(A∨B)
    """
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(rect1[0], rect2[0])
    yA = max(rect1[1], rect2[1])
    xB = min(rect1[2], rect2[2])
    yB = min(rect1[3], rect2[3])
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (rect1[2] - rect1[0] + 1) * (rect1[3] - rect1[1] + 1)
    boxBArea = (rect2[2] - rect2[0] + 1) * (rect2[3] - rect2[1] + 1)
    # return the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the intersection area
    return interArea / float(boxAArea + boxBArea - interArea)

def corner2center(rect):
    """
    rect is defined as [ top_left_x, top_left_y, width, height ]
    """
    center_x = (2 * rect[0] + rect[2]) * 0.5
    center_y = (2 * rect[1] + rect[3]) * 0.5

    return np.array([center_x, center_y, abs(rect[2]), abs(rect[3])])


def center2corner(rect):
    """
    rect is defined as [ top_left_x, top_left_y, width, height ]
    """
    corner_x = rect[0] - rect[2] * 0.5
    corner_y = rect[1] - rect[3] * 0.5

    return np.array([corner_x, corner_y, abs(rect[2]), abs(rect[3])])


def convert2diagonal_points(rect):
    """
    convert rect format

    Args:
        input format is...
        [ top_left_x, top_left_y, width, height ]
    Returns:
        output format is...
        [ top_left_x, top_left_y, bottom_right_x, bottom_right_y ]
    """
    return np.array([rect[0], rect[1], rect[0]+rect[2], rect[1]+rect[3]])


def convert2wh(rect):
    """
    convert rect format

    Args:
        input format is...
        [ top_left_x, top_left_y, bottom_right_x, bottom_right_y ]
    Returns:
        output format is...
        [ top_left_x, top_left_y, width, height ]
    """
    return np.array([rect[0], rect[1], rect[2]-rect[0], rect[3]-rect[1]])
