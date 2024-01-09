import os
os.system('mkdir repo')
os.system('mkdir demo')
os.chdir('demo')
os.system('mkdir uploaded_images')
os.system('mkdir demo_results')
os.chdir('demo_results')
os.system('mkdir yolov5')
os.system('mkdir yolov6')
os.system('mkdir yolov7')
os.system('mkdir yolov8')
os.chdir('../../repo')
os.system('git clone https://github.com/ultralytics/yolov5.git')
os.system('git clone https://github.com/meituan/YOLOv6.git')
os.system('git clone https://github.com/WongKinYiu/yolov7.git')
os.system('git clone https://github.com/ultralytics/ultralytics.git')
os.system('pip install ultralytics')
os.system('pip install -r yolov5/requirements.txt')
os.system('pip install -r yolov6/requirements.txt')
os.system('pip install -r yolov7/requirements.txt')



