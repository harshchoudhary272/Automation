import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return


def iscollide(data):
    for i in range(300,415):
            for j in range(410,563):
                if data[i, j] < 100:
                    hit("down")
                    return 


    for i in range(300,415):
        for j in range(563,650):
            if data[i, j] < 100:
                hit("up")
                return 
    return 


if __name__=="__main__":
    print("dino game is about to start in 2 seconds")
    time.sleep(2)
    #hit('up')

    while True:
         image = ImageGrab.grab().convert('L')
         data = image.load()
         iscollide(data)
             

        # print(asarray(image))
        #draw rectangle for cactus
         for i in range(265,315):
            for j in range(563,650):
                data[i, j] = 0
                    
                

        # draw the rectangle for bird
         for i in range(250,300):
            for j in range(410,563):
                 data[i, j] = 171   

         image.show()
         break
