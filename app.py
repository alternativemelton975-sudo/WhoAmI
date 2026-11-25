from flask import Flask, request, render_template_string, jsonify
import random
from datetime import datetime

app = Flask(__name__)

characters = {}


class Character:
    """Represents a hero character with stats and progression."""

    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power
        self.level = 1
        self.experience = 0

        self.stats = {
            "strength": random.randint(5, 20),
            "intelligence": random.randint(5, 20),
            "agility": random.randint(5, 20),
            "endurance": random.randint(5, 20),
        }

        self.created_date = datetime.now().isoformat()

    def gain_experience(self, amount):
        self.experience += amount

        if self.experience >= 100:
            levels = self.experience // 100
            self.level += levels
            self.experience %= 100

            for stat in self.stats:
                self.stats[stat] += random.randint(1, 3)

            return f"{self.name} leveled up to Level {self.level}!"

        return None

    def total_power(self):
        return sum(self.stats.values()) + (self.level * 10)

    def to_dict(self):
        return {
            "name": self.name,
            "power": self.power,
            "level": self.level,
            "experience": self.experience,
            "stats": self.stats,
            "created_date": self.created_date,
            "total_power": self.total_power()
        }


@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Character Builder</title>
        <style>
            body{
                font-family:Arial,sans-serif;
                max-width:900px;
                margin:auto;
                padding:20px;
                background:#121212;
                color:white;
            }
            input,button{
                padding:10px;
                margin:5px;
            }
            .card{
                border:1px solid #444;
                padding:15px;
                margin-top:15px;
                border-radius:10px;
                background:#1f1f1f;
            }
        </style>
    </head>
    <body>
        <h1>⚔️ Character Builder ⚔️</h1>

        <form action="/create" method="post">
            <input name="name" placeholder="Hero Name" required>
            <input name="power" placeholder="Power" required>
            <button type="submit">Create Character</button>
        </form>

        <h2>Characters</h2>

        {% for character in characters %}
        <div class="card">
            <h3>{{ character.name }}</h3>
            <p><b>Power:</b> {{ character.power }}</p>
            <p><b>Level:</b> {{ character.level }}</p>
            <p><b>Total Power:</b> {{ character.total_power() }}</p>
        </div>
        {% endfor %}
    </body>
    </html>
    """

    return render_template_string(
        html,
        characters=characters.values()
    )


@app.route("/create", methods=["POST"])
def create_character():
    name = request.form.get("name")
    power = request.form.get("power")

    character = Character(name, power)

    characters[name] = character

    return f"""
    <h1>{name} Created!</h1>

    <p>Power: {power}</p>

    <p>Strength: {character.stats['strength']}</p>
    <p>Intelligence: {character.stats['intelligence']}</p>
    <p>Agility: {character.stats['agility']}</p>
    <p>Endurance: {character.stats['endurance']}</p>

    <a href="/">Back</a>
    """


@app.route("/api/characters")
def get_characters():
    return jsonify([
        char.to_dict()
        for char in characters.values()
    ])


@app.route("/battle")
def battle():
    names = list(characters.keys())

    if len(names) < 2:
        return "Create at least two characters first."

    char1 = characters[names[0]]
    char2 = characters[names[1]]

    power1 = char1.total_power()
    power2 = char2.total_power()

    winner = char1 if power1 > power2 else char2

    experience_gain = 50 + (winner.level * 10)

    winner.gain_experience(experience_gain)

    return {
        "character_1": char1.name,
        "character_2": char2.name,
        "power_1": power1,
        "power_2": power2,
        "winner": winner.name,
        "experience_awarded": experience_gain
    }
@app.route("/tournament")
def tournament():

    if len(heroes) < 2:

        return """
        <html>
        <body style="
            background:#020617;
            color:white;
            text-align:center;
            font-family:Arial;
        ">
            <h1>Create at least two heroes first.</h1>
            <a href="/" style="color:gold;">Home</a>
        </body>
        </html>
        """

    contestants = list(heroes.values())

    random.shuffle(contestants)

    output = """
    <html>

    <head>

    <style>

    body{
        background:#020617;
        color:white;
        font-family:Arial,sans-serif;
        text-align:center;
        padding:20px;
    }

    h1{
        color:#38bdf8;
    }

    a{
        color:gold;
        text-decoration:none;
        font-size:18px;
    }

    hr{
        border:1px solid #38bdf8;
    }

    .battle-card{

        background:#1e293b;

        color:#f8fafc;

        margin:15px auto;

        padding:20px;

        max-width:800px;

        border-radius:12px;

        border:2px solid #38bdf8;

        box-shadow:0 0 10px #38bdf8;
    }

    .winner{
        color:#22c55e;
        font-weight:bold;
    }

    .champion{

        background:#451a03;

        color:white;

        padding:25px;

        margin-top:30px;

        border-radius:15px;

        border:3px solid gold;

        box-shadow:0 0 15px gold;
    }

    </style>

    </head>

    <body>

    <h1>⚔ HERO TOURNAMENT ⚔</h1>

    <a href="/">⬅ Home</a>

    <hr>
    """

    while len(contestants) > 1:

        hero1 = contestants.pop(0)
        hero2 = contestants.pop(0)

        winner = (
            hero1
            if hero1["total_power"] >= hero2["total_power"]
            else hero2
        )

       output += f"""
<div style="

    background:#1e293b;

    color:#f8fafc;

    margin:15px;

    padding:15px;

    border-radius:12px;

    border:2px solid #38bdf8;

    box-shadow:0 0 10px #38bdf8;

">

    <h3>
        {hero1['name']}
        VS
        {hero2['name']}
    </h3>

    <p>
        {hero1['name']} Power:
        {hero1['total_power']}
    </p>

    <p>
        {hero2['name']} Power:
        {hero2['total_power']}
    </p>

    <p>
        Winner:
        <span style="
            color:#22c55e;
            font-weight:bold;
        ">
            {winner['name']}
        </span>
    </p>

</div>
"""

        contestants.append(winner)

    champion = contestants[0]

    output += f"""

    <div class="champion">

        <h1>🏆 TOURNAMENT CHAMPION 🏆</h1>

        <h2>{champion['name']}</h2>

        <p>Class: {champion['class']}</p>

        <p>Power: {champion['power']}</p>

        <p>Total Power: {champion['total_power']}</p>

    </div>

    </body>
    </html>
    """

    return output

@app.route("/team")
def team():

    if not characters:
        return jsonify({"message": "No characters found"})

    total_power = sum(
        c.total_power() for c in characters.values()
    )

    avg_level = (
        sum(c.level for c in characters.values())
        / len(characters)
    )

    return jsonify({
        "members": [c.name for c in characters.values()],
        "team_size": len(characters),
        "total_power": total_power,
        "average_level": round(avg_level, 1)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
