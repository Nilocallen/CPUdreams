from modules import circuit, connector


class NotCircuit(circuit.Circuit):
    def __init__(self, name):
        circuit.Circuit.__init__(self, name)
        # self.connectors = list()
        self.A = connector.Connector(self, 'A', activates=1)
        self.B = connector.Connector(self, 'B',)

    def evaluate(self):
        self.B.set(not self.A.value)
