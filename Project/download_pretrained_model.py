import gdown
import os
os.system('mkdir model')
gdown.download_folder('https://drive.google.com/drive/folders/1q4pko-X0AM7rrMFzqis1uhfktD15YrHA?usp=drive_link', output = 'model/yolov7/',quiet=True)
gdown.download_folder('https://drive.google.com/drive/folders/1lGkab2rChQY8SEs54K-dJUHCZ2oRfyaH?usp=drive_link', output = 'model/yolov5/', quiet=True)
gdown.download_folder('https://drive.google.com/drive/folders/1QwOc17xD_hEGcns0Bgbkw3mA8Q4sMo4t?usp=drive_link', output = 'model/yolov8/', quiet=True)
gdown.download_folder('https://drive.google.com/drive/folders/1niJxRUEZ3CT_AvAzrAQkMhZiNrgXlGTJ?usp=drive_link', output = 'model/yolov6/', quiet=True)
