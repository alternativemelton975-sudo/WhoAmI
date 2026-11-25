from flask import Flask, jsonify
import rcs
from IdentityCreator import IdentityCreator

app = Flask(__name__)


def create_identity(name):
    return IdentityCreator(name)


@app.route("/")
def home():
    process = create_identity("Identity")

    process.set_input("input", "Hello, World!")
    process.process()

    output = process.get_output("output")
    output_color = process.get_output_color("output")

    return jsonify({
        "name": process.name,
        "output": output,
        "output_color": output_color
    })


@app.route("/test")
def test():
    process = create_identity("Identity")

    process.set_input("input", "Testing Flask")
    process.process()

    json_data = process.to_json()

    loaded_process = rcs.Creator.from_json(json_data)
    loaded_process.process()

    return jsonify({
        "original_output": process.get_output("output"),
        "loaded_output": loaded_process.get_output("output"),
        "json": json_data
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
