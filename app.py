from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        name = request.form.get("name")
        character_class = request.form.get("class")
        trait = request.form.get("trait")
        weapon = request.form.get("weapon")

        result = f"""
        <div class="card">
            <h2>{name}</h2>
            <p><b>Class:</b> {character_class}</p>
            <p><b>Trait:</b> {trait}</p>
            <p><b>Weapon:</b> {weapon}</p>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Character Creator</title>

        <style>
            body {{
                background: #111;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 30px;
            }}

            .container {{
                max-width: 800px;
                margin: auto;
                background: #222;
                padding: 20px;
                border-radius: 15px;
            }}

            input, select {{
                width: 80%;
                padding: 10px;
                margin: 8px;
                border-radius: 5px;
                border: none;
            }}

            button {{
                background: red;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }}

            .card {{
                margin-top: 20px;
                padding: 15px;
                background: #333;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>

        <div class="container">

            <h1>Character Creator</h1>

            <form method="POST">

                <input
                    type="text"
                    name="name"
                    placeholder="Character Name"
                    required
                >

                <br>

                <select name="class">
                    <option>Warrior</option>
                    <option>Mage</option>
                    <option>Ranger</option>
                    <option>Paladin</option>
                    <option>Assassin</option>
                </select>

                <br>

                <select name="trait">
                    <option>Brave</option>
                    <option>Wise</option>
                    <option>Mysterious</option>
                    <option>Loyal</option>
                    <option>Fearless</option>
                </select>

                <br>

                <select name="weapon">
                    <option>Sword</option>
                    <option>Bow</option>
                    <option>Staff</option>
                    <option>Dagger</option>
                    <option>Hammer</option>
                </select>

                <br><br>

                <button type="submit">
                    Create Character
                </button>

            </form>

            {result}

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
