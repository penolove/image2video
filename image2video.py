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
    height , width , layers =  img.shape

    video = cv2.VideoWriter('video.avi',-1,1,(width,height))

    for image in target_dir_frame_list:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = imread(image)
        video.write(img)
    cv2.destroyAllWindows()
    video.release()

