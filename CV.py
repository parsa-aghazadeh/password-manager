import cv2
from datetime import datetime
import os
class Webcam:
    def capture(self):
        cam = cv2.VideoCapture(0)
        is_health, frame = cam.read()
        if not is_health:
            print("failed to grab frame")
        image = cv2.flip(frame, 1)
        self.frame = image
        cv2.waitKey(0)
        

    def saver(self,mobile):
        if not os.path.isdir('storage'):
            os.makedirs('storage')
        if not os.path.isdir(f'storage/{mobile}'):
            os.makedirs(f'storage/{mobile}')
        current_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.imwrite(f'storage/{mobile}/{current_dateTime}.jpg',self.frame)
    