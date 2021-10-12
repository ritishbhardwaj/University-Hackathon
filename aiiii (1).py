import cv2
import numpy as np

class ai:
    cap = cv2.VideoCapture(0)
    def __init__(self,assign):
        self.assign=assign      
    
    def calling(self):
        while True:
            _, frame = ai.cap.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

            if self.assign=='red':    
                low_red = np.array([161,155,84])
                high_red = np.array([179, 255, 255])  ##in this array we are defining hsv values
                red_mask = cv2.inRange(hsv_frame, low_red, high_red)
                red = cv2.bitwise_and(frame, frame, mask=red_mask)
                cv2.imshow("Frame", frame)
                cv2.imshow("Red", red)
        

            elif self.assign=='blue':    
                low_blue = np.array([94, 80, 2])
                high_blue = np.array([126, 255, 255])
                blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
                blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
                cv2.imshow("Frame", frame)
                cv2.imshow("Blue", blue)

            
            elif self.assign=='green':
                low_green = np.array([25, 52, 72])
                high_green = np.array([102, 255, 255])
                green_mask = cv2.inRange(hsv_frame, low_green, high_green)
                green = cv2.bitwise_and(frame, frame, mask=green_mask)
                cv2.imshow("Frame", frame)
                cv2.imshow("Green", green)

            elif self.assign=='yellow':
                low_yellow= np.array([20,100,100])
                high_yellow= np.array([30,255,255])
                yellow_mask= cv2.inRange(hsv_frame, low_yellow, high_yellow)
                yellow= cv2.bitwise_and(frame,frame,mask=yellow_mask)
                cv2.imshow("Frame", frame)
                cv2.imshow("yellow",yellow)


            elif self.assign=='orange':
                low_orange= np.array([10,100,100])
                high_orange= np.array([20, 255, 255])
                orange_mask= cv2.inRange(hsv_frame, low_orange, high_orange)
                orange= cv2.bitwise_and(frame,frame,mask=orange_mask)
                cv2.imshow("Frame", frame)
                cv2.imshow('orange',orange)

            elif self.assign=='pink':
                low_pink= np.array([145,100,100])
                high_pink= np.array([165, 255, 255])
                pink_mask= cv2.inRange(hsv_frame, low_pink, high_pink)
                pink= cv2.bitwise_and(frame,frame,mask=pink_mask)
                cv2.imshow("Frame", frame)
                cv2.imshow('pink',pink)

            elif self.assign=='brown':
                low_brown= np.array([20,100,100])
                high_brown= np.array([30, 255, 255])
                brown_mask= cv2.inRange(hsv_frame, low_brown, high_brown)
                brown= cv2.bitwise_and(frame,frame,mask=brown_mask)
                cv2.imshow("Frame", frame)
                cv2.imshow('brown',brown)
    
            if cv2.waitKey(33) == 27:
                # for i in range(6):
                #     val=input('yes/no: ')
                #     fn()
                break

                exit(0)
#__main__
print('what colour would you like to test')
print('1. Red /n Blue /n Green /n Yellow /n Orange /n pink /n brown ')
def fn():
    value=(input())
    ref=ai(value)
    # for i in range(6):
    ref.calling()
    # permission=input('yes/no: ')
    # if permission.lower()=='no':
    #     break
fn()   
