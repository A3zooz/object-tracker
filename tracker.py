import cv2


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.waitKey(5000)
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    bounding_box = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Frame")
    tracker = cv2.TrackerKCF.create()
    tracker.init(frame, bounding_box)
    while True:
        ret, frame = cap.read()
        success, bounding_box = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(x) for x in bounding_box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        else:
            cv2.putText(frame, "Tracking failure detected", (100, 100), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        cv2.imshow("Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
