import cv2
import glob
import sys


def to_gray():
    images = glob.glob("./images/input/*")
    for x, img in enumerate(images):
        img = cv2.imread(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./images/output/{0:d}.jpg".format(x), gray)
    print("done!!!!")


if __name__ == "__main__":
    exe_action = sys.argv[2]
    if exe_action == "to_gray":
        to_gray()
