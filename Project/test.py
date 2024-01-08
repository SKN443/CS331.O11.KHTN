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


show_pages(
        [
            Page("demo.py", "Home", "🏠"),
            Page("uploaded.py", "Uploaded Images", "🏞️"),
            Page("store.py", "History", "🏬")
        ]
    )

st.header('Step 1: Upload your images')

files = st.file_uploader('', accept_multiple_files=True)
for file in files:
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    upimg = cv2.imdecode(file_bytes, 1)
    cv2.imwrite('demo/uploaded_images/' + file.name, upimg)

files = glob('demo/uploaded_images/*.*')

st.text("")
st.header('Step 2: Select an image to predict and push predict button')
st.text("")

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
with control[3]:
    num_batches = ceil(len(files)/8)
    page = st.selectbox("Page", range(1,num_batches+1))

try:
    img = image_select(
        label="",
        images=files[(page-1)*8:min(len(files), page*8)],
        captions=[i[len('demo/uploaded_images/'):] for i in files[(page-1)*8:min(len(files), page*8)]],
        use_container_width=False,
    )
except Exception:
    pass
tmp = st.columns(5)
with tmp[2]:
    st.button('Predict!')

st.text("")
st.header('Step 3: Result!')
st.text("")