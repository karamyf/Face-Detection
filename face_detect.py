from face_functions import *
import cv2
import os
#from admin import cam_num


# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/*")


########### IMAGE ############

# pixels = imread('aa.png')
# classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
# bboxes = classifier.detectMultiScale(pixels)


# for box in bboxes:
# # extract
# x, y, width, height = box
# x2, y2 = x + width, y + height
# # draw a rectangle over the pixels
# rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)


# imshow('face detection', pixels)
# waitKey(0)
# destroyAllWindows()


###################### VIDEO #####################



ageProto = "deploy_age.prototxt"
ageModel = "age_net.caffemodel"

genderProto = "deploy_gender.prototxt"
genderModel = "gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# Load network
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)




numFrame = 0
if not os.path.exists('dataset'):
    os.makedirs('dataset')
# Load Camera
# Default Port 0
cam_num = 0
answer = input("Do you Want to Change Default Camera y/n : ")
if ( answer == "y" or answer == "yes" or answer == "Y" or answer == "YES" ):
    cam_num = int(input("Enter Camera Port: "))
    
cap=cv2.VideoCapture(cam_num,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FPS, 30)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    #   top,left,bottom,right
        face_img = frame[x2:x2 + x1, x1:x1 + y2].copy()
        blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]

        label = "{},{}".format(gender, age)




        cv2.rectangle(frame, (x1 - 20, y1 - 20), (x2 + 20, y2 + 30), (0, 200, 0), 2)
        cv2.rectangle(frame, (x1-20, y2-30), (x2+20, y2+35), (0, 200, 0), cv2.FILLED)
        cv2.putText(frame, name, (x1 - 20, y2 + 7), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        
        #display gender and age on the screen
        #cv2.putText(frame, label,(x1-20, y2+30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        
        counter_frame = 0
        if cv2.waitKey(1) & 0xFF == ord('k'):
            cv2.imwrite('dataset/' + str(counter_frame) + '.jpg', frame)
            counter_frame += 1
            
            
        MarkAttendance(name,gender,age)
        print("name :{} ".format(name))
        #print("{}{} ".format(age,gender))
        #dircname = os.path.dirname()
        #print("profile :{} ".format(dircname))


    cv2.imshow("Frame", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
