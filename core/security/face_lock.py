import cv2
import face_recognition
import os
import time

# ================= LOAD KNOWN FACE =================

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
image_path = os.path.join(BASE_DIR, "data", "my_face.jpg")

known_image = face_recognition.load_image_file(image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]


def monitor_face():
    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not video.isOpened():
        print("❌ Camera not accessible")
        return

    print("Security system active...")

    while True:
        ret, frame = video.read()

        if not ret:
            print("Camera error")
            break

        # 🔥 Resize frame (performance boost)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # 🔥 Convert properly (fixes dlib error)
        rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # 🔍 Detect faces (safe method)
        face_encodings = face_recognition.face_encodings(rgb_small)

        status_text = "Checking..."

        # ================= NO FACE =================
        if len(face_encodings) == 0:
            status_text = "No face detected"

        else:
            unknown_detected = False

            for face_encoding in face_encodings:
                distance = face_recognition.face_distance([known_encoding], face_encoding)

                print("Distance:", distance[0])  # Debug

                if distance[0] > 0.6:
                    unknown_detected = True

            # ================= UNKNOWN FACE =================
            if unknown_detected:
                status_text = "Unknown face detected"

                cv2.putText(frame, status_text, (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2)

                cv2.imshow("Security Camera", frame)
                cv2.waitKey(2000)

                print("🚨 Locking system...")
                os.system("rundll32.exe user32.dll,LockWorkStation")
                break

            # ================= AUTHORIZED =================
            else:
                status_text = "Authorized user"

        # ================= DISPLAY TEXT =================
        color = (0, 255, 0) if status_text == "Authorized user" else (0, 0, 255)

        cv2.putText(frame, status_text,
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    color,
                    2)

        cv2.imshow("Security Camera", frame)

        # 🔥 Prevent freeze
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        time.sleep(0.05)

    video.release()
    cv2.destroyAllWindows()