# Import necessary modules
import numpy as np
import pandas as pd
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping

filepath = "unedited/"
dtr = pd.read_csv('train.csv')
pred_data = pd.read_csv('test.csv')
pred_data = pred_data.values

predictors = dtr.drop(["label"], axis=1).as_matrix()

target = to_categorical(dtr.label)

# Create the model: model
model = Sequential()

# Add the first hidden layer
model.add(Dense(50,activation='relu',input_shape=(784,)))

# Add the second hidden layer
model.add(Dense(50,activation='relu'))

# Add the second hidden layer
model.add(Dense(50,activation='relu'))

# Add the second hidden layer
model.add(Dense(50,activation='relu'))


# Add the output layer
model.add(Dense(10,activation='softmax'))

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=3)

# Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

early_stopping_monitor = EarlyStopping(patience=3)

# Fit the model
model.fit(predictors,target, validation_split=0.3, epochs = 40, callbacks = [early_stopping_monitor] )

#ids = np.arange(1,785,1)
#output = pd.DataFrame({'Label': predictions }, index=[1])
#output.to_csv('hwdr_predictions.csv', index = False)
#output.head()

print("Generating test predictions...")
preds = model.predict_classes(pred_data, verbose=0)

def write_preds(preds, fname):
    pd.DataFrame({"ImageId": list(range(1,len(preds),1)), "Label": preds}).to_csv(fname, index=False, header=True)

write_preds(preds, "keras3-mlp.csv")