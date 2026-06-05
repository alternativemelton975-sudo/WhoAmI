import rcs 
class IdentityCreator(rcs.Creator):
    def __init__(self, name):
        super().__init__(name)
        self.add_input("input", rcs.SignalType("any"))
        self.add_output("output", rcs.SignalType("any"))

    def process(self):
        input_signal = self.get_input("input")
        self.set_output("output", input_signal)
def create_identity(name):
    return IdentityCreator(name)

   color = (255, 25, 25) 

   process = create_identity("Identity")

   process.set_input("input", "Hello, World!")
    process.process()

    output = process.get_output("output")
    print(output)  # Should print "Hello, World!"
    output_color = process.get_output_color("output")
    print(output_color)  # Should print (255, 25, 25)

    json_data = process.to_json()
    print(json_data)  # Should print the JSON representation of the process

    with open("identity_process.json", "w") as f:
        f.write(json_data)
    with open("identity_process.json", "r") as f:
        loaded_json = f.read()
