#demo
import streamlit as st
import requests
import os
import importlib
from datetime import datetime
import glob

#select model
# st.markdown(''':rainbow[Select your model] ☃️''')
model_list = ["yolov5", "yolov6", "yolov7", "yolov8"]
ver_dict = {
    None: [],
    "yolov5": ["nano", "small", "medium", "large", "x"],
    "yolov6": ["nano", "small", "medium", "large"],
    "yolov7": ["", "tiny", "x", "w6", "e6", "d6"],
    "yolov8": ["nano", "small", "medium", "large"]}
opt_dict = {
    None: [],
    "yolov5": ["SGD", "Adam"],
    "yolov6": ["SGD", "Adam"],
    "yolov7": ["SGD"],
    "yolov8": ["SGD"]}
model_root = st.selectbox(
    '**:rainbow[Select your model]** ☃️', 
    model_list,
    index=None,
    placeholder="Select your model...")
version = st.selectbox(
    '', 
    ver_dict[model_root],
    index=None,
    placeholder="Select model version...",
    label_visibility="collapsed")
optimizer = st.selectbox(
    '', 
    opt_dict[model_root],
    index=None,
    placeholder="Select optimizer...",
    label_visibility="collapsed")
image_size = 640
if (model_root=="yolov7" and version in ["w6", "d6", "e6"]):
    image_size = 1280
st.write(image_size)

#upload
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.image(uploaded_file)
    st.write("filename:", uploaded_file.file_id, "\n")
    if (uploaded_file.file_id): 
        image_name = uploaded_file.file_id+'.jpg'
        image_path = "demo/uploaded_images/"+image_name
        if (os.path.isfile(image_path)==False):
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
                f.close()

#load model
def option2pyt(model, version, opt, size):
    root = ""
    version2opt = {
        'tiny' : 'tiny',
        '' : '',
        'nano' : 'n',
        'small' : 's',
        'medium' : 'm',
        'large' : 'l',
        'x' : 'x',
        'w6' : 'w',
        'e6' : 'e',
        'd6' : 'd'
    }
    size2opt = {
        640 : '',
        1280 : '6'
    }
    opt2opt = {
        'SGD' : '',
        'Adam' : '_adam'
    }
    model2inf = {
        'yolov5' : 'python ' + root + 'repo/yolov5/detect.py',
        'yolov6' : 'python ' + root + 'tools/infer.py',
        'yolov7' : 'python ' + root + 'detect.py',
        'yolov8' : 'yolo predict'
    }
    return model2inf[model], 'model/' + model + '/' + model + version2opt[version] + size2opt[size] + opt2opt[opt] + '.pt'

hide_labels = st.checkbox('Hide label')
hide_conf = st.checkbox('Hide confident')
if st.button('Predict'):
    opt_hide_labels = ['', '--hide-labels'][int(hide_labels)]
    opt_hide_conf = ['', '--hide-conf'][int(hide_conf)]
    if (model_root and version and optimizer):
        inference, pt = option2pyt(model_root, version, optimizer, image_size)
    if (model_root!='yolov5'):
        pt = '../../'+pt
    url = ""
    name = ""
    for uploaded_file in uploaded_files:
        if (uploaded_file.file_id): 
            name = str(datetime.now()).replace(' ', '').replace('-', '').replace(':', '').replace('.', '')
            image_name = uploaded_file.file_id+'.jpg'
            url = "demo/uploaded_images/"+image_name
            if (model_root!='yolov5'):
                url = '../../'+url
            infer_call = {
                'yolov5' : f'{inference} --weights {pt} --source {url} --name {name} {opt_hide_labels} {opt_hide_conf} --line-thickness 1',
                'yolov6' : f'{inference} --weights {pt} --source {url} --name {name} {opt_hide_labels} {opt_hide_conf}',
                'yolov7' : f'{inference} --weights {pt} --source {url} --name {name} {opt_hide_labels} {opt_hide_conf}',
                'yolov8' : f'{inference} model={pt} source={url} name={name}'
            }

#predict and save output
            if (model_root=='yolov6'):
                os.chdir('repo/yolov6')
            if (model_root=='yolov7'):
                os.chdir('repo/yolov7')
            if (model_root=='yolov8'):
                os.chdir('repo/ultralytics')
            call_arg = infer_call[model_root]
            os.system(call_arg)
            if (model_root!='yolov5'):
                os.chdir('..')
                os.chdir('..')

            save_path = {
                'yolov5' : 'repo\\yolov5\\runs\\detect\\',
                'yolov6' : 'repo\\yolov6\\runs\\inference\\',
                'yolov7' : 'repo\\yolov7\\runs\\detect\\',
                'yolov8' : 'repo\\ultralytics\\runs\\detect\\',
            }
            print(model_root)
            print(name)
            img_path = (glob.glob(save_path[model_root] + name + '\\*.*')[0])#.replace('\\', '/')
            save_command = 'copy '+img_path+' demo\\demo_results\\'+model_root+'\\'+name+'.jpg'
            print(save_command)
            os.system(save_command)

#show output
            st.image(img_path)


