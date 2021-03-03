import cv2
# defining face detector
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
ds_factor=0.6

video = cv2.VideoCapture(0)



def trial_frame():
       #extracting frames
    #ret, frame = self.video.read()
    
    frame =cv2.imread("original.png")
   
    frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)                    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_rects=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray,
                scaleFactor = 1.5, minNeighbors = 15, minSize = (25,25))
        for i in smiles:
            if len(smiles)>1 :
                cv2.putText(frame,"Smiling",(30,30),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,
                cv2.LINE_AA)
                haarcas_output = "haarcas_selfie.png"
                cv2.imwrite(haarcas_output,frame)
        break
        # encode OpenCV raw frame to jpg and displaying it
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()