# Introduction to Pytorch

- [Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
- [PyTorch Introduction Playground](../../../old-ntbks/pytorch-notebooks/)

# Summary
- Tensors and Pytorch
- Autograd and Functions
- Neural Networks
- NOTE: Don't worry if you don't understand the convolution operation just yet

### Tensors
- Tensors are just like numpy arrays that can use GPUs / Parallel processing
- Tensors are just list of lists of list of numbers (like scalars, vectors, 2d and 3d matrices are tensors)
- Pytorch supports hundreds of operations on tensors

### Autograd: Automatic Differentiation
- `Tensor` is one class `Function` is another class, both you need to get the complete history of computation on a tensor
- You can perform automatic differentiations for all operations on Tensors
- If you `require_grad` on a tensor it will track operations on it, and you can call `backward`
to computer the gradients on it automatically. You can use `detach` or wrap a code block with `torch.no_grad()`
if you don't want to track the tensors history (which use memory) if you don't need to compute the gradients.
(Like for evaluating a model)

### Neural Networks
- You can make neural networks using the `torch.nn` package which depends on `autograd`
- `torch.nn` contains `layers` and a method `forward(input)` that returns `output`
- Let's use this module to define a typical training procedure for the neural network

### Typical Training Procedure
1. Define a neural network that has some learnable parameters / weights
2. Iterate over a set of inputs
3. Process input throught the network
4. Compute the loss how fas is the output from being correct
5. Propagate the gradients back into the network's parameters
6. Update the weights of the network using a simple update rule
```
weight = weight - learning_rate * gradient
```

# Gradient Descent and Backpropagation

## Gradient Descent


> Our goal is to find the weights and biases so that the output of our network
approximates the correct output `y(x)` for all training input `x`. We quantify
how well we are achieving this goal with a cost function `C`. An example of a cost
function is the mean square error (MSE).

- Mean square error in english: Get the square of the difference between the the correct output
and the output of the network given each input x. Sum them and divide by the
number of inputs to get the average square error.

```
C(w, b) = sum for each x the function (square(y(x) - neural_network(x, w, b))  then divide by 2n

C(w, b) = Σx (y(x) - neural_network(x, w, b))²
          -----------------
               2 * n

n = number of training inputs
neural_network(x) = output of network given particular x and w, b
y(x) = the correct output given particular x
```

- For demonstration say we have a very simple cost function `C` which
we want to minimize which is dependent on just two variables `v1` and `v2`.
We want to find `v1` and `v2` such that it `C` is the minimum. Our strategy can be
say we start at a random `v = [v1, v2]` what we can do is go to
the direction where the change is the largest a little bit at a time. This is called
gradient descent.

- In mathematical/programmatic terms, given  `C(v1, v2)` or `C(v)` where `v = [v1, v2]`,
 the gradient vector of `C(v1, v2)` is: The partial derivatives of `v1` and `v2` with respect
  to `C` denoted by `∇C`. The strategy is the following:

```
while we are not satisfied:
    Grad C = ∇C = [ ∂C/∂v1 , ∂C/∂v2 ]
    v <- v − learning_rate * ∇C
```
- IMPORTANT: This algorithm is a basis of how to train a neural network. But we might converge to local minima
instead of a global minima. So there are many algorithms built on top of this idea.

- REFERENCE: [Chapter 1 of Section 2 Neural Network and Deep Learning (Learning with Gradient Descent) by Michael A. Nielsen2015](http://neuralnetworksanddeeplearning.com/chap1.html#learning_with_gradient_descent)


# Backpropagation
- So how to compute the gradient descent if our neural network function `neural_network(x, w, b)`
is complicated?  A fast algorithm for computing such gradients is called backpropagation.

> Motivation. In this section we will develop expertise with an intuitive understanding
of backpropagation, which is a way of computing gradients of expressions through recursive
application of chain rule. Understanding of this process and its subtleties is critical
 for you to understand, and effectively develop, design and debug Neural Networks.

 - You can check out Andrej Karpathy's article from Stanford's
CS231n Convolutional Neural Networks for Visual Recognition course [Backpropagation, Intuitions](http://cs231n.github.io/optimization-2/)

# Others

> In this section we’ll walk through a complete implementation of a toy Neural Network in 2 dimensions.
We’ll first implement a simple linear classifier and then extend the code to a 2-layer Neural Network.

- [(Andrej Karpathy) Stanford: Classifying a Toy Spiral Dataset](http://cs231n.github.io/neural-networks-case-study/)

