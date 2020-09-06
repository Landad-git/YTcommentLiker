# YTcommentLiker
Small python script to identify and like youtube comments


#MODULE LIST
in order to run this code you need to install python 3.8 and import the follow via pip install

pip install pyautogui
pip install win32api   #if this doesn't install just continue on
pip install pypiwin32
pip install keyboard
pip install pywin32


#FILES
There are two images: one for youtube in dark mode and one for youtube in light mode. The code needs to be edited to know which one you are using.
change the like variable to likeicondm.png for darkmode and likeicon.png for normal mode

#PERFORMANCE TUNING
on line #21 there is a function  region=(x,y,xd,yd)   which tells the program where to look for the icon and this is setup to look from X pixel 50 to X pixel 250 for the button. 
If the code is not finding any buttons change the 50 to 0 and the 200 to 1000 and make sure youtube is in full screen and the code is executed on the same monitor

