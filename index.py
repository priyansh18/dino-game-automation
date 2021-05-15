import pyautogui as pag
from PIL import Image,ImageGrab
import time
from numpy import asarray

def hit(key):
    pag.press(key)

def isCollideUp(data):
    for i in range(300,330):
        for j in range(430,500):
            if data[i,j] < 100:
                return True
    return False

def isCollideDown(data):
    for i in range(300,330):
        for j in range(300,430):
            if data[i,j] < 100:
                return True
    return False
                
def takeScreensot():
    # Grabbing the image and convert it into Greyscale
    image = ImageGrab.grab().convert('L')
    return image


if __name__ == "__main__":
    print("Hey Dino game is about to start in 3 Seconds")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        # print(asarray(image))
        data = image.load()
        if isCollideUp(data):
            hit('up')
        if isCollideDown(data):
            hit('down')
        
        
    
