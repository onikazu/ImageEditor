import cv2
import glob

if __name__ == "__main__":
    images = glob.glob("./images/origin_to_gray/*")
    for x, img in enumerate(images):
        img = cv2.imread(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./images/converted_to_gray/{0:d}.jpg".format(x), gray)
    print("done!!!!")
