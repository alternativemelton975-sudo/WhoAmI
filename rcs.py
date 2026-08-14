import json

class SignalType:
    def __init__(self, type_name):
        self.type_name = type_name


class Creator:
    def __init__(self, name):
        self.name = name
        self.inputs = {}
        self.outputs = {}
        self.output_colors = {}

    def add_input(self, name, signal_type):
        self.inputs[name] = {"type": signal_type, "value": None}

    def add_output(self, name, signal_type):
        self.outputs[name] = {"type": signal_type, "value": None}

    def set_input(self, name, value):
        self.inputs[name]["value"] = value

    def get_input(self, name):
        return self.inputs[name]["value"]

    def set_output(self, name, value):
        self.outputs[name]["value"] = value

    def get_output(self, name):
        return self.outputs[name]["value"]

    def set_output_color(self, name, color_tuple):
        self.output_colors[name] = color_tuple

    def get_output_color(self, name):
        return self.output_colors.get(name)

    def to_json(self):
        data = {
            "name": self.name,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "output_colors": self.output_colors
        }
        return json.dumps(data)

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        creator = Creator(data["name"])

        creator.inputs = data["inputs"]
        creator.outputs = data["outputs"]
        creator.output_colors = data["output_colors"]

        return creator
