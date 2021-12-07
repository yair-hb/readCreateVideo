#en este codigo se crea una ventana en la que se muestra una fuente de video (webcam)
import cv2

captura = cv2.VideoCapture(0)
while (captura.isOpened()):
    ret, imagen =captura.read()
    if ret == True:
        cv2.imshow('captura', imagen)
        if cv2.waitKey(30) & 0xFF == ord('s'):
            break
    else: break
captura.release()
cv2.destroyAllWindows()
