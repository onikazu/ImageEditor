import os

if __name__ == "__main__":
    if not os.path.isdir("./images"):
        os.mkdir("./images")
        os.mkdir("./images/origin_to_gray")
        os.mkdir("./images/converted_to_gray")

    print("made directory for this program!!!")