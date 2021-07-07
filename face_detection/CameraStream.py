import cv2
import imutils
from FaceDetector import FaceDetector


class CameraStream():
    # finished = pyqtSignal()
    # image = pyqtSignal(QImage)
    # pic = pyqtSignal(object)
    # play = pyqtSignal(int)
    # coordinates = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.videoStream = None
        self.stopped = False
        self.face_detector = FaceDetector(0.5)

    def long_running(self):
        print("Starting")
        self.stopped = False
        self.videoStream = cv2.VideoCapture(0)

        while not self.stopped:
            ret, frame = self.videoStream.read()
            if ret:
                frame = imutils.resize(frame, width=400)
                frame = self.face_detector.detect(frame)
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF
                # if the `q` key was pressed, break from the loop
                if key == ord("q"):
                    self.stopped = True

                # self.pic.emit(frame)

                # rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # h, w, ch = rgb_image.shape
                # bytesPerLine = ch * w
                # convertToQtFormat = QtGui.QImage(
                #     rgb_image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                # p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                # self.image.emit(p)
        self.stop()

    def stop(self):
        cv2.destroyAllWindows()
        self.videoStream.release()  # type:ignore
        self.stopped = True
        # self.videoStream.release()
