from modules import circuit, connector


class AndCircuit(circuit.Circuit):
    def __init__(self, label):
        circuit.Circuit.__init__(self, label)
        self.inputs.append(connector.Connector(self, 'A', activates=1))
        self.inputs.append(connector.Connector(self, 'B', activates=1))
        self.outputs.append(connector.Connector(self, 'C'))

    def evaluate(self):
        self.outputs[0].set(self.inputs[0].value and self.inputs[1].value)
