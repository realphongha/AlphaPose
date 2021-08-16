import cv2
import numpy as np
from urllib.request import urlopen


def read_img(img_path, bgr=False):
    if "http://" in img_path or "https://" in img_path:
        req = urlopen(img_path)
        img = np.asarray(bytearray(req.read()), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    else:
        img = cv2.imread(img_path)
    if not bgr:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
