import cv2 as cv
import cv2.aruco as aruco
import numpy as np

aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
print("arucodict ", aruco_dict)

# img = aruco.drawMarker(aruco_dict, 23, 200, 1)
# img2 = aruco.drawMarker(aruco_dict, 35, 200, 1)
# img3 = aruco.drawMarker(aruco_dict, 40, 200, 1)
# img4 = aruco.drawMarker(aruco_dict, 17, 200, 1)
# img5 = aruco.drawMarker(aruco_dict, 51, 200, 1)
# img6 = aruco.drawMarker(aruco_dict, 64, 200, 1)
# img7 = aruco.drawMarker(aruco_dict, 47, 200, 1)
# img8 = aruco.drawMarker(aruco_dict, 59, 200, 1)

# cv.imwrite('new.jpg', img)
# cv.imwrite('new2.jpg', img2)
# cv.imwrite('new3.jpg', img3)
# cv.imwrite('new4.jpg', img4)
# cv.imwrite('new5.jpg', img5)
# cv.imwrite('new6.jpg', img6)
# cv.imwrite('new7.jpg', img7)
# cv.imwrite('new8.jpg', img8)

parameters =  aruco.DetectorParameters_create()
print("parameters ", parameters)

frame = cv.imread('aruco.jpg', cv.IMREAD_COLOR)

gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

res = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
print("res ", res[1])
# print("corners ", corners)
# print("ids ", ids)
# print("rejectedImgPoints ", rejectedImgPoints)

# gray = aruco.drawDetectedMarkers(gray, corners, ids) #Draw A square around the markers

# cv.imwrite('frame2.jpg',gray)