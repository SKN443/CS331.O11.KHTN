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

st.header('Welcome to our demo CS331!')
