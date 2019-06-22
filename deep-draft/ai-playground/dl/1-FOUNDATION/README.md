# SESSION 1: FOUNDATIONS

## :pushpin:LEARNING GOALS
- Understand what a simple feedforward neural network is and how to train them to be able to do stuff
- Learn basic deep learning terminologies and concepts which you will use all the time
- Write code in TensorFlow 2.0 to train simple models like for classifying images of clothing and predicting fuel efficiency

## :pushpin:LECTURE

### :tv:[MIT: Introduction to Deep Learning 2019](https://www.youtube.com/watch?v=5v1JnYv_yWs&index=1&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)
  - 45-Minute Video by Alexander Amini [Slides](http://introtodeeplearning.com/materials/2019_6S191_L1.pdf)

## :pushpin:NOTES

### The Neuron and the Simple Feedforward Network
- Inputs and Outputs, Weights and Biases
- Activation Functions, Hidden and Fully-Connected Layers

### Inputs and Outputs
- Feature selection and feature preprocessing, normalize
- Representations of inputs (features) and outputs
- One-hot encoding, softmax

### The Training Process (One Way to look at it)
1. Set up the architecture
2. Set up the data and  the loss
3. Learning and evaluation

### The Training Process (Another way to look at it)
1. Prepare a balanced dataset (use techniques to avoid bias)
  - split data into training set and test set
2. Define your "neural network architecture" and initialize weights
3. Train and evaluate your model
  - loss functions, optimization algorithms, and others
4. Save and restore your model
  - Experiment with different possible parameters and retrain
  - Hopefully you get a better performing model


### Training and Evaluation
- Error / loss functions
- Optimization Algorithms
- Evaluation metrics
- Gradient Descent and Backpropagation
- Exploding and vanishing gradient problem

### Some Tunable Hyperparameters
- Batchsize, Epochs, Learning Rate
- Weight Initialization

### Overfitting and Underfitting
- Some techniques to avoid them
- L2 Regularization, Dropouts, Pooling (for CNN)
- A different model, Get more data, Get better data
- Cross-validated Evaluation?? Ensemble learning??

## Terms you might encounter that you don't need right now (we will discuss them in the future)
- RNN, CNN, LSTM, Convolution

## :pushpin:OPTIONAL READINGS
- [(Andrej Karpathy) Stanford: Intro to Neural Networks, Stanford](http://cs231n.github.io/neural-networks-1/#actfun)
- [(Samay Shamdasani) Enlight: Build a Neural Network](https://enlight.nyc/projects/neural-network/)
- [(Joseph Lee Wei En) Build your first Neural Network to predict house prices with Keras](https://hackernoon.com/build-your-first-neural-network-to-predict-house-prices-with-keras-3fb0839680f4)
- [(Tyler Elliot Bettilyon) How to classify MNIST digits with different neural network architectures](https://medium.com/tebs-lab/how-to-classify-mnist-digits-with-different-neural-network-architectures-39c75a0f03e3)
- [(Michael A. Nielsen) Using neural nets to recognize handwritten digits](http://neuralnetworksanddeeplearning.com/chap1.html)
- [(Mithi Sevilla) Machine Learning Intuitions](https://docs.google.com/presentation/d/1k5E_dpSk3PzaO-HvwMeOy-UIGHSsVCsVcPXoDzdVa1o/edit#slide=id.g4213f1dd40_0_328)
- [Python Course EU Neural Network Hand Written Digits Minist](https://www.python-course.eu/neural_network_mnist.php)
- [(Raheel Shaikh) Feature Selection Techniques in Machine Learning with Python](https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e)
- [(James Dellinger) Weight Initialization in Neural Networks: A Journey From the Basics to Kaiming](https://towardsdatascience.com/weight-initialization-in-neural-networks-a-journey-from-the-basics-to-kaiming-954fb9b47c79)
- [(Pedro Domingos) A Few Useful Things to Know about Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf)
