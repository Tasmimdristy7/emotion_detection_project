from fer import FER
import cv2

# Load the pre-trained emotion detection model
emotion_detector = FER()

# Capture video from the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()
    if not ret:
        break

    # Detect emotions in the frame
    emotions = emotion_detector.detect_emotions(frame)
    
    # Display the results on the frame
    for emotion in emotions:
        # Get the most dominant emotion
        dominant_emotion = max(emotion['emotions'], key=emotion['emotions'].get)
        
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (emotion['box'][0], emotion['box'][1]),
                      (emotion['box'][0] + emotion['box'][2], emotion['box'][1] + emotion['box'][3]),
                      (0, 255, 0), 2)

        # Display the dominant emotion above the rectangle
        cv2.putText(frame, dominant_emotion, (emotion['box'][0], emotion['box'][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Show the frame with the detected emotions
    cv2.imshow('Emotion Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
video_capture.release()
cv2.destroyAllWindows()
