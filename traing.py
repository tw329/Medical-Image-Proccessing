import os
import cv2
import codecs
SUCCESS_NAME="benign"
SUCCESS_WIDTH=150
SUCCESS_HEIGHT=150
ERROR_NAME="malignant"
NUMSTAGES=5
METHOD="LBP"

OUT_TEXT=""
SUCCESS_NUM=0
for f in os.listdir(SUCCESS_NAME):
	img=cv2.imread(SUCCESS_NAME+"/"+f)
	img=cv2.resize(img, (SUCCESS_WIDTH,SUCCESS_HEIGHT))
	cv2.imwrite(SUCCESS_NAME+"/"+f,img)
	OUT_TEXT+=SUCCESS_NAME+"/"+f+" 1 0 0 "+str(SUCCESS_WIDTH)+" "+str(SUCCESS_HEIGHT)+"\n"
	SUCCESS_NUM+=1

f=codecs.open(SUCCESS_NAME+".txt","w")
f.write(OUT_TEXT)
f.close()

OUT_TEXT=""
ERROR_NUM=0
for f in os.listdir(ERROR_NAME):
	OUT_TEXT+=ERROR_NAME+"/"+f+"\n"
	ERROR_NUM+=1

f=codecs.open(ERROR_NAME+".txt","w")
f.write(OUT_TEXT)
f.close()
print("===opencv_createsamples===")
os.system("opencv_createsamples.exe -info "+SUCCESS_NAME+".txt -vec "+SUCCESS_NAME+".vec -bg "+ERROR_NAME+".txt -num "+str(SUCCESS_NUM)+" -w "+str(SUCCESS_WIDTH)+" -h "+str(SUCCESS_HEIGHT))
print("===opencv_traincascade===")
os.system("opencv_traincascade.exe -data xml/ -vec "+SUCCESS_NAME+".vec -bg "+ERROR_NAME+".txt -numPos "+str(SUCCESS_NUM)+" -numNeg "+str(ERROR_NUM)+" -numStages "+str(NUMSTAGES)+" -featureType "+METHOD+" -w "+str(SUCCESS_WIDTH)+" -h "+str(SUCCESS_HEIGHT)+" -precalcValBufSize 4048 -precalcIdxBufSize 4048 -numThreads 24 -maxFalseAlarmRate 0.5 -minHitRate 0.995")
