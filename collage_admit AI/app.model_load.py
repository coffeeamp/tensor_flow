import tensorflow as tf
import keras

tf_model = keras.models.load_model('collage_admit AI\my_model.h5')
# 예측
예측값 = tf_model.predict([ [750, 3.70, 1] ])
print(예측값)