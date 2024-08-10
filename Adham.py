import cv2 
import tkinter
image=cv2.imread('cat.jpg')
window = tkinter.Tk()
cv2.imshow('image',image)
def vFlipImage():
    cv2.destroyAllWindows()
    Vflip=cv2.flip(image,0)
    cv2.imshow('vflip',Vflip)
def hFlipImage():
    cv2.destroyAllWindows()
    hflip=cv2.flip(image,1)
    cv2.imshow('hflip',hflip)
def FlipImage():
    cv2.destroyAllWindows()
    flip=cv2.flip(image,-1)
    cv2.imshow('flip',flip)
def Original():
    cv2.destroyAllWindows()
    cv2.imshow('original',image)
def gray():
    cv2.destroyAllWindows()
    Gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray',Gray)
def HSV():
    cv2.destroyAllWindows()
    HSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV',HSV)
Vbutton=tkinter.Button(text='vflip',command = vFlipImage)
Hbutton=tkinter.Button(text='Hflip',command = hFlipImage)
original=tkinter.Button(text='original',command = Original)
button=tkinter.Button(text='flip',command = FlipImage)
Gbutton=tkinter.Button(text='Gray',command = gray)
HSVbutton=tkinter.Button(text='HSV',command = HSV)
Vbutton.grid(row=0,column=0)
Hbutton.grid(row=0,column=1)
button.grid(row=1,column=0)
original.grid(row=1,column=1)
Gbutton.grid(row=2,column=0)
HSVbutton.grid(row=2,column=1)
window.mainloop()