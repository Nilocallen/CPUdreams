from modules import circuit, connector


class NotCircuit(circuit.Circuit):
    def __init__(self, name):
        circuit.Circuit.__init__(self, name)
        # self.connectors = list()
        self.inputs.append(connector.Connector(self, 'A', activates=1))
        self.outputs.append(connector.Connector(self, 'B'))

    def evaluate(self):
        self.outputs[0].set(not self.inputs[0].value)
