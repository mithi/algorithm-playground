# SESSION 2: COMPUTER VISION AND TRANSFER LEARNING

## Learning Goals
- Understand what the convolution and related operations are and why they are useful for neural networks to understand image data
- Understand the basic building blocks of convolutional neural network architectures (layer patterns) and terminologies used
- Learn what transfer learning is, why and how you should use it
- Build your own CNN image classifier from scratch like for german traffic signs as an example
- Use transfer-learning to classify a very small set of training images (like maybe 120 images of birds and bees)

# Videos
- [(Ava Soleimany) Deep Computer Vision 2019 MIT Lecture](https://www.youtube.com/watch?v=H-HVZJ7kGI0&index=1&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)
- [(Fernanda Viegas) Data Visualization for Machine Learning](https://www.youtube.com/watch?v=ulLx2iPTIcs&index=1&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)

# Code
- [PYTORCH: Train a CNN classifier for CIFAR10](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)
- [(Sasank Chilamkurthy) PYTORCH: Transfer Learning Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)

## Going beyond
- Be familiarized with data augmentation techniques
- Be familiarized on some techniques on how to visualize what and how CNNs learn and see
- Be familiarized about the idea of adversarial examples and how it can fool image classifiers
- You might also be interested to try [Object detection](http://course18.fast.ai/lessons/lesson8.html)

> Object detection, which means getting a model to draw a box around every key object in an image, and label each one correctly. - Fast AI

> I like to summarize this point as “don’t be a hero”: Instead of rolling your own architecture for a problem,
you should look at whatever architecture currently works best on ImageNet, download a pretrained model and finetune
it on your data. You should rarely ever have to train a ConvNet from scratch or design one from scratch. - Andrej Karpathy


## References

- CS231n: Convolutional Neural Networks for Visual Recognition Course Notes by Andrej Karpathy
  - [Convolutional Neural Networks: Architectures, Convolution / Pooling Layers ](http://cs231n.github.io/convolutional-networks/)
  - Visualizing what ConvNets learn (draft)
  - Transfer learning (draft)
- [Daniel Nouri 2014, Using convolutional neural nets to detect facial keypoints tutorial](http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/)
- [(Olah) Conv Nets: A Modular Perspective Posted on July 8, 2014](http://colah.github.io/posts/2014-07-Conv-Nets-Modular/)
