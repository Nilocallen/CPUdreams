from modules import circuit, connector


class AndCircuit(circuit.Circuit):
    def __init__(self, label):
        circuit.Circuit.__init__(self, label)
        self.A = connector.Connector(self, 'A', activates=1)
        self.B = connector.Connector(self, 'B', activates=1)
        self.C = connector.Connector(self, 'C')

    def evaluate(self):
        self.C.set(self.A.value and self.B.value)
