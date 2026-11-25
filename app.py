from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    character_html = ""

    if request.method == "POST":
        name = request.form.get("name")
        character_class = request.form.get("class")
        trait = request.form.get("trait")
        weapon = request.form.get("weapon")

        character_html = f"""
        <div class="card result">
            <h2>{name}</h2>
            <p><strong>Class:</strong> {character_class}</p>
            <p><strong>Trait:</strong> {trait}</p>
            <p><strong>Weapon:</strong> {weapon}</p>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Character Creator</title>

        <style>
            body {{
                background:#121212;
                color:white;
                font-family:Arial,sans-serif;
                text-align:center;
                padding:40px;
            }}

            .card {{
                max-width:500px;
                margin:auto;
                background:#222;
                padding:25px;
                border-radius:15px;
                box-shadow:0 0 15px red;
            }}

            input, select {{
                width:90%;
                padding:10px;
                margin:10px;
                border:none;
                border-radius:5px;
            }}

            button {{
                background:red;
                color:white;
                border:none;
                padding:12px 20px;
                border-radius:8px;
                cursor:pointer;
            }}

            .result {{
                margin-top:25px;
            }}
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Character Creator</h1>

            <form method="POST">

                <input
                    type="text"
                    name="name"
                    placeholder="Character Name"
                    required
                >

                <select name="class">
                    <option>Warrior</option>
                    <option>Mage</option>
                    <option>Ranger</option>
                    <option>Paladin</option>
                    <option>Assassin</option>
                </select>

                <select name="trait">
                    <option>Brave</option>
                    <option>Wise</option>
                    <option>Mysterious</option>
                    <option>Loyal</option>
                    <option>Fearless</option>
                </select>

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

            {character_html}

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
