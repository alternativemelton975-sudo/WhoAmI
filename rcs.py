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

    # Input / Output definitions

    def add_input(self, name, signal_type):
        self.inputs[name] = {
            "type": signal_type,
            "value": None
        }

    def add_output(self, name, signal_type):
        self.outputs[name] = {
            "type": signal_type,
            "value": None
        }

    # Input / Output values

    def set_input(self, name, value):
        self.inputs[name]["value"] = value

    def get_input(self, name):
        return self.inputs[name]["value"]

    def set_output(self, name, value):
        self.outputs[name]["value"] = value

    def get_output(self, name):
        return self.outputs[name]["value"]

    # Output color

    def set_output_color(self, name, color_tuple):
        self.output_colors[name] = color_tuple

    def get_output_color(self, name):
        return self.output_colors.get(name)

    # JSON Serialization

    def to_json(self):
        safe_inputs = {
            key: {
                "type": value["type"].type_name,
                "value": value["value"]
            }
            for key, value in self.inputs.items()
        }

        safe_outputs = {
            key: {
                "type": value["type"].type_name,
                "value": value["value"]
            }
            for key, value in self.outputs.items()
        }

        data = {
            "class": self.__class__.__name__,
            "name": self.name,
            "inputs": safe_inputs,
            "outputs": safe_outputs,
            "output_colors": self.output_colors
        }

        return json.dumps(data)

    # JSON Loading

    @staticmethod
    def from_json(json_data):
        from IdentityCreator import IdentityCreator

        data = json.loads(json_data)

        if data.get("class") == "IdentityCreator":
            creator = IdentityCreator(data["name"])
        else:
            creator = Creator(data["name"])

        creator.inputs = {
            key: {
                "type": SignalType(value["type"]),
                "value": value["value"]
            }
            for key, value in data["inputs"].items()
        }

        creator.outputs = {
            key: {
                "type": SignalType(value["type"]),
                "value": value["value"]
            }
            for key, value in data["outputs"].items()
        }

        creator.output_colors = data["output_colors"]

        return creator
