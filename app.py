from flask import Flask, request, render_template_string, jsonify
import random
from datetime import datetime

app = Flask(__name__)

characters = {}


class Character:
    def __init__(self, name, power):
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


def write_log(character):

    with open("hero_logs.txt", "a") as f:

        f.write(
            f"{datetime.now()} | "
            f"{character.name} | "
            f"{character.power} | "
            f"Power Score: {character.total_power()}\n"
        )


@app.route("/")
def home():

    html = """
    <!DOCTYPE html>

    <html>

    <head>

    <title>Hero Identity Generator</title>

    <style>

    body{
        font-family:Arial,sans-serif;
        max-width:1000px;
        margin:auto;
        padding:20px;
        background:#121212;
        color:white;
        text-align:center;
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

    a{
        color:gold;
        text-decoration:none;
    }

    </style>

    </head>

    <body>

    <h1>⚔ Hero Identity Generator ⚔</h1>

    <form action="/create" method="post">

        <input
            name="name"
            placeholder="Hero Name"
            required
        >

        <input
            name="power"
            placeholder="Hero Power"
            required
        >

        <button type="submit">
            Create Hero
        </button>

    </form>

    <br>

    <a href="/heroes">Hero Registry</a>

    <br><br>

    <a href="/battle">Battle Arena</a>

    <br><br>

    <a href="/tournament">Tournament Mode</a>

    <br><br>

    <a href="/logs">Hero Logs</a>

    <hr>

    <h2>Current Heroes</h2>

    {% for character in characters %}

        <div class="card">
            <h3>{{ character.name }}</h3>

            <p>Power: {{ character.power }}</p>

            <p>Level: {{ character.level }}</p>

            <p>Total Power:
               {{ character.total_power() }}</p>
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

    write_log(character)

    return f"""
    <h1>{name} Created!</h1>

    <p>Power: {power}</p>

    <p>Strength: {character.stats['strength']}</p>

    <p>Intelligence: {character.stats['intelligence']}</p>

    <p>Agility: {character.stats['agility']}</p>

    <p>Endurance: {character.stats['endurance']}</p>

    <a href="/">Back Home</a>
    """


@app.route("/heroes")
def heroes():

    output = """
    <html>
    <body style="
        background:#121212;
        color:white;
        font-family:Arial;
        text-align:center;
    ">
    <h1>Hero Registry</h1>
    """

    for character in characters.values():

        output += f"""
        <div style="
            background:#1f1f1f;
            margin:10px;
            padding:15px;
            border-radius:10px;
        ">
            <h2>{character.name}</h2>

            <p>Power: {character.power}</p>

            <p>Level: {character.level}</p>

            <p>Total Power:
               {character.total_power()}</p>

        </div>
        """

    output += '<a href="/">Home</a></body></html>'

    return output


@app.route("/battle")
def battle():

    names = list(characters.keys())

    if len(names) < 2:
        return "Create at least two heroes first."

    char1 = characters[names[0]]
    char2 = characters[names[1]]

    power1 = char1.total_power()
    power2 = char2.total_power()

    winner = char1 if power1 >= power2 else char2

    return f"""
    <html>

    <body style="
        background:#020617;
        color:white;
        text-align:center;
        font-family:Arial;
    ">

    <h1>⚔ Battle Arena ⚔</h1>

    <h2>{char1.name} VS {char2.name}</h2>

    <p>{char1.name}: {power1}</p>

    <p>{char2.name}: {power2}</p>

    <h2 style="color:#22c55e;">
        Winner: {winner.name}
    </h2>

    <a href="/">Home</a>

    </body>

    </html>
    """


@app.route("/tournament")
def tournament():

    if len(characters) < 2:
        return "Create at least two heroes first."

    contestants = [
        character.to_dict()
        for character in characters.values()
    ]

    random.shuffle(contestants)

    output = """
    <html>
    <body style="
        background:#020617;
        color:white;
        text-align:center;
        font-family:Arial;
        padding:20px;
    ">

    <h1 style="color:#38bdf8;">
        ⚔ HERO TOURNAMENT ⚔
    </h1>

    <a href="/" style="color:gold;">
        Home
    </a>

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
            margin:15px auto;
            padding:15px;
            border-radius:12px;
            border:2px solid #38bdf8;
            box-shadow:0 0 10px #38bdf8;
            max-width:700px;
        ">

            <h3>
                {hero1['name']} VS {hero2['name']}
            </h3>

            <p>
                Winner:
                <span style="color:#22c55e;">
                    {winner['name']}
                </span>
            </p>

        </div>
        """

        contestants.append(winner)

    champion = contestants[0]

    output += f"""
    <div style="
        background:#451a03;
        color:white;
        margin:25px auto;
        padding:25px;
        border-radius:15px;
        border:3px solid gold;
        max-width:700px;
    ">

        <h1 style="color:gold;">
            🏆 Tournament Champion 🏆
        </h1>

        <h2>{champion['name']}</h2>

        <p>Total Power:
           {champion['total_power']}</p>

    </div>

    </body>
    </html>
    """

    return output


@app.route("/logs")
def logs():

    try:

        with open("hero_logs.txt", "r") as f:
            content = f.read()

        return f"""
        <html>

        <body style="
            background:#000814;
            color:#7dd3fc;
            font-family:Consolas;
            padding:20px;
        ">

        <h1 style="color:gold;">
            Hero Logs
        </h1>

        <pre>{content}</pre>

        <a href="/" style="color:gold;">
            Home
        </a>

        </body>

        </html>
        """

    except FileNotFoundError:

        return """
        <h1>No logs found</h1>
        <a href="/">Home</a>
        """


@app.route("/api/characters")
def get_characters():
    return jsonify([
        c.to_dict()
        for c in characters.values()
    ])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
