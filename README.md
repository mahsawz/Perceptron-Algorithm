# Perceptron-Algorithm

The Perceptron algorithm is a two-class (binary) classification machine learning algorithm.

It is a type of neural network model, perhaps the simplest type of neural network model.

It consists of a single node or neuron that takes a row of data as input and predicts a class label. This is achieved by calculating the weighted sum of the inputs and a bias (set to 1). The weighted sum of the input of the model is called the activation.

- Activation = Weights \* Inputs + Bias

If the activation is above 0.0, the model will output 1.0; otherwise, it will output 0.0.

- Predict 1: If Activation > 0.0
- Predict 0: If Activation <= 0.0

Given that the inputs are multiplied by model coefficients, like linear regression and logistic regression, it is good practice to normalize or standardize data prior to using the model.

Here, I have a file with "[gradientdescentforperceptron_nor.py](https://github.com/mahsawz/Perceptron-Algorithm/blob/main/gradientdescentforperceptron_nor.py)" name that implements the gradient descent algorithm for the perceptron, which is designed for NOR binary logic function and uses it to update its weights.

also I have another file with "[perceptron_algorithm.py](https://github.com/mahsawz/Perceptron-Algorithm/blob/main/perceptron_algorithm.py)" name that implements the Perceptron algorithm and run it on the [attached data](https://github.com/mahsawz/Perceptron-Algorithm/blob/main/data.txt).

The classification result:

![Image](https://github.com/mahsawz/Perceptron-Algorithm/blob/main/result-perceptron.png)

The error rate per iteration:

![Image](https://github.com/mahsawz/Perceptron-Algorithm/blob/main/result-accuracy.png)
