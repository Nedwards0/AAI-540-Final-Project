import os
import cv2
from pathlib import Path
import datetime
import json


class DataFile():
    def __init__(self, Path: str, Class: str, video : str):
        self.Path = Path
        self.Class = Class
        self.video = video

class Proccessor:
    Version = '0.0.0'
    
    def __init__(self, Path: str):
        self.Dataset_Path =  Path
        self.classes = os.listdir(self.Dataset_Path)
    def getClasses(self):
        return(self.classes)
    def getVideosForClass(self, className):
        if(className in self.classes):
            folder = self.Dataset_Path + "/" + className
            files = os.listdir(folder)
            Datafiles = [DataFile((self.Dataset_Path + "/" + className + "/" + file), className, file) for file in files]
            return Datafiles
        else:
            print("This is not a class in the dataset")
    def convertVideoToImages(self, datafile: DataFile, Generate_Label_Info_As_Json=True, Export_Dir = "Images", split_by_video=True):
        print(datafile.Path)
        vidcap = cv2.VideoCapture(datafile.Path)
        success,image = vidcap.read()
        count = 0
        success = True
        if(split_by_video):
            Folder_write_location =  Export_Dir + "/" + datafile.Class + "/" + datafile.video + "/"
        else:
            Folder_write_location =  Export_Dir + "/" + datafile.Class + "/"
        Path(Folder_write_location).mkdir(parents=True, exist_ok=True)
        while success:        
            cv2.imwrite(Folder_write_location + "frame%d.jpg" % count, image)
            success,image = vidcap.read()
            count += 1
            if(Generate_Label_Info_As_Json):
                json_to_write={
                    'class':datafile.Class,
                    'video':datafile.video,
                    'processorVersion':self.Version,
                    'procesedWhen': str(datetime.datetime.now())
                }
                with open( (Folder_write_location + "metaData%d.json" % count), "w", encoding='utf-8') as outfile:
                    json.dump(json_to_write, outfile, ensure_ascii=False, indent=4)
        return 1

if __name__ == "__main__":

    # This is Testing code not meant to be used in producation
    print("Starting Test")
    process = Proccessor("UCF-101") # Assumes Folder is located at same level as code.
    classes = process.getClasses()
    class_count = 101
    assert (len(classes) ==  class_count) #Verifys Right amount of classes in dataset. Hard coded 
    assert(len(process.getVideosForClass(classes[0])) == 145)
    total_vid_count = 0
    for item in classes:
        total_vid_count += len(process.getVideosForClass(item))
    toal_video = 13320
    assert(total_vid_count == toal_video)
    assert(process.convertVideoToImages(process.getVideosForClass(classes[0])[0]))

