# image2video

#require to install ffmpeg
https://www.faqforge.com/linux/how-to-install-ffmpeg-on-ubuntu-14-04/

```
cd frames
ffmpeg -f image2 -i %06d.jpg -s 320x240 video.avi
```

-r 24 (which means fps = 24)
[ref]
http://wilsbur.pixnet.net/blog/post/146836324-ffmpeg%E5%B8%B8%E7%94%A8%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9
