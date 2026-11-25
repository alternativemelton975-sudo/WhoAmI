import rcs


class IdentityCreator(rcs.Creator):
    def __init__(self, name):
        super().__init__(name)

        self.add_input("input", rcs.SignalType("any"))
        self.add_output("output", rcs.SignalType("any"))

        self.set_output_color("output", (255, 25, 25))

    def process(self):
        input_signal = self.get_input("input")
        self.set_output("output", input_signal)
