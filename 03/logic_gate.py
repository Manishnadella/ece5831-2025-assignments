import numpy as np

class LogicGate:
    def __init__(self):
        # defining params for each gate
        # each parameter has gate name and their corresponding weights and theta.
        self.params = {
            "AND":  (np.array([1.0, 1.0]),  1.5),
            "NAND": (np.array([-1.0, -1.0]), -1.5),
            "OR":   (np.array([0.7, 0.7]),  0.5),
            "NOR":  (np.array([-0.7, -0.7]), -0.5),
        }


    def _is_over_threshold(self, w, theta, x1, x2):
        """
        For given input x1,x2, weights (w1,w2) and threshold theta,
        return 1 if w1.x1 + w2.x2 > theta, else return 0.

        dot(w,x) computes w1.x1 + w2.x2
        """
        x = np.array([x1, x2], dtype=float)
        return int(np.dot(w, x) > theta)

    # defining functions for each gate
    # each gate function below uses parameters defined in self.params to compute threshold logic
    def and_gate(self, x1, x2):
        return self._is_over_threshold(*self.params["AND"], x1, x2)

    def nand_gate(self, x1, x2):
        return self._is_over_threshold(*self.params["NAND"], x1, x2)

    def or_gate(self, x1, x2):
        return self._is_over_threshold(*self.params["OR"], x1, x2)

    def nor_gate(self, x1, x2):
        return self._is_over_threshold(*self.params["NOR"], x1, x2)

    # defining test function to check output of gates
    def test(self):
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]  # input for gates

        # AND gate
        print("Results of AND gate:")
        for input in inputs:
            print(f'{input[0]} AND {input[1]} = {self.and_gate(input[0], input[1])}')

        # NAND gate
        print("\nResults of NAND gate:")
        for input in inputs:
            print(f'{input[0]} NAND {input[1]} = {self.nand_gate(input[0], input[1])}')

        # OR gate
        print("\nResults of OR gate:")
        for input in inputs:
            print(f'{input[0]} OR {input[1]} = {self.or_gate(input[0], input[1])}')

        # NOR gate
        print("\nResults of NOR gate:")
        for input in inputs:
            print(f'{input[0]} NOR {input[1]} = {self.nor_gate(input[0], input[1])}')   


if __name__ == "__main__":
    """
    This file contains LogicGate class writen by Manish Nadella.
    The code computes outputs based on the perceptron logic that is:
    1: w1.x1 + w2.x2 > theta
    0: w1.x1 + w2.x2 <= theta

    The weights and theta values that are defined can be plugged in along with the inputs of logic gates to get the output of the logic gates.
    For ex, consider AND gate with weights [1.0, 1.0] and theta 1.5 and inputs x1=1, x2=1, the output will be 1 as 1.0*1 + 1.0*1 = 2 > 1.5.

    The file module3.py calls the test function which prints the output of all logic gates.
    """
    print("This file contains implementation of weights and theta values for logic gates. Please run module3.py to test the implementation of logic gates.")