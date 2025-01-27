import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'   # 라이브러리 충돌 해결
#OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
#pip install nomkl
#pip install --upgrade ultralytics opencv-python
# pip install --upgrade fastapi uvicorn pydantic Pillow numpy requests python-multipart
# pip install -U numpy==1.26.0