# from ultralytics import YOLO
# import cv2

# # Load trained model
# model = YOLO("runs/detect/train2/weights/best.pt")
# # Test image
# image_path = r"C:\Users\subra\Downloads\adr.jpeg"
# #PAN_CARD.jpg
# results = model(image_path)

# # Show results 
# for result in results:
#     frame = result.plot()

#     cv2.imshow("Detection", frame)
#     cv2.waitKey(0)

# cv2.destroyAllWindows()




from ultralytics import YOLO
import cv2

# model = YOLO("runs/detect/pancard_model/weights/best.pt")

model = YOLO("runs/detect/train2/weights/best.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("PAN Card Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()