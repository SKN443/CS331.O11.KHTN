# CS331.O11.KHTN
Repository uses in course CS331.O11.KHTN - Advanced computer vision
## About the course
- **University**: University of Information Technology - VNUHCM UIT.
- **Faculty**: Computer Science
- **Semester**: 1
- **Year**: 2023 - 2024
- **Lecturer**: Mai Tiến Dũng
## About the group 11
|**Student ID**| **Member**|**Email**|
|-----------|-----------|-----------|
|21522407|Phan Trọng Nhân|21522407@gm.uit.edu.vn|
|21522034|Nguyễn Hoàng Hải|21522034@gm.uit.edu.vn|

## Usage

<details open>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/SKN443/CS331.O11.KHTN/blob/master/requirements.txt) in a
[**Python>=3.11.0**](https://www.python.org/) environment

```bash
git clone https://github.com/SKN443/CS331.O11.KHTN.git  # clone
cd CS331.O11.KHTN
pip install -r requirements.txt  # install
```
</details>

<details open>
<summary>Preparing pretrained models</summary>

Open the terminal in the ``Project`` folder and execute [initialization.py](https://github.com/SKN443/CS331.O11.KHTN/blob/main/Project/initialization.py) for download pretrained model to local \
(it will take time due to these large models)

```bash
cd Project
python initialization.py 
```
</details>

<details open>
<summary>Host app</summary>

Running [test.py](https://github.com/SKN443/CS331.O11.KHTN/blob/main/Project/test.py) to host your app:

```python
streamlit run test.py
```

</details>
