import mediapipe as mp
import cv2





class HandTracking:
    
    def __init__(self,mode=False,maxHands = 1 , detectionCon = 0.5 , trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = 0.5

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):

        imageRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms , self.mpHands.HAND_CONNECTIONS)
        
        return img

    def findXPosition(self,img , handNo = 0 ):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id,lm in enumerate(myHand.landmark):
                cx ,cy = lm.x , lm.y

                lmList.append([id,cx,cy])
        
        return lmList


