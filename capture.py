import cv2

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press SPACE to capture image... (Press ESC to exit)")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Show camera frame
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    # Press SPACE to capture image
    if key % 256 == 32:
        img_name = "captured_image.png"
        cv2.imwrite(img_name, frame)
        print(f"Image saved as {img_name}")

    # Press ESC to exit
    elif key % 256 == 27:
        print("Closing camera...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()