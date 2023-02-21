from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt


def open_image():
    global img
    filename = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg;.jpeg;.png;.bmp")])
    img = cv2.imread(filename)
    img2= cv2.resize(img,(300,200))
    cv2.imshow("Original Image", img2)
def ocr_image():
    text = pytesseract.image_to_string(img, lang='eng')
    new_window = Toplevel(root)
    new_window.title("OCR Output")
    result_label = Label(new_window, text=text)
    result_label.pack(pady=10)
    # print("OCR output: ", text)
def open_camera():
    global img
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            img = frame
            break
    cap.release()
    img2= cv2.resize(img,(300,200))
    cv2.destroyAllWindows()
    cv2.imshow("Image", img2)

def brighten_image():
    global img
    alpha = 3
    beta = 25
    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    img2= cv2.resize(img,(300,200))
    cv2.imshow("Brightened Image", img2)

    
def invert():
    global img
    img2 = cv2.resize(img, (300, 200))
    inverted = 255 - img2
    cv2.imshow("Inverted Image", inverted)
    
   
    


root = Tk()
root.title("OCR (Optical Character Recognition) APP")

open_button = Button(root, text="Open Image", command=open_image, width=30, height=1)
invert = Button(root, text="invert", command=invert, width=20, height=1)
ocr_image_button = Button(root, text="OCR Image", command=ocr_image,width=20, height=1)
open_camera_button = Button(root, text="Open Camera", command=open_camera, width=30, height=1)
brighten_image_button = Button(root, text="Brighten Image", command=brighten_image,width=20, height=1)
label1 = Label(root, text="Khoir Afandi _ 2215102009")
label2 = Label(root, text="Yeni Puspitasari _ 2215102004 ")
label3 = Label(root, text="Wulansari _ 2215102010")
label4 = Label(root, text="Wulan Kyrniawati _ 2215102001")
label5 = Label(root)


label1.pack(pady=0)
label2.pack(pady=0)
label3.pack(pady=0)
label4.pack(pady=0)
label5.pack(pady=35)

open_camera_button.pack(pady=10 )
open_button.pack(pady=10 )
ocr_image_button.pack(pady=5 )
brighten_image_button.pack(pady=5 )
invert.pack(pady=5 )





root.geometry("600x400")
root.mainloop()