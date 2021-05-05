import cv2
import glob
import numpy as np

dist_coeffs = np.array([-0.4023, 0.2236, -0.0051, -0.0090, -0.0646])
intrinsic_m = np.array([[440.2053, 0.000000, 350.0626], [0.000000, 440.9488, 264.6964], [0.000000, 0.000000, 1.000000]])
count = 0

#move through every element inside path
for img in glob.glob("/home/lapyrcio/Desktop/imagery/*.jpg"):
    n= cv2.imread("/home/lapyrcio/Desktop/imagery/Boson"+str(count)+".jpg")
    undistorted = cv2.undistort(n, intrinsic_m, dist_coeffs, None, intrinsic_m)
    cv2.imwrite("/home/lapyrcio/Desktop/newimagery/Boson_new"+str(count)+".jpg", undistorted)
    count = count + 1
