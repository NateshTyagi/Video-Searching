import cv2
import os
from imageai.Detection import ObjectDetection
from glob import glob
import pytesseract
import numpy as np
from matplotlib import pyplot as plt
import moviepy.editor as mp
import speech_recognition as sr

#path='images'
#if not os.path.exists(path):
#	os.makedirs(path)
vidcap = cv2.VideoCapture('ENCOURAGEMENT.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(os.path.join("frame "+str(sec)+" sec.jpg"), image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1
#it will capture image in each 0.5 second
success = getFrame(sec)
while success:
    sec = sec + frameRate
    #sec = round(sec, 2)
    success = getFrame(sec)
    
execution_path = os.getcwd()

for i in glob('*.jpg'):
	img = cv2.imread(os.path.basename(i))  #This line will read the image file..
	print("the filename is:", os.path.basename(i))
	print( pytesseract.image_to_string(img))#this line will print the text document in command line
    
    
print('the execution path is', execution_path)
#filename_queue = tf.train.string_input_producer(tf.train.match_filenames_once("./images/*.jpg"))

for i in glob('*.jpg'):# here datasets is the directory name where all your files are kept. if you have in the same directory then no need to put directory name
	input_file= os.path.basename(i)# This will have all the input file in the directory
	print("the file name is", input_file)
	output_file=input_file+"_new.jpg"#this statement stores the new input file name as eg. 4_new_.jpg
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	#detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "4.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
	detections = detector.detectObjectsFromImage(input_image=input_file, output_image_path= output_file)
	print("the detection is done in", output_file)

	for eachObject in detections:
		print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        
 

clip = mp.VideoFileClip("ENCOURAGEMENT.mp4").subclip(0,3600)
clip.audio.write_audiofile("theaudio.wav")
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "theaudio.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

#recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))