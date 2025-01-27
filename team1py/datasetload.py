from roboflow import Roboflow
import requests
import cv2
import os
# 데이터셋 다운로드
rf = Roboflow(api_key="v7qrBk52ZYAlleV3s8sM")
project = rf.workspace().project("aiprojetteam1")
dataset = project.version(15).download("yolov8")
