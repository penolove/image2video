# image2video

#require to install ffmpeg
https://www.faqforge.com/linux/how-to-install-ffmpeg-on-ubuntu-14-04/

```
cd frames
ffmpeg -f image2 -i %06d.jpg -s 320x240 video.avi
```
