# 컴퓨터공학부 정세빈 202103095
from scipy.misc import imread, imsave, imresize

img = imread('cat.jpg')
print(img.dtype, img.shape)

img_tined = imresize(img_tinted, (300, 300))

imsave('cat_tinted.jpg', img_tinted)
print(img_tinted.dtype, img_tinted.shape)
