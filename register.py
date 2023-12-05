import cv2 as cv
import pandas as pd

face_cascade = cv.CascadeClassifier("content\haarcascade_frontalface_default.xml")
cam=cv.VideoCapture(0)
Id = int(input("enter your id number"))
Name = input("Enter your name")
df2 = pd.Dataframe({"Id": [Id], "Name": [Name]})
df = pd.concat([df, df2]).drop_duplicates(),df.reset_index(drop=True)
df.to_csv("content\oye.csv",index=False)
sampleNum = 0
while True:
    ret, img = cam.read()
    faces=face_cascade.detectMultiScale(img,1.3,5)
    for(x, y ,w ,h) in faces:
        cv.rectangle(img ,(x, y),(x+w, y+h), (144,1,1),3)
        sampleNum = sampleNum+1
        #saving data in oye
        cv.imwrite("content" +Id+ '.' + (sampleNum + ".jpg"))
        cv.imshow('frame' ,img)
    if cv.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum>10:
        break
    cam.release()
    cv.destroyAllWindows()