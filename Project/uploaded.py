from glob import glob
import streamlit as st
import string
import random
import numpy as np
import cv2
from streamlit_image_select import image_select
from math import ceil
from pathlib import Path

from st_pages import Page, show_pages, add_page_title


st.markdown(
    """
    <style>
    [data-baseweb="select"] {
        margin-top: -50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
control = st.columns(4)
# with control[0]:
#     version = st.selectbox("", ('yolov5', 'yolov6', 'yolov7', 'yolov8'))
files = glob('demo/uploaded_images' + '/*.*')

with control[3]:
    num_batches = ceil(len(files)/8)
    page = st.selectbox("", range(1,num_batches+1))
try:
    img = image_select(
        label="",
        images=files[(page-1)*8:min(len(files), page*8)],
        captions=[i[len('demo/demo_results/')+6:] for i in files[(page-1)*8:min(len(files), page*8)]],
        use_container_width=False,
    )
    st.image(img)
except Exception:
    pass