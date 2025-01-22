# !pip install ultralytics tensorflow roboflow numpy
import tensorflow as tf
from tensorflow import keras
from roboflow import Roboflow
import numpy as np
import os

# GPU 메모리 설정
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

# Roboflow 설정
rf = Roboflow(api_key="your_api_key")
project = rf.workspace("your_workspace").project("your_project")
version = project.version(1)

# 데이터셋 다운로드
dataset = version.download("tensorflow")

# 모델 다운로드
save_dir = "downloaded_model"
os.makedirs(save_dir, exist_ok=True)
version.model.download("keras", save_dir)

# 모델 로드
model = keras.models.load_model(os.path.join(save_dir, "model.h5"))

# 데이터 제너레이터 설정
train_datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
)

# 데이터 로드
train_generator = train_datagen.flow_from_directory(
    os.path.join(dataset.location, "train"),
    target_size=(640, 640),  # 모델의 입력 크기에 맞게 조정
    batch_size=32,
    class_mode='categorical'
)

validation_generator = val_datagen.flow_from_directory(
    os.path.join(dataset.location, "valid"),
    target_size=(640, 640),
    batch_size=32,
    class_mode='categorical'
)

# 콜백 설정
callbacks = [
    keras.callbacks.ModelCheckpoint(
        "best_model.h5",
        monitor='val_loss',
        save_best_only=True,
        mode='min'
    ),
    keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.1,
        patience=3,
        min_lr=1e-6
    )
]

# 모델 컴파일
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 추가 학습
history = model.fit(
    train_generator,
    epochs=100,
    validation_data=validation_generator,
    callbacks=callbacks
)

# 학습 결과 시각화
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

# 손실 그래프
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

# 정확도 그래프
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

# 모델 평가
evaluation = model.evaluate(validation_generator)
print(f"Validation Loss: {evaluation[0]}")
print(f"Validation Accuracy: {evaluation[1]}")

# 최종 모델 저장
model.save("final_model.h5")