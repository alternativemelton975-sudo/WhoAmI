import rcs

class IdentityCreator(rcs.Creator):
    def __init__(self, name):
        super().__init__(name)

        # Define input/output ports
        self.add_input("input", rcs.SignalType("any"))
        self.add_output("output", rcs.SignalType("any"))

        # Assign color to the output port
        self.set_output_color("output", (255, 25, 25))

    def process(self):
        input_signal = self.get_input("input")
        self.set_output("output", input_signal)


def create_identity(name):
    return IdentityCreator(name)


# -----------------------------
# Runtime test
# -----------------------------
process = create_identity("Identity")

process.set_input("input", "Hello, World!")
process.process()

output = process.get_output("output")
print(output)  # Should print "Hello, World!"

output_color = process.get_output_color("output")
print(output_color)  # Should print (255, 25, 25)

json_data = process.to_json()
print(json_data)

with open("identity_process.json", "w") as f:
    f.write(json_data)

with open("identity_process.json", "r") as f:
    json_data = f.read()

loaded_process = rcs.Creator.from_json(json_data)
loaded_process.process()

loaded_output = loaded_process.get_output("output")
print(loaded_output)  # Should print "Hello, World!"
