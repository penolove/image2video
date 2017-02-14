import os 
import glob
import cv2

from cv2 import VideoWriter,  imread, resize


if __name__=="__main__":
    target_dir_Jpg = os.path.join(os.getcwd(), 'frames')
    target_dir_frame_pattern = os.path.join(target_dir_Jpg,'*.jpg')
    target_dir_frame_list = glob.glob(target_dir_frame_pattern)
    target_video = os.path.join(os.getcwd(), 'target.avi')
    print target_video
    img = imread(target_dir_frame_list[0])
    shape = (img.shape[0],img.shape[1])
    fps = 20
    fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v') # note the lower case
    fourcc = cv2.cv.CV_FOURCC('M','P','E','G')
    vout = cv2.VideoWriter()
    success = vout.open(target_video,fourcc,fps,shape,True) 
    for image in target_dir_frame_list:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = imread(image)
        vout.write(img)
    vout.release()
    cv2.destroyAllWindows()

