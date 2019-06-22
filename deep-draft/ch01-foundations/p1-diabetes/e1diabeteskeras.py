# ---
# Goal
# ---
# Create and train a simple neural network to predict whether
# a person has had an onset of diabetes given eight medical attributes
# This data set of 768 samples is from the UCI machine learning repository
# See associated text file `diabetes-dataset-info.txt` for more details

# Adapted from
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# https://www.kaggle.com/atulnet/pima-diabetes-keras-implementation

# --
# PIPELINE
# --

# Load Data.
# Define Model.
# Compile Model.
# Fit Model.
# Evaluate Model.
# Use Model to predict


import tensorflow as tf
from tensorflow.keras import layers
import numpy

print("Versions:")
print("Tensorflow:", tf.VERSION)
# 1.14.0-rc1
print("Keras: ", tf.keras.__version__)
#2.2.4-tf

# Fix random seed for reproducibility
numpy.random.seed(7)

# Load pima indians dataset
path = "./pima-indians-diabetes.data.csv"
dataset = numpy.loadtxt(path, delimiter=",")

# Split into input (X) and output (Y) variables
X = dataset[:, 0:8]
Y = dataset[:, 8]

# Inspect one sample
n = 1
print("--\n", "Attributes for sample:", n, "\n--\n")
print('{:40.35} {:2.3f}'.format("Number of times pregnant", X[n][0]))
print('{:40.35} {:2.3f}'.format("Plasma glucose concentration", X[n][1]))
print('{:40.35} {:2.3f}'.format("Diastolic blood pressure (mm Hg)", X[n][2]))
print('{:40.35} {:2.3f}'.format("Triceps skin fold thickness (mm)", X[n][3]))
print('{:40.35} {:2.3f}'.format("2-Hour serum insulin (mu U/ml)", X[n][4]))
print('{:40.35} {:2.3f}'.format("Body mass index kg/m^2)", X[n][5]))
print('{:40.35} {:2.3f}'.format("Diabetes pedigree function", X[n][6]))
print('{:40.35} {:2.3f}'.format("Age (yrs) ", X[n][7]))

print("-------------------------------------------------------")
print('{:40.35} {:1.1f}'.format("Diabetes?  Y/N (1/0)", Y[n]))
print()

# Define model
model = tf.keras.Sequential()
model.add(layers.Dense(12, input_dim=8, activation='relu'))
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# KNOWN WARNING
# calling VarianceScaling.__init__ (from tensorflow.python.ops.init_ops)
# with dtype is deprecated and will be removed in a future version.

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# KNOWN ISSUE
# add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated

# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)

# Epoch 150/150
# loss: 0.4875 - acc: 0.7812

model.summary()

# Model: "sequential"
# Layer (type)                 Output Shape              Param #
# dense (Dense)                (None, 12)                108
# dense_1 (Dense)              (None, 8)                 104
# dense_2 (Dense)              (None, 1)                 9
# Total params: 221
# Trainable params: 221
# Non-trainable params: 0

# Calculate predictions
predictions = model.predict(X)

print(" sample | probability | predicted | actual | correct")
for i, (p, a) in enumerate(zip(predictions, Y)):
  print('{:7d} | {:11.3f} | {:9d} | {:6d} | {:5}'.format(
         i, float(p), round(int(p)), int(a), str(int(p) == a)))

# sample | probability | predicted | actual | correct
#      0 |       0.771 |         0 |      1 | False
#      1 |       0.112 |         0 |      0 | True
#      2 |       0.895 |         0 |      1 | False
#      3 |       0.097 |         0 |      0 | True
