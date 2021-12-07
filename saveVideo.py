#en este codigo se graba un video desde la fuente de imagen (webcam)
import cv2

captura = cv2.VideoCapture(0)
fps = captura.get(cv2.CAP_PROP_FPS)
size = (int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)), int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)))
salida = cv2.VideoWriter('videoSalida.avi', cv2.VideoWriter_fourcc(*'XVID'), fps,size)
while (captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        cv2.imshow('video', imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break
captura.release()
salida.release()
cv2.destroyAllWindows()
