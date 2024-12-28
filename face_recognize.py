# It helps in identifying the faces 
import cv2, sys, numpy, os 
import mysql.connector 
size = 4
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
  
# Part 1: Create fisherRecognizer 
print('Recognizing Face Please Be in sufficient Lights...') 
  
# Create a list of images and a list of corresponding names 
(images, lables, names, id) = ([], [], {}, 0) 
for (subdirs, dirs, files) in os.walk(datasets): 
    for subdir in dirs:
        #print(subdir)
        names[id] = subdir 
        subjectpath = os.path.join(datasets, subdir) 
        for filename in os.listdir(subjectpath): 
            path = subjectpath + '/' + filename 
            lable = id
            images.append(cv2.imread(path, 0)) 
            lables.append(int(lable)) 
        id += 1
(width, height) = (130, 100) 
  
# Create a Numpy array from the two lists above 
(images, lables) = [numpy.array(lis) for lis in [images, lables]]
#print(images)
  
# OpenCV trains a model from the images 
# NOTE FOR OpenCV2: remove '.face' 
model = cv2.face.LBPHFaceRecognizer_create() 
model.train(images, lables) 
# Part 2: Use fisherRecognizer on camera stream 
face_cascade =  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#print("hello1")
webcam = cv2.VideoCapture(0)


while True: 
    (_, im) = webcam.read() 
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces: 
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
        face = gray[y:y + h, x:x + w] 
        face_resize = cv2.resize(face, (width, height)) 
        # Try to recognize the face 
        prediction = model.predict(face_resize) 
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3) 
        a=prediction
  
        if prediction[1]<500: 
  
           cv2.putText(im, '% s - %.0f' % 
(names[prediction[0]], prediction[1]), (x-10, y-10),  
cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
           mydb=mysql.connector.connect(host="localhost",user="root", passwd="goutham",database="students")
           mycursor=mydb.cursor()
           sql=('UPDATE student SET Date=CURRENT_TIMESTAMP()  where Rollno = %s;'%(names[prediction[0]]),)
           sql1=('UPDATE student SET Attendance=1  where Rollno = %s;'%(names[prediction[0]]),)
           mycursor.execute(*sql)
           mycursor.execute(*sql1)
           mydb.commit()
           
        else: 
          cv2.putText(im, 'not recognized',  
(x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0)) 
  
    cv2.imshow('OpenCV', im) 
      
    key = cv2.waitKey(10) 
    if key ==13 : 
    	break
    


















