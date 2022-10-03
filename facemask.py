import os
import cv2
import tensorflow
import keras.models

import numpy as np
from tensorflow.keras.models import model_from_json
import streamlit as st
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')


def detect_face_mask(img):
    # y_pred=model.predict_classes(img.reshape(1,224,224,3))
    y_pred = (loaded_model.predict(img.reshape(1, 224, 224, 3)) > 0.5)*1

    return y_pred[0][0]


def draw_label(img, text, pos, bg_color):
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, cv2.FILLED)

    end_x = pos[0]+text_size[0][0]+2
    end_y = pos[0]+text_size[0][1]-2

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, cv2.FILLED)
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 0), 1, cv2.LINE_AA)


def detect_face(img):
    coods = haar.detectMultiScale(img)
    return coods


haar = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


with open("model.json", "r") as file:
    model_read = file.read()

loaded_model = model_from_json(model_read)
loaded_model.load_weights("weight.h5")


st.title("Face Mask Detection")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
