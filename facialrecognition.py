import cv2

def capture_face_from_camera():
    """
    Captures the face from the camera and returns the frame.
    """
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()
    return frame

def load_known_faces_from_db():
    """
    Load and return known faces from the database.
    For demonstration purposes, I am just loading a single reference image.
    Modify this function to load multiple faces if needed.
    """
    # For now, we'll use a reference image to simulate loading from a database.
    # You may replace this section with your method of loading known faces.
    reference_image = cv2.imread('face.jpg')
    return [reference_image]  # Returning a list containing one known face image.

def detect_faces_cv(image):
    """
    Detect faces in an image using OpenCV's Haar cascades.
    Returns the coordinates of the detected faces.
    """
    # Load the pre-trained Haar cascade for face detection from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    return faces

def recognize_face(known_faces, unknown_face_image):
    """
    Compares unknown_face_image with a list of known_faces.
    Returns True if a match is found, otherwise returns False.
    """
    # Loop through the known faces and compare them with the unknown face image
    for known_face in known_faces:
        # Implement a method for comparison here (for instance, using OpenCV's methods)
        # You may compare histograms, structural similarity, or other methods for comparison.
        # This example uses simple comparison by resizing images and checking if they're equal.
        resized_unknown = cv2.resize(unknown_face_image, (known_face.shape[1], known_face.shape[0]))
        if cv2.meanSquaredError(known_face, resized_unknown) < threshold:
            return True

    return False

if __name__ == '__main__':
    known_faces = load_known_faces_from_db()
    captured_face = capture_face_from_camera()

    # Detect faces in the captured image using OpenCV
    faces_detected = detect_faces_cv(captured_face)

    if len(faces_detected) > 0:
        # Draw rectangles around detected faces for visualization
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(captured_face, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Show the image with rectangles around detected faces
        cv2.imshow('Detected Faces', captured_face)
        cv2.waitKey(0)  # Waits indefinitely for a key press to close the window
        cv2.destroyAllWindows()

        # Check if the detected face matches with known faces
        if recognize_face(known_faces, captured_face):
            print("Face recognized!")
        else:
            print("Face not recognized!")
    else:
        print("No faces detected in the captured image.")
