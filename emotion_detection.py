import cv2

# Open webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
