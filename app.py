from flask import Flask, request
import random

app = Flask(__name__)

POWER_MAP = {
    "Warrior": "Lightning",
    "Mage": "Arcane Magic",
    "Ranger": "Nature",
    "Paladin": "Holy Light",
    "Assassin": "Shadow"
}


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        name = request.form.get("name")
        hero_class = request.form.get("class")
        trait = request.form.get("trait")
        weapon = request.form.get("weapon")

        strength = random.randint(5, 15)
        intelligence = random.randint(5, 15)
        agility = random.randint(5, 15)
        endurance = random.randint(5, 15)

        if hero_class == "Warrior":
            strength += 10
            endurance += 5

        elif hero_class == "Mage":
            intelligence += 10

        elif hero_class == "Ranger":
            agility += 10

        elif hero_class == "Paladin":
            strength += 5
            endurance += 10

        elif hero_class == "Assassin":
            agility += 10
            intelligence += 5

        if trait == "Brave":
            strength += 5

        elif trait == "Wise":
            intelligence += 5

        elif trait == "Mysterious":
            agility += 3
            intelligence += 3

        elif trait == "Loyal":
            endurance += 5

        elif trait == "Fearless":
            strength += 3
            endurance += 5

        power = POWER_MAP.get(hero_class, "Unknown")

        total_power = (
            strength
            + intelligence
            + agility
            + endurance
        )

        titles = [
            "Storm Guardian",
            "Shadow Walker",
            "Dragon Slayer",
            "Light Bringer",
            "Arcane Master",
            "Iron Defender"
        ]

        hero_title = random.choice(titles)

        biography = (
            f"{name} the {hero_title} is a "
            f"{trait.lower()} {hero_class.lower()} "
            f"who channels {power.lower()} through a "
            f"{weapon.lower()}."
        )

        result = f"""
        <div class="card">
            <h2>⚔ HERO IDENTITY REPORT ⚔</h2>

            <h1>{name}</h1>

            <p><b>Title:</b> {hero_title}</p>

            <p><b>Class:</b> {hero_class}</p>

            <p><b>Trait:</b> {trait}</p>

            <p><b>Power:</b> {power}</p>

            <p><b>Weapon:</b> {weapon}</p>

            <hr>

            <h3>Stats</h3>

            <p>💪 Strength: {strength}</p>

            <p>🧠 Intelligence: {intelligence}</p>

            <p>🏃 Agility: {agility}</p>

            <p>🛡 Endurance: {endurance}</p>

            <p><b>Total Power:</b> {total_power}</p>

            <hr>

            <h3>Biography</h3>

            <p>{biography}</p>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>Hero Identity Generator</title>

        <style>

            body {{
                background: #0d1117;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 30px;
            }}

            .container {{
                max-width: 900px;
                margin: auto;
                background: #161b22;
                padding: 25px;
                border-radius: 15px;
            }}

            input, select {{
                width: 80%;
                padding: 12px;
                margin: 8px;
                border-radius: 8px;
                border: none;
            }}

            button {{
                background: #dc2626;
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }}

            button:hover {{
                background: #b91c1c;
            }}

            .card {{
                margin-top: 20px;
                background: #21262d;
                padding: 20px;
                border-radius: 12px;
                text-align: left;
            }}

            hr {{
                border: 1px solid #444;
            }}

        </style>

    </head>

    <body>

        <div class="container">

            <h1>⚔ Hero Identity Generator ⚔</h1>

            <p>Create your unique hero identity.</p>

            <form method="POST">

                <input
                    type="text"
                    name="name"
                    placeholder="Hero Name"
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
                    Generate Hero
                </button>

            </form>

            {result}

        </div>

    </body>

    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
