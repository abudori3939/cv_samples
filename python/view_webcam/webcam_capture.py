import cv2

def main():
    capture = cv2.VideoCapture(0)

    while(True):
      try:
        ret, frame = capture.read()
        if ret is False:
          raise IOError
        cv2.imshow('frame',frame)
        cv2.waitKey(1)
      except KeyboardInterrupt:
        # 終わるときは CTRL + C を押す
        break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
