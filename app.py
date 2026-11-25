from flask import Flask, request
from datetime import datetime
import random

app = Flask(__name__)

heroes = {}

POWER_MAP = {
    "Warrior": "Lightning",
    "Mage": "Arcane Magic",
    "Ranger": "Nature",
    "Paladin": "Holy Light",
    "Assassin": "Shadow"
}


def write_log(hero):

    with open("hero_logs.txt", "a") as log:

        log.write("\n")
        log.write("=" * 50 + "\n")
        log.write(f"Created: {datetime.now()}\n")
        log.write(f"Hero: {hero['name']}\n")
        log.write(f"Class: {hero['class']}\n")
        log.write(f"Trait: {hero['trait']}\n")
        log.write(f"Weapon: {hero['weapon']}\n")
        log.write(f"Power: {hero['power']}\n")
        log.write(f"Total Power: {hero['total_power']}\n")
        log.write("=" * 50 + "\n")


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
            strength +
            intelligence +
            agility +
            endurance
        )

        hero_title = random.choice([
            "Storm Guardian",
            "Shadow Walker",
            "Dragon Slayer",
            "Light Bringer",
            "Arcane Master",
            "Iron Defender"
        ])

        biography = (
            f"{name} the {hero_title} is a "
            f"{trait.lower()} {hero_class.lower()} "
            f"who channels {power.lower()} through a "
            f"{weapon.lower()}."
        )

        hero_data = {
            "name": name,
            "class": hero_class,
            "trait": trait,
            "weapon": weapon,
            "power": power,
            "strength": strength,
            "intelligence": intelligence,
            "agility": agility,
            "endurance": endurance,
            "total_power": total_power
        }

        heroes[name] = hero_data

        write_log(hero_data)

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
                background:#0d1117;
                color:white;
                font-family:Arial;
                text-align:center;
                padding:30px;
            }}

            .container {{
                max-width:900px;
                margin:auto;
                background:#161b22;
                padding:25px;
                border-radius:15px;
            }}

            input,select {{
                width:80%;
                padding:12px;
                margin:8px;
                border:none;
                border-radius:8px;
            }}

            button {{
                background:#dc2626;
                color:white;
                padding:12px 30px;
                border:none;
                border-radius:8px;
                cursor:pointer;
            }}

            button:hover {{
                background:#b91c1c;
            }}

            .card {{
                margin-top:20px;
                background:#21262d;
                padding:20px;
                border-radius:12px;
                text-align:left;
            }}

            a {{
                color:gold;
                text-decoration:none;
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

        <br>

        <a href="/heroes">Hero Registry</a>

        <br><br>

        <a href="/battle">Battle Arena</a>

        <br><br>

        <a href="/tournament">Tournament Mode</a>

        <br><br>

        <a href="/logs">Hero Logs</a>

        {result}

    </div>

    </body>
    </html>
    """


@app.route("/heroes")
def heroes_page():

    output = """
    <h1>Hero Registry</h1>
    <a href="/">Home</a>
    <hr>
    """

    for hero in heroes.values():

        output += f"""
        <div style="
            margin:20px;
            padding:15px;
            border:1px solid white;
        ">
            <h2>{hero['name']}</h2>
            <p>Class: {hero['class']}</p>
            <p>Power: {hero['power']}</p>
            <p>Total Power: {hero['total_power']}</p>
        </div>
        """

    return output


@app.route("/battle")
def battle():

    hero_names = list(heroes.keys())

    if len(hero_names) < 2:

        return """
        <h1>Create at least two heroes first.</h1>
        <a href="/">Home</a>
        """

    hero1 = heroes[hero_names[0]]
    hero2 = heroes[hero_names[1]]

    winner = (
        hero1
        if hero1["total_power"] > hero2["total_power"]
        else hero2
    )

    return f"""
    <h1>⚔ Battle Arena ⚔</h1>

    <h2>{hero1['name']} VS {hero2['name']}</h2>

    <p>{hero1['name']} Power: {hero1['total_power']}</p>
    <p>{hero2['name']} Power: {hero2['total_power']}</p>

    <h1>🏆 Winner: {winner['name']}</h1>

    <a href="/">Home</a>
    """


@app.route("/tournament")
def tournament():

    if len(heroes) < 2:

        return """
        <h1>Create at least two heroes first.</h1>
        <a href="/">Home</a>
        """

    contestants = list(heroes.values())

    random.shuffle(contestants)

    output = """
    <h1>⚔ HERO TOURNAMENT ⚔</h1>
    <a href="/">Home</a>
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
            background:#222;
            margin:15px;
            padding:15px;
            border-radius:10px;
        ">

            <h3>
                {hero1['name']}
                VS
                {hero2['name']}
            </h3>

            <p>
                Winner:
                <b>{winner['name']}</b>
            </p>

        </div>
        """

        contestants.append(winner)

    champion = contestants[0]

    output += f"""
    <hr>

    <h1 style="color:gold;">
        🏆 Tournament Champion
    </h1>

    <h2>{champion['name']}</h2>

    <p>Class: {champion['class']}</p>

    <p>Total Power: {champion['total_power']}</p>
    """

    return output


@app.route("/logs")
def logs():

    try:

        with open("hero_logs.txt", "r") as file:
            return f"<pre>{file.read()}</pre>"

    except FileNotFoundError:

        return """
        <h1>No logs found.</h1>
        <a href="/">Home</a>
        """


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000,
        debug=True
    )
