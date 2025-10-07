
from multilayer_perceptron import MultilayerPerceptron
import numpy as np

mlp = MultilayerPerceptron()
x = np.array([1.0, 0.5])
print(f'Input to the MLP: {x}')
y = mlp.forward(x)
print(f'Output of the MLP: {y}') 