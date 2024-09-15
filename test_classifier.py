import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.putText(frame, f'Ready? Press "Q" ! :)', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                    cv2.LINE_AA)
    cv2.putText(frame, f'[Normal]', (100, 130), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                    cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()