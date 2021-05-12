import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('recording.avi',fourcc,20.0,(640,480))
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while cap.isOpened():
    success,img=cap.read()
    out.write(img)
    cv2.imshow('video',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
