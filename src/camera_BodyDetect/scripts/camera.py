import numpy as np
import cv2 as cv
from PIL import Image

class BodyBoxing:
    def __init__(self):
        self.cap = cv.VideoCapture(0)
        fps = self.cap.get(cv.CAP_PROP_FPS)
        self.imageNum = 0
        self.sum=0
        self.timef=45   #抽帧：每45帧抽一帧出来处理
    def body_boxing(self):       
        while(True):
            self.sum+=1
            # 一帧一帧捕捉
            (self.frameState, self.frame) = self.cap.read()
            if self.frameState == True and (self.sum % self.timef==0):
                # 我们对帧的操作在这里
                gray = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
                cv.rectangle(gray,(384,0),(510,128),(0,255,0),3)    #左上角 右下角的坐标
                # 显示返回的每帧
                cv.imshow('frame',gray)
                frame = Image.fromarray(np.uint8(gray))
                frame = np.array(frame)
                # RGBtoBGR满足opencv显示格式
                frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
                self.imageNum = self.imageNum + 1
                fileName =  str(self.imageNum) + '.jpg'  # 存储路径
                cv.imwrite(fileName, frame, [cv.IMWRITE_JPEG_QUALITY, 100])
                print(fileName + " successfully write in")  # 输出存储状态

            elif self.frameState == False:
                break

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        # 当所有事完成，释放 VideoCapture 对象
        self.cap.release()
        cv.destroyAllWindows()
# body = BodyBoxing()
# body.body_boxing()
