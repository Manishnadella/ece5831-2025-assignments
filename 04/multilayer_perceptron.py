import numpy as np

class MultilayerPerceptron:
    def __init__(self):
        # Custom Weights and Bias
        self.w1 = np.array([[0.5, -1.0, 2.0], [1.5, 0.0, -0.5]])
        self.b1 = np.array([0.2, -0.3, 0.1])
        
        self.w2 = np.array([[1.0, -2.0], [-1.0, 1.0], [0.5, 0.5]])
        self.b2 = np.array([-0.1, 0.3])
        
        self.w3 = np.array([[2.0, -1.0], [1.5, 0.5]])
        self.b3 = np.array([0.3, -0.4])
    
    def identify(self, x):
        return x

    # define sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    

    def forward(self, x):
        # Forward pass
        a1 = np.dot(x, self.w1) + self.b1
        z1 = self.sigmoid(a1)
        
        a2 = np.dot(z1, self.w2) + self.b2
        z2 = self.sigmoid(a2)
        
        a3 = np.dot(z2, self.w3) + self.b3
        y = self.identify(a3)  
        
        return y
    

if __name__ == "__main__":
    print("Multi-layer perceptron with 3 layers")