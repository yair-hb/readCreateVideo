#este es el codigo para ver un video mediante opencv
import cv2

captura = cv2.VideoCapture('video.mp4')
while (captura.isOpened()):
    ret, imagen =captura.read()
    if ret == True:
        cv2.imshow('captura', imagen)
        if cv2.waitKey(30) == ord('s'):
            break
    else: break
captura.release()
cv2.destroyAllWindows()
