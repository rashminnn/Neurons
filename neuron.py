class neuron:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

        def activate(self, inputs):
            return sum(w*i for w,i in zip(self.weights,inputs))+self.bias