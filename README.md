# SittingRestReminder
A tool to remind you to take a break during work

目的 Purpose  
如果长期间以一种姿势坐在电脑前，对脊椎（腰椎、颈椎）、对肛肠健康都不利。本人由于长期的坐姿不规范且长时间坐，导致出现了腰椎间盘突出和痔疮等疾病，所以自己动手编辑了该软件，用于强制自己在工作时进行休息。  
If you sit in front of the computer in one position for a long time, it is bad for the spine (lumbar spine, cervical spine) and anorectal health. Due to my long-term irregular sitting posture and sitting for a long time, I suffered from diseases such as lumbar disc herniation and hemorrhoids, so I edited this software myself to force myself to take a rest during work.  

介绍 Introduction  
基于TK的倒计时提醒休息软件  
Countdown reminder rest software based on TK  

函数说明 Function specification  
img_2_py.py:  
由于GUI界面上用到两个图片， 为了避免调用外部图片，将图片转换为16进制数据，并保存到Py文件中，方便主函数调用。  
Since two images are used on the GUI interface, in order to avoid calling the external image, the image is converted to hexadecimal data and saved to the Py file, which is convenient for the main function call.  
SittingRestReminder.py:  
运行主函数，采用schedule定时任务，定时调用GUI界面达到提醒休息目的。  
Main function. Use schedule to schedule tasks and call GUI interface periodically to remind rest.
