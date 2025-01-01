#!/usr/bin/env python

import numpy as np
from PIL import Image

flip = 1 # green
flop = 2 # blue

### without copy

d = np.array(Image.open("test_images/apples.png"))
t = d[:,:,flip]
d[:,:,flip] = d[:,:,flop]
d[:,:,flop] = t
im = Image.fromarray(d)
print("compare flipped colours without .copy():")
print(d[:10,:10,flip])
print(d[:10,:10,flop])
im.save("bad_apples_without_copy.png")

### with copy
d = np.array(Image.open("test_images/apples.png"))
t = d[:,:,flip].copy()
d[:,:,flip] = d[:,:,flop].copy()
d[:,:,flop] = t
im = Image.fromarray(d)
print("\n\n")
print("compare flipped colours with .copy():")
print(d[:10,:10,flip])
print(d[:10,:10,flop])
im.save("bad_apples_with_copy.png")

