# File:     connector.py
# Author:   Colin Allen
# A connector sits in between the inputs and outputs of a circuit to connect the two together.
# This schema is taken from http://openbookproject.net/courses/python4fun/logic.html


class Connector:
    def __init__(self, owner, label, activates=0, monitor=0):
        self.value = None
        self.owner = owner
        self.label = label
        self.monitor = monitor
        self.activates = activates

        self.connects = []

    def connect(self, inputs):
        """
        Connects an output connector to a set of inputs.
        :param inputs: List (or single element) of inputs
        """
        if not isinstance(inputs, list):
            inputs = [inputs]
        for input in inputs:
            self.connects.append(input)

    def set(self, value):
        if self.value == value:
            return
        self.value = value
        if self.activates:
            self.owner.evaluate()
        if self.monitor:
            print("Connector {0}-{1} set to {2}".format(self.owner.label,
                                                        self.label,
                                                        self.value))
            # TODO show in sim

        for con in self.connects:
            con.set(value)
