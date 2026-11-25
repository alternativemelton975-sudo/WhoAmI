from flask import Flask
import random

app = Flask(__name__)

names = [
    "Aria", "Drake", "Nova", "Phoenix", "Kai",
    "Luna", "Atlas", "Shadow", "Blaze", "Orion"
]

classes = [
    "Warrior",
    "Mage",
    "Ranger",
    "Paladin",
    "Assassin"
]

traits = [
    "Brave",
    "Clever",
    "Mysterious",
    "Loyal",
    "Fearless"
]


@app.route("/")
def create_character():
    character = {
        "name": random.choice(names),
        "class": random.choice(classes),
        "trait": random.choice(traits),
        "level": random.randint(1, 100)
    }

    return f"""
    <html>
    <head>
        <title>Character Creator</title>
        <style>
            body {{
                background-color: #121212;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
            }}

            .card {{
                width: 400px;
                margin: auto;
                background: #222;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 0 15px red;
            }}

            h1 {{
                color: #ff4444;
            }}

            button {{
                padding: 10px 20px;
                background: red;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Random Character</h1>
            <h2>{character["name"]}</h2>
            <p><strong>Class:</strong> {character["class"]}</p>
            <p><strong>Trait:</strong> {character["trait"]}</p>
            <p><strong>Level:</strong> {character["level"]}</p>

            <br>

            <button onclick="window.location.reload();">
                Generate New Character
            </button>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
