import os
os.system('mkdir repo')
os.chdir('repo')
os.system('git clone https://github.com/ultralytics/yolov5.git')
os.system('git clone https://github.com/meituan/YOLOv6.git')
os.system('git clone https://github.com/WongKinYiu/yolov7.git')
os.system('git clone https://github.com/ultralytics/ultralytics.git')
os.system('pip install ultralytics')
os.system('pip install -r yolov5/requirements.txt')
os.system('pip install -r yolov6/requirements.txt')
os.system('pip install -r yolov7/requirements.txt')



